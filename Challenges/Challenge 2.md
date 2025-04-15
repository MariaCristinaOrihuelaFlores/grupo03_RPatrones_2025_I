# Grupo 03 - Reconocimiento de Patrones
# 1. Introducción

La lucha contra el cáncer sigue siendo uno de los retos más significativos en el ámbito de la salud global, afectando a 20 millones de personas en todo el mundo. La reactivación de la muerte celular inducida por la acumulación de peróxidos lipídicos dependientes del hierro (ferroptosis) es un mecanismo potencial para el tratamiento del cáncer.

Esto se debe a un principio químico, que nos da el indicio de que podemos usarla para destruir células cancerígenas. El principio comienza con el metabolismo normal de una persona, especialmente en procesos inflamatorios o en presencia de ciertas enzimas, se pueden crear peróxidos de hidrógeno (H₂O₂). Esta molécula reacciona con el hierro en su estado ferroso y se producirá una reacción llamada **Fentón**.

Esto nos generará un radical hidroxilo, el cuál será altamente oxidante y tenderá a reaccionar en este caso con un lípido en el medio generando un radical lipídico.

En la reacción, el lípido a ser atacado se representa como **RH** y luego de la oxidación, quedará con un radical libre. Posteriormente, este lípido con el radical libre procederá a reaccionar con oxígeno y formará el **peróxido lipídico**, cuya acumulación está relacionada con la ferroptosis, el tipo de muerte celular programada que nos ayudará a combatir el cáncer.

Como curiosidad adicional, este lípido con su radical libre podrá oxidar a otros lípidos, aumentando aún más la cantidad de peróxidos lipídicos.

Una vía para desencadenar la ferroptosis implica la **inactivación de la proteína peroxidasa dependiente del glutatión (GPx4)**. La identificación de moléculas que pueden inducir ferroptosis a través de la inhibición de GPx4 es crucial para el desarrollo de nuevas terapias anticancerígenas.

En este sentido, los **catecoles** han demostrado ser candidatos interesantes debido a su alta afinidad por el hierro, lo que les permite formar **complejos estables** (provocando la acumulación de hierro Fe³⁺ en la sangre). Esto, si bien no es el hierro Fe²⁺ utilizado directamente para generar radicales hidroxilo, por el principio de Le Châtelier, **la reacción de Fe²⁺ hacia Fe³⁺ tenderá a ir hacia la izquierda**, aumentando la concentración de Fe²⁺ en la sangre y **favoreciendo directamente la ferroptosis**.

Con el objetivo de acelerar la identificación de estos compuestos en bases de datos moleculares, este trabajo presenta un **modelo predictivo basado en redes neuronales artificiales (ANN)** para identificar moléculas con afinidad por el sitio activo de GPx4. Utilizando una base de datos de productos naturales de Perú (Perú NPDB), se realizó un análisis a partir de 83 catecoles y se generaron 1,024 descriptores moleculares.

Adicionalmente, se aplicó la técnica de **eliminación recursiva de características (RFE)** para refinar el modelo y mejorar su precisión, reduciendo de 1,024 descriptores a 131 atributos (descriptores moleculares) y optimizando el rendimiento del modelo de red neuronal artificial (ANN).

---

# 2. Objetivos

Desarrollar un modelo predictivo basado en redes neuronales artificiales (ANN) para identificar compuestos, específicamente catecoles, con afinidad por el sitio activo de la proteína GPx4, con el fin de promover la **inducción de ferroptosis** como estrategia potencial en el tratamiento del cáncer.
