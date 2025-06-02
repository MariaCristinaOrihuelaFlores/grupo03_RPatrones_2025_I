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

Se utiliza el dataset publicado por Grisoni et al., disponible en el repositorio de la UCI:  
🔗 https://archive.ics.uci.edu/dataset/510/qsar+bioconcentration+classes+dataset

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
| [`Grisoni_et_al_2016_EnvInt88.csv`](./Grisoni_et_al_2016_EnvInt88.csv) | Dataset curado con descriptores moleculares, logBCF y etiquetas de clase. |
| [`ch6_regression.ipynb`](./ch6_regression.ipynb) | Notebook con el modelo base y evaluación para la tarea de regresión. |
| [`ch6_classification.ipynb`](./ch6_classification.ipynb) | Notebook con el modelo base y evaluación para la tarea de clasificación. |
| [`train_regression.py`](./train_regression.py) | Script para lanzar entrenamientos y sweeps (regresión). |
| [`train_classification.py`](./train_classification.py) | Script para lanzar entrenamientos y sweeps (clasificación). |
| [`wandb_sweep_config_regression.yaml`](./wandb_sweep_config_regression.yaml) | Configuración del grid search para la regresión usando Weights & Biases. |
| [`wandb_sweep_config_classification.yaml`](./wandb_sweep_config_classification.yaml) | Configuración del grid search para la clasificación usando Weights & Biases. |

---

## Referencias

- QSAR Bioconcentration classes dataset [Dataset]. (2019). UCI Machine Learning Repository. https://doi.org/10.24432/C56S46  
- Grisoni, F., Consonni, V., Vighi, M., Villa, S., & Todeschini, R. (2016). Expert QSAR system for predicting the bioconcentration factor under the REACH regulation. *Environmental Research*, 151, 478–487.  
[https://doi.org/10.1016/j.envres.2016.04.032](https://doi.org/10.1016/j.envres.2016.04.032)
