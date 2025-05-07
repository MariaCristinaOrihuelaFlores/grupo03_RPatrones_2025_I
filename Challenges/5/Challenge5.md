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

