# Conceptos clave en SVM: C, Kernel y Gamma

## 🎛️ Hiperparámetro `C` en SVM

### 🧩 ¿Qué es `C`?

`C` es el **parámetro de regularización** en el algoritmo SVM.  
Determina **cuánto penalizamos los errores** cometidos al clasificar los datos de entrenamiento.

---

### 📐 Intuición geométrica

El objetivo del SVM es encontrar un **hiperplano con el mayor margen** que separe las clases, pero a veces no se puede separar perfectamente sin cometer errores.

- `C` controla el **equilibrio entre el margen ancho y la clasificación correcta** de cada punto de entrenamiento.

---

### 🔁 ¿Qué pasa al modificar `C`?

| Valor de `C` | Comportamiento del modelo                                   | Riesgo            |
|--------------|-------------------------------------------------------------|-------------------|
| 🔹 **C bajo**  | Acepta más errores. Busca un margen amplio.                | ➖ Underfitting    |
| 🔸 **C alto**  | Penaliza fuertemente los errores. Intenta clasificar todo bien. | ➕ Overfitting     |

---

### 🎯 Analogía simple

Imagina que entrenas a un robot que debe separar pelotas rojas y azules con una regla:

- Si le das un **C bajo**, le dices: *"No importa si te equivocas un poco, pero asegúrate de hacer una separación simple"*.
- Si le das un **C alto**, le dices: *"¡Prohibido equivocarse! Clasifica TODO bien aunque tengas que hacer una frontera rara o enredada"*.

---

### 📊 Visualización conceptual

> Aquí podrías incluir una imagen con dos subgráficos que comparen:

1. **C = 0.1**: Margen amplio, acepta algunos errores.
2. **C = 100**: Margen estrecho, ajusta demasiado al conjunto de entrenamiento.

---


## 🌐 ¿Qué es el Kernel?

El **kernel** es una función que permite que un modelo SVM (Support Vector Machine) **proyecte los datos a un espacio de mayor dimensión** para encontrar una frontera de separación más clara entre clases, incluso cuando no es posible separarlas linealmente en su espacio original.

### 🎯 ¿Para qué sirve el kernel?
- Transforma los datos para que **sí puedan separarse con una línea recta (hiperplano)**.
- Permite capturar **relaciones no lineales** entre los datos.
- Evita que el modelo tenga que hacer cálculos complejos en espacios de muchas dimensiones (gracias al "truco del kernel").

### 🧪 Tipos comunes de kernel:
| Kernel        | Características                                | Ideal para...                              |
|---------------|-------------------------------------------------|---------------------------------------------|
| `linear`      | Separación lineal directa                       | Datos que ya son linealmente separables     |
| `poly`        | Usa polinomios de grado n                      | Relaciones más complejas                   |
| `rbf`         | Función gaussiana (Radial Basis Function)       | Fronteras suaves y no lineales              |
| `sigmoid`     | Similar a redes neuronales                      | Usado en ciertos contextos específicos      |

---

## ⚙️ ¿Qué es Gamma (`γ`)?

`gamma` es un **hiperparámetro** que se utiliza en los **kernels no lineales**, como `rbf`, `poly` o `sigmoid`. Controla **cuánto influye cada punto de entrenamiento** sobre la forma de la frontera de decisión del modelo.

### 🧠 Intuición:
> `gamma` define el **alcance de la memoria** de cada punto.  
> ¿Ve solo su cuadra o ve toda la ciudad?

### 🔍 ¿Cómo afecta el valor de gamma?

| Valor de `gamma` | Comportamiento del modelo                    | Posible problema      |
|------------------|-----------------------------------------------|------------------------|
| Bajo (`↓`)       | Cada punto influye en una **zona amplia**     | Underfitting           |
| Medio (óptimo)   | Frontera curva y **bien ajustada**            | Buen rendimiento       |
| Alto (`↑`)       | Cada punto solo influye en su **vecindad**    | Overfitting            |

### 📌 Recomendaciones prácticas:
- `gamma` solo aplica a kernels **no lineales**.
- Para un buen modelo, debe ajustarse junto con otros hiperparámetros (como `C`).
- Una gamma muy alta puede hacer que el modelo aprenda **ruido o detalles irrelevantes**.

---

## 🧪 Comparación gráfica (imaginaria)

![image](https://github.com/user-attachments/assets/243327d8-f256-4992-bfd5-f71ec4ec6533)

🔍 Explicación del gráfico:

Gamma bajo (0.01):
La frontera es muy suave, generaliza demasiado → underfitting.

Gamma medio (1):
La frontera se ajusta bien a los datos → buen ajuste.

Gamma alto (100):
La frontera es muy irregular y compleja → overfitting (el modelo memoriza el ruido).
