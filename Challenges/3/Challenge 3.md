# Conceptos clave en SVM: Kernel y Gamma

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


