Inferencia y
Estimación
Trabajo Práctico 1

Trabajo Práctico 1
Aplicando PCA a las entradas, es posible reducir la dimensión conservando la
información más relevante que permita distinguir varias categorías (clases).
Clasificador
Normal
Normal
PCA
Neumonía
Neumonía
k < m
Menor dimensión
en las entradas del
clasificador

Trabajo Práctico 1 – Objetivos
Ejercicio 1
● Evaluar la clasificación sin PCA.
● Evaluar la clasificación con PCA variando la cantidad de componentes (K).
Ejercicio 2
● Perturbar las imágenes de prueba con probabilidad p y visualizar con
Utilizamos PCA para representación diferentes clases de imágenes en una
scatter de las K=2 componentes principales de los datos.
menor dimensión y cómo se comporta en la clasificación.
● Aplicar Monte Carlo para evaluar cuánto se degrada la información en
función de perturbaciones en las imágenes de prueba.
Ejercicio 3
● Justificar el uso de Monte Carlo aplicado al cálculo de probabilidades.

Dataset

Trabajo Práctico 1 – Dataset
dataset_tp1
train
Utilizamos PCA para representación diferentes clases de imágenes en una test
menor dimensión y cómo se comporta en la clasificación.
train_labels.csv
test_labels.csv

Trabajo Práctico 1 – Dataset
dataset_tp1
PMINST_0001.png
PMINST_0002.png
train
PMINST_0003.png
…
PMINST_2428.png
Utilizamos PCA para representación diferentes clases de imágenes en una test
menor dimensión y cómo se comporta en la clasificación.
train_labels.csv
test_labels.csv

Trabajo Práctico 1 – Dataset
dataset_tp1
train
PMINST_2429.png
PMINST_2430.png
Utilizamos PCA para representación diferentes clases de imágenes en una test
PMINST_2431.png
menor dimensión y cómo se comporta en la clasificación.
…
PMINST_2896.png
train_labels.csv
test_labels.csv

Trabajo Práctico 1 – Dataset
dataset_tp1
train
Utilizamos PCA para representación diferentes clases de imágenes en una test
menor dimensión y cómo se comporta en la clasificación.
train_labels.csv
test_labels.csv

Trabajo Práctico 1 – Dataset
dataset_tp1
train
Utilizamos PCA para representación diferentes clases de imágenes en una test
menor dimensión y cómo se comporta en la clasificación.
train_labels.csv
test_labels.csv

Trabajo Práctico 1
Ajuste del modelo PCA
train
Estimar covarianza
Matriz de
o matrices SVD proyección P
Ajustar
modelo
PCA

Trabajo Práctico 1
Entrenamiento del clasificador sin PCA
train
Entrenar Modelo
clasificador entrenado
train_labels.csv

Trabajo Práctico 1
Entrenamiento del clasificador con PCA
train P, K P: matriz de componentes principales
K: tamaño final de la proyección
Entrenar Modelo
PCA
clasificador entrenado
train_labels.csv

Trabajo Práctico 1
Clasificación sin PCA
test Modelo
entrenado
Clasificador
Total de aciertos
Total de datos
Comparación Accuracy
test_labels.csv

Trabajo Práctico 1
Clasificación con PCA
| test | P, K | Modelo  |
| ---- | ---- | ------- |
entrenado
|     | PCA | Clasificador |
| --- | --- | ------------ |
Total de aciertos
Total de datos
Accuracy
Comparación
test_labels.csv

Resultados a
presentar

Trabajo Práctico 1 – Ejercicio 1
K
ycaruccA
test
K
PCA +
Accuracy
Clasificación curva
test_labels.csv

Trabajo Práctico 1 – Ejercicio 2
P, K
p
Girar 180°
test
PCA
1–p
p
|     | ● Normal    |     | ● Normal    |     |     | ● Normal    |
| --- | ----------- | --- | ----------- | --- | --- | ----------- |
|     | ● Neumonía  |     | ● Neumonía  |     |     | ● Neumonía  |
| Y   |             | Y   |             |     | Y   |             |
| 2   |             | 2   |             |     | 2   |             |
|     | scatter     |     | scatter     | …   |     | scatter     |
|     | Y           |     | Y           |     |     | Y           |
|     | 1           |     | 1           |     |     | 1           |

Trabajo Práctico 1 – Ejercicio 2
Simulaciones Monte Carlo (con perturbación de las imágenes)
Girar 180°
PCA + Accuracy
test
Clasificación i = 1
p
Girar 180°
PCA + Accuracy
Clasificación i = 2
1–p
Girar 180°
PCA + Accuracy
Clasificación i = N
MC
…
…
p
1–p
test
p
test
1–p
N
senoicazilaeR
CM
● Imagen original
● Imagen perturbada

Trabajo Práctico 1 – Ejercicio 2
En cada realización Monte Carlo obtenemos un accuracy. Para cuantificar cuánto se
degrada esta métrica en función de la probabilidad de perturbación de las imagenees
(p), podemos definir la pérdida del accuracy:
L(p) = A – A
0 p
Donde:
A : es el accuracy base (nuestra referencia) obtenido con el conjunto de test con todas
0
las imágenes originales (sin perturbaciones).
A : es el accuracy obtenido con el grupo de test para cada realización Monte Carlo,
p
donde algunas imágenes se procesaran giradas (con probabilidad p) o al derecho (con
probabilidad 1–p).

Trabajo Práctico 1 – Ejercicio 2
Con Monte Carlo buscamos estimar las siguientes cantidades:
● Accuracy promedio
● Probabilidad de que la pérdida supere el umbral 𝛿 = 0.1.
● Histograma del accuracy.

Trabajo Práctico 1 – Ejercicio 2
p
ycaruccA oidemorp
curva
p
)𝛿>L(P
Accuracy
curva
aicneucerF
◼ Histograma
-- Accuracy base
histograma
Accuracy
aicneucerF
p
◼ Histograma
-- Accuracy base
histograma
…

Trabajo Práctico 1 – Ejercicio 3
En la tercer parte se pide justificar desde la teoría, la validez de la
metodología utilizada por medio de Monte Carlo.

Actividades

Trabajo Práctico 1 – Actividad 1
Escriba un programa que complete los siguientes pasos:
1. Levantar las imágenes del conjunto de train y entrenar el modelo
de clasificación de regresión logística.
2. Levantar las imágenes del conjunto de test y realizar la predicción
de clase para cada imagen de entrada, calculando el accuracy con
el total de imágenes de prueba.

Trabajo Práctico 1 – Actividad 2
Escriba un programa que complete los siguientes pasos:
1. Levantar las imágenes del conjunto de train y entregar el modelo
PCA para obtener la matriz de componentes principales (utilice la
descomposición SVD).
2. Levantar las imágenes del conjunto de test para transformarlas al
espacio PCA con K=2. Visualizar scatter de ambas componentes.
3. Luego realice la predicción de clase utilizando como entradas a los
vectores reducidos con PCA.

Trabajo Práctico 1 – Actividad 3
Pensar un pseudocódigo que resuelva la lógica del Ejercicio 1 y otro para
el Ejercicio 2.
