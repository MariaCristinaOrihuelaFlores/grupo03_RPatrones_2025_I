import argparse
import time
import pandas as pd
import numpy as np
import torch
from torch import nn
import torch.nn.functional as F
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score, classification_report, confusion_matrix
from collections import Counter
import wandb

parser = argparse.ArgumentParser()
parser.add_argument('--hidden_dim', type=int, default=128)
parser.add_argument('--layers', type=int, default=2)
args = parser.parse_args()

# Dataset
df = pd.read_csv("Grisoni_et_al_2016_EnvInt88.csv")
df["Class"] = df["Class"].astype(int) - 1

X = df.drop(columns=["CAS", "SMILES", "Set", "logBCF", "Class"])
y = df["Class"].values

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_trainval = X_scaled[df["Set"] == "Train"]
y_trainval = y[df["Set"] == "Train"]
X_test = X_scaled[df["Set"] == "Test"]
y_test = y[df["Set"] == "Test"]

X_train, X_val, y_train, y_val = train_test_split(X_trainval, y_trainval, test_size=0.2, random_state=13, stratify=y_trainval)

X_train_tensor = torch.tensor(X_train, dtype=torch.float32)
y_train_tensor = torch.tensor(y_train, dtype=torch.long)
X_val_tensor = torch.tensor(X_val, dtype=torch.float32)
y_val_tensor = torch.tensor(y_val, dtype=torch.long)
X_test_tensor = torch.tensor(X_test, dtype=torch.float32)
y_test_tensor = torch.tensor(y_test, dtype=torch.long)

# Modelo Flexible
def build_model(input_dim, hidden_dim, num_layers):
    layers = []
    layers.append(nn.Linear(input_dim, hidden_dim))
    layers.append(nn.BatchNorm1d(hidden_dim))
    layers.append(nn.LeakyReLU(0.01))
    layers.append(nn.Dropout(0.5))

    for _ in range(num_layers - 1):
        layers.append(nn.Linear(hidden_dim, hidden_dim))
        layers.append(nn.BatchNorm1d(hidden_dim))
        layers.append(nn.LeakyReLU(0.01))
        layers.append(nn.Dropout(0.2))

    layers.append(nn.Linear(hidden_dim, 3))
    return nn.Sequential(*layers)

model = build_model(X_train.shape[1], args.hidden_dim, args.layers)

# Loss: Focal + Label Smoothing
class FocalLossWithLabelSmoothing(nn.Module):
    def __init__(self, alpha=None, gamma=2, smoothing=0.1, n_classes=3):
        super().__init__()
        self.alpha = alpha
        self.gamma = gamma
        self.smoothing = smoothing
        self.n_classes = n_classes

    def smooth_labels(self, target):
        with torch.no_grad():
            true_dist = torch.zeros(size=(target.size(0), self.n_classes), device=target.device)
            true_dist.fill_(self.smoothing / self.n_classes)
            true_dist.scatter_(1, target.unsqueeze(1), 1 - self.smoothing)
        return true_dist

    def forward(self, logits, target):
        prob = F.softmax(logits, dim=1)
        log_prob = F.log_softmax(logits, dim=1)
        smoothed_target = self.smooth_labels(target)
        focal_term = (1 - prob) ** self.gamma
        if self.alpha is not None:
            alpha = self.alpha.to(logits.device)
            focal_term = alpha.unsqueeze(0) * focal_term
        loss = -smoothed_target * focal_term * log_prob
        return loss.sum(dim=1).mean()

cnt = Counter(y_train)
alpha = torch.tensor([1 / cnt[c] for c in sorted(cnt)], dtype=torch.float32)

criterion = FocalLossWithLabelSmoothing(alpha=alpha, gamma=2, smoothing=0.1, n_classes=3)
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)


def init_weights(m):
    if isinstance(m, nn.Linear):
        nn.init.kaiming_normal_(m.weight, nonlinearity='leaky_relu')
        if m.bias is not None:
            nn.init.constant_(m.bias, 0)

model.apply(init_weights)

# Sweep
epochs = 60 
patience = 60 # igual que epocas para comparar los tiempos de ejecución
best_val_loss = float('inf')
counter = 0
start_time = time.time()

wandb.init(project="ch6_classification", entity="zerocris13")

for epoch in range(epochs):
    model.train()
    optimizer.zero_grad()
    y_pred = model(X_train_tensor)
    loss = criterion(y_pred, y_train_tensor)
    loss.backward()
    optimizer.step()

    for name, param in model.named_parameters():
        if param.requires_grad and param.grad is not None:
            wandb.log({f"gradients/{name}": param.grad.norm().item()})

    model.eval()
    with torch.no_grad():
        y_val_pred = model(X_val_tensor)
        val_loss = criterion(y_val_pred, y_val_tensor)

    wandb.log({"epoch": epoch + 1, "train_loss": loss.item(), "val_loss": val_loss.item()})
    print(f"Epoch {epoch+1}, Train Loss: {loss.item():.4f}, Val Loss: {val_loss.item():.4f}")

    if val_loss.item() < best_val_loss:
        best_val_loss = val_loss.item()
        best_model_state = model.state_dict()
        counter = 0
    else:
        counter += 1
        if counter >= patience:
            print("Early stopping")
            break

elapsed = time.time() - start_time

# Evaluación
model.load_state_dict(best_model_state)
model.eval()
with torch.no_grad():
    y_test_pred = model(X_test_tensor)
    y_pred_labels = y_test_pred.argmax(dim=1).numpy()

acc = accuracy_score(y_test, y_pred_labels)
f1_weighted = f1_score(y_test, y_pred_labels, average='weighted')
precision = precision_score(y_test, y_pred_labels, average='weighted')
recall = recall_score(y_test, y_pred_labels, average='weighted')

report = classification_report(y_test, y_pred_labels, digits=4)
print("\nClassification Report:\n", report)

wandb.log({
    "confusion_matrix": wandb.plot.confusion_matrix(
        probs=None,
        y_true=y_test,
        preds=y_pred_labels,
        class_names=["Class 0", "Class 1", "Class 2"]
    )
})

# Log de métricas finales
wandb.log({
    "test_acc": acc,
    "test_f1_weighted": f1_weighted,
    "test_precision": precision,
    "test_recall": recall,
    "training_time_sec": elapsed
})

wandb.finish()