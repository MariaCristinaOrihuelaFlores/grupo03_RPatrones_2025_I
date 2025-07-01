# Grupo 03 - Reconocimiento de Patrones

- Repositorio del Grupo 3 del curso de Reconocimiento de Patrones 2025-1

## Presentación del equipo
| Foto  | Descripción |
|-------|------------|
|<div align="center"><image src="https://github.com/MariaCristinaOrihuelaFlores/grupo03_RPatrones_2025_I/blob/main/Challenges/Integrantes/20202517_ORIHUELA_FLORES_MARIA_CRISTINA (1).png" width="200px" height="270px">| **Cristina Orihuela**<br>cristina.orihuela@upch.pe<br> <p align="justify"> Estudiante entusiasta de Ingeniería Biomédica de 10mo con interés en la innovación tecnológica aplicada a la salud. Comprometida con el trabajo en equipo y la mejora continua de sus habilidades técnicas y científicas.</p>|
|<div align="center"><image src="https://github.com/MariaCristinaOrihuelaFlores/grupo03_RPatrones_2025_I/blob/main/Challenges/Integrantes/Firefly 20250120222401.png" width="200px" height="270px">| **Gabriel Sanchez**<br>gabriel.marcos@upch.pe<br> <p align="justify"> Estudiante de 9no Ciclo con experiencia en el desarrollo de soluciones tecnológicas innovadoras para desafíos emergentes mediante investigación científica y en el área de Ingenieria Clínica. Poseo habilidades analíticas avanzadas y una sólida formación en software de análisis, visualización y procesado de datos. Motivado por seguir aprendiendo nuevas tecnologías  e integrarlas en el desarrollo de proyectos con un impacto positivo en el sector salud </p>|
|![Figureteando](https://github.com/user-attachments/assets/27cb749f-98c4-410e-8bc6-8e3e4aba4c83)| **Rodrigo Gonzales**<br>rodrigo.gonzales@upch.pe<br> <p align="justify"> Estudiante de Ingeniería Biomédica de 9no ciclo orientado a la investigación y al desarrollo de soluciones tecnológicas para el sector salud. Interesado en aplicar sus conocimientos en proyectos con impacto real en la sociedad. </p>|

# Mejora de la segmentación en ecografías abdominales mediante adaptación de dominio con CycleGAN y U-Net

## Descripción del proyecto

### Problemática
La ecografía (US) es una herramienta diagnóstica clave por su bajo costo y no invasividad, pero sus imágenes presentan artefactos (ruido *speckle*, sombras) y alta variabilidad operador-dependiente, dificultando el desarrollo de algoritmos robustos de segmentación automática. Los simuladores basados en proyección de rayos generan datos sintéticos con máscaras precisas, pero su falta de realismo (*domain gap*) limita la transferencia a entornos clínicos reales.

### Objetivos
1. Reducir el *domain shift* entre imágenes simuladas y reales mediante **CycleGAN**, preservando estructuras anatómicas clave
2. Entrenar una **U-Net** con imágenes adaptadas para segmentación multiclase (hígado, riñón, vasos, etc.) en ecografías abdominales reales
3. Validar el *pipeline* integrado como herramienta para aplicaciones clínicas y educativas en entornos con datos reales limitados

## Metodología clave

- **Dataset**: 
  - 617 imágenes reales (ecografías de 11 pacientes) 
  - 926 simuladas (*USSimAndSegm*)
  
- **CycleGAN**:
  - Entrenado con pérdidas adversariales
  - Pérdidas de ciclo (λ=10) e identidad (λ=0.5)
  - Transforma simulaciones a dominio realista

- **U-Net**:
  - Arquitectura simétrica 2D (4 niveles)
  - Entrenada con *Dice loss* + *cross-entropy*
  - Utiliza imágenes adaptadas por CycleGAN

- **Métricas**:
  - *Realismo*: 
    - SSIM = 0.2928
    - PSNR = 15.38 dB 
    - LNCC = 0.3827
  - *Segmentación*: 
    - Dice = 0.5782
    - IoU = 0.5153 (en datos reales)

## Resultados destacados

✔ Reducción del *domain shift* confirmada por análisis **t-SNE** (mayor solapamiento entre dominios)  
✔ Segmentación viable en estructuras predominantes (hígado/riñón)  
✔ Limitaciones en clases minoritarias (vesícula)  

**Limitaciones identificadas**:
- Dataset pequeño (600 imágenes reales vs. ideal >2000)
- Solo incluye órganos sanos (se requiere patologías para generalización clínica)

## Impacto y futuro

El *pipeline* demuestra que la **adaptación de dominio con GANs** es prometedora para ecografía, especialmente en entornos con escasez de datos anotados. 

**Futuras mejoras**:
- Aumentar el dataset con casos patológicos
- Explorar arquitecturas más avanzadas (pérdidas perceptuales, Transformers)
- Optimizar la segmentación de clases minoritarias
