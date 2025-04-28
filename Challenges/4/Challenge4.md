Un Random Forest (Bosque Aleatorio) es un conjunto de árboles de decisión que trabajan juntos para hacer predicciones. 

# Entendiendo la intuición detrás del algoritmo Random Forest

El algoritmo Random Forest es una técnica poderosa de aprendizaje basada en árboles en Machine Learning que se utiliza para hacer predicciones, y luego se realiza una votación entre todos los árboles para determinar la predicción final. Son ampliamente utilizados en tareas de clasificación y regresión [1].

#### Ejemplo práctico:

Imagina que pides consejo a un grupo de amigos sobre a dónde ir de vacaciones. Cada amigo te da su recomendación basada en su perspectiva y preferencias únicas (es decir, cada árbol de decisión entrenado en diferentes subconjuntos de datos). Luego, tomas tu decisión final considerando la opinión de la mayoría o promediando sus sugerencias (predicción en conjunto).

![image](https://github.com/user-attachments/assets/4758d448-10d9-4257-a676-d37b509c38d5)

En la imagen podemos ver que: el proceso comienza con un conjunto de datos que contiene filas y sus correspondientes etiquetas de clase (columnas).

### ¿Cómo funciona el algoritmo de Random Forest?

El algoritmo de Random Forest funciona en varios pasos:

Paso 1) Random Forest construye múltiples árboles de decisión utilizando muestras aleatorias de los datos. Cada árbol se entrena con un subconjunto diferente de los datos, lo que hace que cada árbol sea único.

Paso 2) Al crear cada árbol, el algoritmo selecciona aleatoriamente un subconjunto de características o variables para dividir los datos, en lugar de usar todas las características disponibles al mismo tiempo. Esto añade diversidad a los árboles.

Paso 3) Cada árbol de decisión en el bosque realiza una predicción basada en los datos con los que fue entrenado. Al hacer la predicción final, Random Forest combina los resultados de todos los árboles.

Paso 4) Para tareas de clasificación, la predicción final se decide mediante votación por mayoría. Esto significa que la categoría predicha por la mayoría de los árboles será la predicción final.

Paso 5) Para tareas de regresión, la predicción final es el promedio de las predicciones de todos los árboles.

Paso 6) La aleatoriedad en la selección de muestras de datos y características ayuda a prevenir el sobreajuste (overfitting), haciendo que las predicciones sean más precisas y confiables.

Otro punto clave que nos ayudará a entender bien, como funciona el Random Forest son los supuestos, las ventajas y limitaciones del modelo [1].

## Supuestos del Random Forest

- Cada árbol toma sus propias decisiones: Cada árbol en el bosque hace sus propias predicciones de manera independiente, sin depender de los demás.

- Se usan partes aleatorias de los datos: Cada árbol se construye utilizando muestras y características aleatorias para reducir errores.

- Se necesita suficiente cantidad de datos: Tener suficientes datos asegura que los árboles sean diferentes entre sí y aprendan patrones variados.

- Predicciones diferentes mejoran la precisión: Combinar las predicciones de distintos árboles lleva a obtener un resultado final más preciso [1].

## Ventajas del Random Forest

- Random Forest proporciona predicciones muy precisas incluso con conjuntos de datos grandes.

- Puede manejar bien los datos faltantes sin comprometer la precisión.

- No requiere normalización ni estandarización del conjunto de datos.

- Al combinar múltiples árboles de decisión, se reduce el riesgo de sobreajuste del modelo [1].

## Limitaciones del Random Forest

- Puede ser computacionalmente costoso, especialmente cuando se utilizan muchos árboles.

- Es más difícil de interpretar en comparación con modelos más simples como los árboles de decisión [1].

## Discusión

Random Forest es básicamente un conjunto de árboles de decisión que trabajan juntos para hacer una predicción más robusta. Cada árbol se entrena con una parte diferente de los datos y, al final, la decisión final se toma como un "voto" entre todos los árboles. Esto ayuda mucho a evitar el sobreajuste y a mejorar la precisión, como vimos en clase y en la teoría [1].

Ahora, viendo los resultados de nuestro experimento:

Cuando variamos el criterio de pureza, gini dio el mejor accuracy (0.9704) comparado con entropy y log_loss. Esto tiene sentido porque gini suele ser más rápido de calcular y es más eficiente en conjuntos de datos grandes como MNIST.

Sobre el número de estimadores, notamos que conforme aumentábamos la cantidad de árboles, el accuracy también subía. Por ejemplo, con 10 árboles apenas llegamos a 0.9492, pero con 1000 árboles subimos hasta 0.9725. Sin embargo, también vimos que el tiempo de entrenamiento creció bastante.
Por eso, 500 árboles nos pareció el mejor punto de equilibrio: el accuracy era alto (0.9712) y el costo computacional no era tan exagerado. A partir de 500, el aumento en accuracy ya era muy pequeño, pero el tiempo de entrenamiento sí que aumentaba un montón.

En cuanto a la profundidad máxima de los árboles, al usar una profundidad baja como 5, el accuracy cayó bastante (0.8673). A medida que aumentábamos la profundidad, el accuracy subía, llegando a 0.9714 con profundidad 30. Curiosamente, vimos que profundidad 30 dio mejor resultado que dejar los árboles sin límite de profundidad (None), donde el accuracy fue 0.9712. Esto sugiere que en este caso, poner un límite de profundidad ayuda a mejorar el rendimiento y a evitar overfitting.

Finalmente, comparado con otros modelos como SVM, notamos que Random Forest entrenó mucho más rápido. Con SVM, los entrenamientos eran bastante pesados para este tamaño de dataset (MNIST), mientras que Random Forest, aunque tarda más a medida que suben los árboles, sigue siendo mucho más ágil en general.

## Referencias

[1] geeksforgeeks. “Random Forest Algorithm in Machine Learning - GeeksforGeeks”. GeeksforGeeks. Accedido el 28 de abril de 2025. [En línea]. Disponible: https://www.geeksforgeeks.org/random-forest-algorithm-in-machine-learning/?utm_source=chatgpt.com
