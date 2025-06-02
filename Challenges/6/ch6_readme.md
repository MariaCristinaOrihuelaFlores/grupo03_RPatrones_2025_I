# QSAR Bioconcentration - Regresión y Clasificación con Redes Neuronales

Para el Challenge 6 se presenta una implementación de modelos de redes neuronales aplicados al dataset de QSAR Bioconcentration para resolver dos tareas: **regresión del log BCF (bioconcentration factor)** y **clasificación del mecanismo de bioconcentración**.

---

## Descripción del problema

El bioconcentration factor (BCF) es una medida clave para estimar la capacidad de una sustancia química para acumularse en organismos acuáticos. Predecir este valor es importante para evaluar riesgos ambientales.

En este estudio se abordan dos objetivos:

- **Tarea de regresión:** predecir el valor continuo de log(BCF).
- **Tarea de clasificación:** categorizar cada sustancia en tres clases discretas según su mecanismo de bioconcentración:
  - Clase 0: almacenamiento lipídico predominante.
  - Clase 1: almacenamiento en sitios adicionales (e.g., proteínas).
  - Clase 2: metabolización o eliminación activa.

---

## Dataset

Se utiliza el dataset publicado por Grisoni et al. (2016), disponible en Kaggle:  
🔗 [QSAR Bioconcentration Dataset](https://www.kaggle.com/datasets/rajgupta2019/qsar-bioconcentration-classes-dataset/)

- **Número de muestras:** 779 compuestos químicos.
- **Columnas de entrada:** 9 descriptores moleculares numéricos.
- **Columnas clave:**
  - `logBCF`: valor continuo de log bioconcentration factor (regresión).
  - `Class`: clase objetivo (0, 1 o 2) para la clasificación.
  - `Set`: partición del dataset (`Train` o `Test`).

---

## Estructura de archivos

| Archivo | Descripción |
|--------|-------------|
| `Grisoni_et_al_2016_EnvInt88.csv` | Dataset curado con descriptores moleculares, logBCF y etiquetas de clase. |
| `ch6_regression.ipynb` | Notebook con el modelo base y evaluación para la tarea de regresión. |
| `ch6_classification.ipynb` | Notebook con el modelo base y evaluación para la tarea de clasificación. |
| `train_regression.py` | Script para lanzar entrenamientos y sweeps (regresión). |
| `train_classification.py` | Script para lanzar entrenamientos y sweeps (clasificación). |
| `wandb_sweep_config_regression.yaml` | Configuración del grid search para la regresión usando Weights & Biases. |
| `wandb_sweep_config_classification.yaml` | Configuración del grid search para la clasificación usando Weights & Biases. |
---

##  Referencias

Grisoni, F., Cassotti, M., Todeschini, R., & Benfenati, E. (2016). Reshaped k-nearest neighbor QSAR algorithm: optimizing the predictive performance of the k-nearest neighbor algorithm in QSAR. *Journal of chemical information and modeling*, 56(12), 2307–2312.

---
