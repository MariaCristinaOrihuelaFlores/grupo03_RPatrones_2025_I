# Importar ibrerias
import time
import wandb
import pandas as pd
import numpy as np
import torch
from torch import nn
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score
import argparse

# Cargar Dataset
df = pd.read_csv("Grisoni_et_al_2016_EnvInt88.csv")

# Normalizar de logBCF
logBCF_min = df["logBCF"].min()
logBCF_max = df["logBCF"].max()
df["logBCF_norm"] = (df["logBCF"] - logBCF_min) / (logBCF_max - logBCF_min)

X = df.drop(columns=["CAS", "SMILES", "Set", "Class", "logBCF", "logBCF_norm"])
y = df["logBCF_norm"].values
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Dividir el dataset en entrenamiento/validación y test
X_trainval = X_scaled[df["Set"] == "Train"]
y_trainval = y[df["Set"] == "Train"]
X_test = X_scaled[df["Set"] == "Test"]
y_test_true = df[df["Set"] == "Test"]["logBCF"].values

X_train, X_val, y_train, y_val = train_test_split(X_trainval, y_trainval, test_size=0.2, random_state=13)

# Modelo base parametrizable
def build_model(input_dim, layers, hidden_dim, dropout, activation):
    activ = nn.SiLU() if activation == "silu" else nn.ReLU()
    modules = []
    in_dim = input_dim
    for _ in range(layers):
        modules.extend([
            nn.Linear(in_dim, hidden_dim),
            nn.BatchNorm1d(hidden_dim),
            activ,
            nn.Dropout(dropout)
        ])
        in_dim = hidden_dim
    modules.append(nn.Linear(hidden_dim, 1))
    modules.append(nn.Sigmoid())
    return nn.Sequential(*modules)

# Sweep
def train(config):
    wandb.init(config=config)
    config = wandb.config

    model = build_model(
        input_dim=X_train.shape[1],
        layers=config.layers,
        hidden_dim=config.hidden_dim,
        dropout=config.dropout,
        activation=config.activation
    )

    criterion = nn.MSELoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=config.lr, weight_decay=config.weight_decay)

    X_train_tensor = torch.tensor(X_train, dtype=torch.float32)
    y_train_tensor = torch.tensor(y_train.reshape(-1, 1), dtype=torch.float32)
    X_val_tensor = torch.tensor(X_val, dtype=torch.float32)
    y_val_tensor = torch.tensor(y_val.reshape(-1, 1), dtype=torch.float32)
    X_test_tensor = torch.tensor(X_test, dtype=torch.float32)

    best_val_loss = float("inf")
    patience = 170 # igual que epocas para comparar los tiempos de ejecución
    counter = 0
    epochs = 170

    start_time = time.time()

    for epoch in range(epochs):
        model.train()
        optimizer.zero_grad()
        y_pred_train = model(X_train_tensor)
        loss_train = criterion(y_pred_train, y_train_tensor)
        loss_train.backward()
        optimizer.step()

        model.eval()
        with torch.no_grad():
            y_pred_val = model(X_val_tensor)
            loss_val = criterion(y_pred_val, y_val_tensor)

        wandb.log({
            "epoch": epoch + 1,
            "train_loss": loss_train.item(),
            "val_loss": loss_val.item()
        })

        if loss_val.item() < best_val_loss:
            best_val_loss = loss_val.item()
            best_model_state = model.state_dict()
            counter = 0
        else:
            counter += 1
            if counter >= patience:
                break

    elapsed = time.time() - start_time

    # Evaluación
    model.load_state_dict(best_model_state)
    model.eval()
    with torch.no_grad():
        y_pred_norm = model(X_test_tensor).numpy().flatten()

    y_pred_logBCF = y_pred_norm * (logBCF_max - logBCF_min) + logBCF_min
    mse = mean_squared_error(y_test_true, y_pred_logBCF)
    r2 = r2_score(y_test_true, y_pred_logBCF)

    wandb.log({"test_mse": mse, "test_r2": r2, "train_time_sec": elapsed})
    wandb.finish()

# Argumentos CLI para ejecución directa
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--activation", type=str, default="silu")
    parser.add_argument("--dropout", type=float, default=0.2)
    parser.add_argument("--hidden_dim", type=int, default=64)
    parser.add_argument("--layers", type=int, default=2)
    parser.add_argument("--lr", type=float, default=0.001)
    parser.add_argument("--weight_decay", type=float, default=0.001)
    args = parser.parse_args()

    config_dict = vars(args)
    train(config_dict)
