### Análisis de CSV

Vemos que tenemos el SMILE y varios descriptores moleculares de diferentes moléculas, vamos a en una tabla identificar cada uno de estos.


| **Columna**                   | **Tipo**  | **Significado**                                                                                   |
|------------------------------|-----------|----------------------------------------------------------------------------------------------------|
| `Molecular_Weight`           | Numérico  | Peso molecular total en Daltons (g/mol), incluye todos los átomos.                                |
| `Polar_Area`                 | Numérico  | Área polar superficial (TPSA), relacionada con solubilidad y permeabilidad.                       |
| `Complexity`                 | Numérico  | Medida de la complejidad estructural de la molécula (ramificación, ciclos, estereocentros, etc.). |
| `XLogP`                      | Numérico  | Logaritmo del coeficiente de partición octanol/agua. Mide lipofilicidad.                          |
| `Heavy_Atom_Count`           | Numérico  | Número de átomos pesados (no H).                                                                  |
| `H-Bond_Donor_Count`         | Numérico  | Número de átomos capaces de donar un enlace de hidrógeno (como OH o NH).                          |
| `H-Bond_Acceptor_Count`      | Numérico  | Número de átomos capaces de aceptar un enlace de hidrógeno (como O, N con pares libres).          |
| `Rotatable_Bond_Count`       | Numérico  | Número de enlaces simples no rígidos. Relacionado con la flexibilidad molecular.                  |
| `Exact_Mass`                 | Numérico  | Masa exacta calculada con isótopos más abundantes (alta precisión).                               |
| `Monoisotopic_Mass`          | Numérico  | Igual que `Exact_Mass`, suele usarse en espectrometría de masas.                                  |
| `Charge`                     | Numérico  | Carga neta formal de la molécula.                                                                 |
| `Covalent_Unit_Count`        | Numérico  | Número de fragmentos moleculares conectados covalentemente (por ej., sales).                      |
| `Isotopic_Atom_Count`        | Numérico  | Número de átomos con isótopos específicos (no comunes).                                           |
| `Total_Atom_Stereo_Count`    | Numérico  | Total de centros estereogénicos en átomos (quiralidad).                                           |
| `Defined_Atom_Stereo_Count`  | Numérico  | Cuántos estereocentros están definidos.                                                           |
| `Undefined_Atom_Stereo_Count`| Numérico  | Cuántos estereocentros están indefinidos.                                                         |
| `Total_Bond_Stereo_Count`    | Numérico  | Número de estereoisomerismos tipo E/Z (dobles enlaces).                                           |
| `Defined_Bond_Stereo_Count`  | Numérico  | Cuántos están definidos como E o Z.                                                               |
| `Undefined_Bond_Stereo_Count`| Numérico  | Cuántos no tienen definida la geometría (E/Z).                                                    |

De la tabla vamos a seleccionar tres **descriptores moleculares** particularmente importantes para una interpretación futura con aplicaciones tecnológicas, científicas o farmacológicas:

1. **`Polar_Area` (Área Polar Superficial)**: Es crucial porque influye directamente en la **permeabilidad celular** y la **absorción oral** de una molécula, lo cual es vital para evaluar su viabilidad como fármaco o compuesto bioactivo.

2. **`XLogP`**: Mide la **lipofilicidad** de una molécula, un factor determinante en su capacidad para atravesar membranas biológicas. Es clave en el diseño de fármacos, donde el balance entre solubilidad en agua y en lípidos puede definir la eficacia de un compuesto.

3. **`H-Bond_Donor_Count` y `H-Bond_Acceptor_Count`**: (cuentan como uno por su relación directa) son esenciales porque determinan la **capacidad de interacción mediante enlaces de hidrógeno**, algo fundamental para la **afinidad y especificidad de unión a blancos moleculares** como proteínas o ADN.


### 🔬 Análisis de los Descriptores Moleculares Clave

Con base en los valores observados en la tabla (`Polar_Area`, `XLogP`, `H-Bond_Donor_Count` y `H-Bond_Acceptor_Count`), se pueden extraer las siguientes conclusiones:

---

#### **1. Polar Area (TPSA)**
- Los valores oscilan aproximadamente entre **70.6** y **489.0**, indicando una **amplia diversidad en la polaridad superficial**.
- **Valores bajos (< 90 Å²)**: Alta permeabilidad celular y buena absorción oral. Candidatos ideales para administración oral.
- **Valores altos (> 140 Å²)**: Baja permeabilidad, pero potencialmente útiles para **interacciones extracelulares** o inhibidores de superficie.

---

#### **2. XLogP**
- Rango observado: de **−4.5** hasta **+4.7**, lo que indica una mezcla de compuestos **hidrofílicos y lipofílicos**.
- **Valores negativos**: Mayor solubilidad acuosa; útiles para compuestos que actúan en medios biológicos acuosos.
- **Valores positivos (> 2)**: Alta lipofilicidad; favorecen el paso a través de membranas celulares, aunque pueden comprometer solubilidad.

---

#### **3. H-Bond Donor / Acceptor Count**
- **Donadores de H**: Entre **0 y 13**
- **Aceptores de H**: Entre **2 y 15**
- Un mayor número sugiere **alta capacidad de interacción molecular** mediante enlaces de hidrógeno, importante en la **afinidad y especificidad con blancos como proteínas o ADN**.
- Sin embargo, muchos enlaces de hidrógeno también pueden disminuir la permeabilidad.

---

### 📌 Conclusión General
La diversidad en estos tres descriptores clave indica que la biblioteca molecular está bien equilibrada para abordar distintas **rutas de administración**, **afinidades biológicas** y **usos farmacológicos o tecnológicos**. Se pueden identificar tanto moléculas con buen perfil de absorción oral como otras más aptas para **aplicaciones extracelulares o biotecnológicas**.

