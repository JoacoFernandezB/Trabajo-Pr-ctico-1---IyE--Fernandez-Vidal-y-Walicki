|          |     |             | Trabajo |     | Práctico    |     | N.°          | 1   |          |
| -------- | --- | ----------- | ------- | --- | ----------- | --- | ------------ | --- | -------- |
| Análisis | de  | Componentes |         |     | Principales |     | y Simulación |     | de Monte |
Carlo
|     |     | Cristian | Walicki |     | de los | Santos | — Legajo: | 370838 |     |
| --- | --- | -------- | ------- | --- | ------ | ------ | --------- | ------ | --- |
Joaquin Fernandez Beschtedt — Legajo: 370841 Tomas Vidal — Legajo: 370826
|     |     |            |     | Universidad  |     | de San | Andrés    |      |     |
| --- | --- | ---------- | --- | ------------ | --- | ------ | --------- | ---- | --- |
|     |     | Inferencia |     | y Estimación |     | —      | Primavera | 2026 |     |
Resumen
Este trabajo aplica Análisis de Componentes Principales (PCA) y simulación de Monte
Carlo para estudiar la clasificación de radiografías de tórax (dataset PneumoniaMNIST)
mediante Regresión Logística. El clasificador entrenado sobre las imágenes completas (m=
16384 píxeles) alcanza un accuracy de 0,8034 sobre el conjunto de prueba, mientras que la
proyección sobre k =12 componentes principales lo eleva a 0,8504, superando al modelo de
| referencia | con | una fracción | mínima | de  | la dimensión |     | original. |     |     |
| ---------- | --- | ------------ | ------ | --- | ------------ | --- | --------- | --- | --- |
Adicionalmente, se evaluó la robustez del clasificador ante rotaciones de 180◦ aplicadas
con probabilidad p a las imágenes de prueba, mediante N =1000 simulaciones indepen-
MC
dientes por cada valor de p. La probabilidad estimada de que la pérdida de accuracy supere
(Pˆ
una tolerancia δ = 0,1 pasa de ser prácticamente nula para p ≤ 0,2 a certeza = 1) para
p ≥ 0,6, con una transición abrupta entre p = 0,3 y p = 0,5. Este estimador se justifica
| formalmente |     | mediante | la Ley | de los Grandes |     | Números. |     |     |     |
| ----------- | --- | -------- | ------ | -------------- | --- | -------- | --- | --- | --- |
1

1. Introducción
Cuandoladimensióndelosdatos(m)esmuysuperioralnúmerodeobservacionesdisponibles
(n), como ocurre con imágenes de alta resolución, trabajar directamente en el espacio original
tiene dos costos: computacional (diagonalizar una matriz m×m es computacionalmente inefi-
ciente) y estadístico, conocido como la maldición de la dimensionalidad — cuantas más variables
irrelevantes o redundantes se incluyen, más datos se necesitan para estimar un modelo confiable.
PCA aborda ambos problemas: identifica las direcciones de mayor varianza de los datos y
permite proyectarlos sobre un subespacio de dimensión k ≪ m que concentra la mayor parte
de la variabilidad. En la práctica, cuando m ≫ n conviene calcular estas direcciones mediante
la Descomposición en Valores Singulares (SVD) de la matriz de datos centrada, en lugar de
diagonalizar directamente la matriz de covarianza de tamaño m×m.
Para evaluar la robustez de un clasificador frente al posible ruido de los datos se empleó la
simulación de Monte Carlo. Esta permite estimar cantidades de interés, como la probabilidad de
que el desempeño se degrade más allá de una tolerancia aceptable, promediando el resultado de
un gran número de repeticiones aleatorias. Que el promedio muestral converja a la probabilidad
verdadera a medida que crece el número de simulaciones se apoya formalmente en la Ley de los
Grandes Números.
En este trabajo se aplican ambas herramientas sobre un problema concreto de clasificación
de imágenes médicas: distinguir radiografías de tórax de pacientes sanos y con neumonía. El
objetivo es doble. Por un lado, estudiar cómo varía el desempeño de un clasificador de Regresión
Logística al reducir la representación de las imágenes a un número creciente de componentes
principales,ydeterminarsiexisteunsubespaciodedimensiónreducidaquepreservelacapacidad
de clasificación. Por otro lado, evaluar la robustez del clasificador ya entrenado frente a un tipo
específico de perturbación de las imágenes de prueba (rotaciones de 180◦ aplicadas de manera
aleatoria), estimando mediante simulaciones de Monte Carlo cuánto se degrada su desempeño y
con qué probabilidad esa degradación supera un umbral tolerable.
2. Metodología
2.1. Dataset y representación
El conjunto de datos utilizado es PneumoniaMNIST, compuesto por radiografías de tórax en
escala de grises de 128×128 píxeles, correspondientes a dos clases (0 = sano, 1 = neumonía).
Cada imagen se aplana en un vector de dimensión m = 128×128 = 16384, de modo que los
conjuntos de entrenamiento y de prueba quedan representados como matrices X
train
∈ Rntrain×m
y X
test
∈ Rntest×m, con sus etiquetas asociadas.
2.2. Clasificador
Se utilizó un modelo de Regresión Logística con el método de optimización newton-cg, en
lugar del método por defecto de la librería, porque este último no lograba converger para ciertos
valores de k. La métrica de evaluación es el accuracy calculado como la proporción de etiquetas
correctamente predichas.
2.3. PCA vía SVD
Dado que m (16384) es mucho mayor que n (número de imágenes de entrenamiento), diago-
nalizar directamente la matriz de covarianza (de tamaño m×m) resulta computacionalmente
inviable. En su lugar, se centra la matriz de entrenamiento (X = X −µ) y se calcula su
c train
descomposición en valores singulares:
X = USVT
c
2

Las columnas de V son las direcciones principales (autovectores de la matriz de covarianza),
y la proyección de cualquier conjunto X sobre las primeras k componentes se calcula como:
|     |     |     |     |     | Y   | = (X | −µ)V |     |
| --- | --- | --- | --- | --- | --- | ---- | ---- | --- |
|     |     |     |     |     | k   |      | k    |     |
donde V contiene las primeras k columnas de V. µ y V se estiman siempre a partir del
k
conjuntodeentrenamiento,inclusoalproyectarelconjuntodeprueba,paranofiltrarinformación
| de test | en la | estimación | de  | la base | de proyección. |     |     |     |
| ------- | ----- | ---------- | --- | ------- | -------------- | --- | --- | --- |
Este procedimiento es matemáticamente equivalente a diagonalizar la matriz de covarianza
1
estimada Cˆ = XTX : sus autovalores se relacionan con los valores singulares de X
|     | X   |     | c   | c   |     |     |     | c   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
n−1
mediante
s2
|     |     |     |     |     | λ   | =     | i   |     |
| --- | --- | --- | --- | --- | --- | ----- | --- | --- |
|     |     |     |     |     |     | i n−1 |     |     |
Es decir, V coincide con la matriz de autovectores de Cˆ (P en la notación de la cátedra), y
X
trabajarconlaSVDdeX evitaconstruirydiagonalizarexplícitamenteunamatrizdecovarianza
c
de tamaño m×m, sin perder equivalencia teórica con el método basado en covarianza.
| 2.4. | Diseño | del | experimento |     | de robustez |     | (Monte Carlo) |     |
| ---- | ------ | --- | ----------- | --- | ----------- | --- | ------------- | --- |
Fijando k = 2, se entrenó un clasificador sobre la proyección PCA del conjunto de entrena-
miento y se evaluó su accuracy de referencia A sobre el conjunto de prueba sin perturbar. Cabe
0
aclarar que A no coincide con el accuracy del baseline sin PCA reportado en la Sección 3.1: se
0
tratadeldesempeñodelmodeloconk = 2componentes,queeselpuntodepartidacontraelcual
se miden las pérdidas de esta sección. El modelo se entrena una única vez, con el conjunto de
entrenamiento sin perturbar; las rotaciones se aplican exclusivamente a las imágenes de prueba
| durante | las simulaciones. |     |     |     |     |     |     |     |
| ------- | ----------------- | --- | --- | --- | --- | --- | --- | --- |
Luego, para cada valor de probabilidad p en {0,1,0,2,...,0,9}, se generaron N MC = 1000
realizaciones independientes: en cada una, cada imagen del conjunto de prueba se rota 180◦ con
probabilidad p (y se deja sin modificar con probabilidad 1−p), se proyecta sobre las mismas
k = 2 componentes de entrenamiento, y se evalúa el accuracy resultante A p .
(i)
Para cada realización i se define la pérdida L (p) = A −A , y se fija una tolerancia δ = 0,1.
|     |     |     |     |     |     | i   | 0 p |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
E[A
Las cantidades de interés estimadas son el valor medio del accuracy p ] y la probabilidad
P (L(p) > δ), ambas calculadas como promedios muestrales sobre las N realizaciones (ver
p MC
| Sección | 3.6 para | la  | justificación | formal | de este | último). |     |     |
| ------- | -------- | --- | ------------- | ------ | ------- | -------- | --- | --- |
3. Resultados
| 3.1. | Clasificación |     | con | y sin | PCA |     |     |     |
| ---- | ------------- | --- | --- | ----- | --- | --- | --- | --- |
El clasificador entrenado sobre las imágenes completas, sin reducción de dimensionalidad,
alcanza un accuracy de 0,8034 sobre el conjunto de prueba. Este valor se toma como referencia
(baseline) para evaluar el efecto de proyectar los datos sobre un subespacio de menor dimensión.
Se evaluó el accuracy del modelo PCA + Regresión Logística para valores de k entre 2 y 492,
en pasos de 10. El mejor resultado se obtuvo con k = 12, con un accuracy de 0,8504, superior al
| baseline | utilizando | apenas |     | un 0,07% | de la | dimensión | original. |     |
| -------- | ---------- | ------ | --- | -------- | ----- | --------- | --------- | --- |
3

Figura 1: Accuracy del modelo PCA + Regresión Logística en función de k, comparado con el
baseline (línea punteada).
Observandoelgráfico(Figura1)sepuedenotarcómoelaccuracyrápidamentellegaalmáximo
en k = 12, luego baja y vuelve al mismo punto pero con k = 112. A partir de ese punto, se puede
notar una tendencia de la precisión del modelo a decrecer para k grande. Algo destacable a
mencionar es que con k = 2 el modelo ya tiene una certeza muy similar a la del baseline.
También se proyectó el conjunto de prueba sobre las dos primeras componentes principales
y se graficó un diagrama de dispersión coloreado por clase (sano/neumonía), con el objetivo de
evaluar visualmente si las direcciones de mayor varianza separan las clases.
4

Figura 2: Proyección del conjunto de prueba sobre las dos primeras componentes principales,
| coloreada | por clase. |     |     |     |
| --------- | ---------- | --- | --- | --- |
En el análisis de las dos componentes principales (Figura 2), a simple vista se puede denotar
un agrupamiento relativo de los puntos. Si bien hay entrecruzamiento, cualitativamente se puede
apreciar que la parte mayoritaria de las imágenes de pulmones sanos está agrupada más arriba
| que las | imágenes de | pulmones enfermos. |     |     |
| ------- | ----------- | ------------------ | --- | --- |
3.2. Efecto de las perturbaciones sobre las componentes principales
Antes de cuantificar la degradación del desempeño, resulta ilustrativo observar cómo la per-
turbación modifica la estructura de los datos en el espacio de componentes principales. Para una
realización de la simulación y distintos valores de p, se proyectó el conjunto de prueba perturba-
do sobre las dos primeras componentes principales obtenidas del conjunto de entrenamiento (sin
| perturbar), | y se graficó | el diagrama | de dispersión | correspondiente. |
| ----------- | ------------ | ----------- | ------------- | ---------------- |
5

Figura 3: Proyección del conjunto de prueba perturbado sobre las dos primeras componentes
principales, para distintos valores de p, coloreada por clase.
La Figura 3 muestra la proyección del conjunto de prueba perturbado sobre las mismas dos
primeras componentes principales de la Figura 2, para una realización de la simulación en cada
valor de p ∈ {0,1,0,2,...,0,9}.
Para p = 0,1 y p = 0,2, la estructura de la nube es prácticamente indistinguible de la
observada sin perturbar (Figura 2): las imágenes sanas se agrupan mayormente en la región
superior del plano, mientras que las imágenes con neumonía forman un núcleo denso en la zona
inferior. El solapamiento entre clases es similar al basal, con los centros de masa de ambas nubes
claramente diferenciados.
A partir de p = 0,3 y hasta p = 0,5, se observa una infiltración progresiva de puntos corres-
pondientes a pulmones enfermos dentro de la región que en la Figura 2 estaba dominada por
pulmones sanos. El núcleo denso de casos enfermos se mantiene compacto en la parte inferior
del plano, pero la proporción de puntos rojos mezclados en la zona superior aumenta de forma
sostenida, degradando la separabilidad visual entre clases.
Parap ≥ 0,6,lasuperposiciónentreclasesenlaregióncentraleinferiordelplanoespráctica-
mente total, y a simple vista no es posible distinguir una clase de otra en esa zona. Sin embargo,
incluso para p = 0,9 persiste una asimetría: un subconjunto de puntos correspondientes a pulmo-
nes sanos permanece disperso hacia valores más altos de la Componente 2 (y de la Componente
1), en una región que continúa relativamente libre de casos enfermos. Es decir, la mezcla entre
clases no es homogénea en todo el plano: lo que se pierde con el aumento de p es la separación
neta en el núcleo central de la nube, mientras que la dispersión característica de los sanos hacia
valores extremos de la Componente 2 se conserva parcialmente.
En ningún caso se observan agrupamientos espurios (subclusters aislados o estructuras nue-
vas): el efecto de la perturbación es un solapamiento progresivo de ambas nubes hacia una región
6

común, y no una reorganización cualitativa de la geometría de los datos. Este comportamiento
es consistente con la caída de accuracy documentada en las secciones siguientes: al aumentar
p, una fracción creciente de imágenes enfermas rotadas cae dentro de la región del espacio de
componentes principales que el clasificador asocia a la clase sana, erosionando progresivamente
la frontera de decisión aprendida durante el entrenamiento.
3.3. Accuracy medio en función de la perturbación
Mediante el método de Monte Carlo se estimó el valor medio del accuracy E[A ] como el
p
promedio de los accuracies obtenidos en las N = 1000 realizaciones correspondientes a cada
MC
valor de p:
Figura4:AccuracymedioestimadoE[A ]enfuncióndep,comparadocontraA (líneapunteada).
p 0
El accuracy de referencia sin perturbaciones fue A = 0,803. Al incrementar la probabilidad
0
de rotación p, el accuracy medio estimado mediante Monte Carlo disminuye de forma aproxima-
damente lineal: pasa de alrededor de 0,775 para p = 0,1 a 0,550 para p = 0,9. No se observa
un umbral abrupto en la curva de accuracy medio, sino una degradación progresiva y sostenida
a medida que aumenta la fracción esperada de imágenes rotadas. En el extremo p = 0,9, el
clasificador alcanza su menor desempeño promedio, con una disminución aproximada de 0,253
respecto del accuracy base.
3.4. Probabilidad de exceder la tolerancia
Para cada valor de p, se estimó la probabilidad P (L(p) > δ) como la proporción de las
p
N = 1000 realizaciones en las que la pérdida de accuracy superó la tolerancia δ = 0,1:
MC
7

Figura 5: Probabilidad estimada Pˆ (L(p) > δ) en función de p, con N = 1000 simulaciones
p MC
| por valor | de p y δ = | 0,1. |     |     |
| --------- | ---------- | ---- | --- | --- |
Laprobabilidadestimada(Figura5)permaneceprácticamentenulaparap ≤ 0,2(elclasifica-
dor es robusto ante una fracción baja de imágenes rotadas), sube de forma abrupta entre p = 0,3
y p = 0,5, y satura en 1,0 a partir de p = 0,6: en ese régimen todas las simulaciones registraron
| una pérdida       | de accuracy | superior          | a la tolerancia | fijada.   |
| ----------------- | ----------- | ----------------- | --------------- | --------- |
| 3.5. Distribución |             | de los accuracies |                 | simulados |
Finalmente, para cada valor de p se representó mediante un histograma la distribución de los
N accuracies obtenidos en las simulaciones, lo que permite observar no solo el desplazamiento
MC
del valor medio sino también la dispersión del desempeño ante la perturbación.
8

Figura 6: Distribución de los accuracies obtenidos en las N = 1000 simulaciones de Monte
MC
| Carlo, | para cada | valor de p. |     |     |     |
| ------ | --------- | ----------- | --- | --- | --- |
A medida que aumenta la probabilidad de rotación p, las distribuciones de accuracy se des-
plazan progresivamente hacia valores menores. Además, para valores bajos e intermedios de p se
observaunamayordispersióndelosresultados,mientrasqueparavaloresaltoslasdistribuciones
se concentran nuevamente alrededor de accuracies bajos. En general, los histogramas presentan
una forma aproximadamente simétrica alrededor de su valor medio, aunque pueden observarse
pequeñas asimetrías debidas a la naturaleza discreta del número de imágenes rotadas en cada
realización.
El umbral de tolerancia es A 0 −δ = 0,803−0,1 = 0,703. Para p = 0,1 y p = 0,2, la mayor
parte de la distribución se mantiene por encima de este umbral. En p = 0,3, una fracción de las
realizaciones ya queda por debajo del mismo. A partir de p = 0,4, la mayor parte de la masa de
las distribuciones se ubica por debajo de A −δ, lo que indica que las pérdidas superiores a la
0
| tolerancia | se vuelven    | frecuentes. |        |                |         |
| ---------- | ------------- | ----------- | ------ | -------------- | ------- |
| 3.6.       | Justificación | mediante    | la Ley | de los Grandes | Números |
Para cada valor fijo de p, se define en la i-ésima simulación la variable indicadora:
⊮{L
|     |     |     | I = | (p) > δ} |     |
| --- | --- | --- | --- | -------- | --- |
|     |     |     | i   | i        |     |
Como I es una variable de Bernoulli, su esperanza coincide con la probabilidad del evento
i
que indica:
|     |     |     | E[I ] = | P (L(p) > δ) |     |
| --- | --- | --- | ------- | ------------ | --- |
|     |     |     | i       | p            |     |
DadoquelasN simulacionessegenerandemaneraindependienteybajolasmismascondi-
MC
ciones para un p fijo, las variables I ,...,I son independientes e idénticamente distribuidas.
1 NMC
9

Por la Ley de los Grandes Números, el promedio muestral converge a la esperanza a medida que
| crece el número | de simulaciones: |     |     |     |     |     |
| --------------- | ---------------- | --- | --- | --- | --- | --- |
N
1 (cid:88)MC
|     |     |     | I   | −−−−−−→ | E[I ] = P (L(p) | > δ) |
| --- | --- | --- | --- | ------- | --------------- | ---- |
|     |     |     | i   |         | i p             |      |
|     |     | N   |     | NMC→∞   |                 |      |
MC i=1
| Esto justifica | formalmente | el  | estimador | utilizado: |     |     |
| -------------- | ----------- | --- | --------- | ---------- | --- | --- |
N (cid:88)MC
1
|     |     | Pˆ (L(p) | > δ) | =   | ⊮{L (p) | > δ} |
| --- | --- | -------- | ---- | --- | ------- | ---- |
|     |     | p        |      |     | i       |      |
|     |     |          |      | N   | MC      |      |
i=1
En la implementación, cada simulación aporta el valor 1 si la pérdida observada excede la
tolerancia y 0 en caso contrario, y el estimador se obtiene promediando esos valores sobre las
N realizaciones. El resultado es exactamente la proporción de simulaciones en las que ocurrió
MC
el evento L (p) > δ, es decir, el estimador de Monte Carlo justificado arriba.
i
4. Conclusiones
Respecto de la reducción de dimensionalidad, proyectar las imágenes sobre apenas k = 12
componentes principales no solo mantiene el desempeño del clasificador, sino que lo mejora
respectodelmodeloentrenadosobrelas16384dimensionesoriginales(0,8504contra0,8034).Esto
es consistente con la idea de que gran parte de la información relevante para distinguir pulmones
sanos de pulmones con neumonía está concentrada en unas pocas direcciones de mayor varianza,
y que retener dimensiones adicionales puede introducir ruido que perjudica la generalización del
modelo.
Respecto de la robustez, la simulación de Monte Carlo muestra que el clasificador tolera bien
una fracción baja de imágenes mal orientadas (probabilidad de perturbación p ≤ 0,2), pero su
desempeñosedegradadeformaabruptaapartirdep ≈ 0,3,alcanzandounaprobabilidaddefallo
(pérdida de accuracy mayor a 0,1) cercana a 1 para p ≥ 0,6. Este comportamiento evidencia que
el modelo no es robusto ante perturbaciones sistemáticas del preprocesamiento de las imágenes.
LavalidezdeestasestimacionesseapoyaenlaLeydelosGrandesNúmeros:conN = 1000
MC
simulaciones, el estimador muestral resulta consistente, aunque un análisis más riguroso podría
complementarse con un intervalo de confianza para cada probabilidad estimada, para cuantificar
| la incertidumbre | asociada    | al número | finito | de  | repeticiones. |     |
| ---------------- | ----------- | --------- | ------ | --- | ------------- | --- |
| Dificultades     | encontradas |           |        |     |               |     |
La principal dificultad de implementación fue la convergencia del clasificador: el método de
optimizaciónpordefectodelalibreríautilizadanoalcanzabalaconvergenciaparaalgunosvalores
de k, lo que producía advertencias. Se resolvió cambiando al método newton-cg, que converge de
manera estable para todos los k evaluados, y ampliando el número máximo de iteraciones.
Una segunda consideración fue el costo computacional del cálculo de las componentes prin-
cipales: dado que la dimensión de las imágenes (m = 16384) supera ampliamente el número de
observaciones disponibles, construir y diagonalizar la matriz de covarianza resultaba inviable,
por lo que usamos el SVD de la matriz de datos centrada, equivalente en términos teóricos pero
| mucho más eficiente. |     |     |     |     |     |     |
| -------------------- | --- | --- | --- | --- | --- | --- |
10
