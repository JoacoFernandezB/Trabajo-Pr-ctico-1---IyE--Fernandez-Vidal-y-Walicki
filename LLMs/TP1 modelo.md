|     |             | Universidad |        |          | de San       | Andrés    |      |
| --- | ----------- | ----------- | ------ | -------- | ------------ | --------- | ---- |
|     | Inferencia  |             |        |          | y Estimación |           |      |
|     |             | Trabajo     |        | Práctico |              | N.º 1     |      |
|     |             | Compresión  |        |          | de Imágenes  |           |      |
|     | Profesores: |             | Matías | Perlin,  | Pau García   | Gulisano, | Juan |
Ponce
|     |        |        | Integrantes            |     | (Grupo | 4):      |       |
| --- | ------ | ------ | ---------------------- | --- | ------ | -------- | ----- |
|     | Máximo | Barral | - barralm@udesa.edu.ar |     |        | - Legajo | 36585 |
Lautaro Valentín Caminoa - lcaminoa@udesa.edu.ar - Legajo 36571
|     | Franco | Sandri | - fsandri@udesa.edu.ar |     |     | - Legajo | 36530 |
| --- | ------ | ------ | ---------------------- | --- | --- | -------- | ----- |
Resumen
El presente trabajo aborda la compresión de imágenes mediante el análisis de componentes prin-
cipales (PCA), una técnica estadística de reducción de dimensionalidad. Se estudió en primer
lugar la correlación espacial entre píxeles vecinos, mostrando que una mayor redundancia local
facilita la compresión. Posteriormente se implementó el algoritmo de PCA desde cero, segmen-
tando las imágenes en bloques y proyectando los datos en un subespacio de menor dimensión,
con el objetivo de evaluar la pérdida de información frente al ahorro de espacio. La reconstruc-
ción de las imágenes evidenció que es posible mantener una alta fidelidad visual conservando
solo una fracción de los componentes principales, aunque con pérdidas graduales en detalles
finos al incrementar el porcentaje de compresión. Finalmente, el análisis cuantitativo mediante
el error cuadrático medio (MSE) confirmó el compromiso entre eficiencia y calidad, validando
a PCA como una herramienta efectiva para la compresión de imágenes en contextos donde la
| redundancia | espacial | es significativa. |     |     |     |     |     |
| ----------- | -------- | ----------------- | --- | --- | --- | --- | --- |

1. Introducción
En épocas de big data, el volumen de información generada y almacenada crece a un
ritmoexponencial.Dentrodeesteescenario,lacompresióndeinformación(yenparticular
deimágenes)seconvierteenunprocesoesencialparaoptimizarelalmacenamiento,reducir
costos de transmisión y mejorar la eficiencia en el procesamiento de grandes volúmenes de
información visual. El análisis de componentes principales (PCA, por sus siglas en inglés)
constituye una de las técnicas más utilizadas para la reducción de dimensionalidad.
El fundamento de PCA radica en identificar las direcciones de mayor varianza dentro
de un conjunto de datos y proyectarlos en un subespacio de menor dimensión, sin perder
información esencial. En la práctica, se implementa de manera eficiente a través de la
| Descomposición |     | en Valores | Singulares |     | (SVD). |     |     |     |     |     |
| -------------- | --- | ---------- | ---------- | --- | ------ | --- | --- | --- | --- | --- |
Sea A ∈ Rn×m la matriz de datos centrados en la media. Su factorización SVD es:
|     |      |     |      |     | A   | = USV⊤, |     |     |      | (1) |
| --- | ---- | --- | ---- | --- | --- | ------- | --- | --- | ---- | --- |
|     | Rn×n |     | Rm×m |     |     |         |     |     | Rn×m |     |
donde U ∈ y V ∈ son matrices ortogonales, y S ∈ es una matriz
diagonal rectangular cuyos elementos s ≥ 0 son los valores singulares de A.
i
Matemáticamente, consideramos que cada bloque de la imagen puede representarse
como un vector X ∈ Rm, donde m corresponde al número de píxeles del bloque. A partir
| de ello, | se construye | la  | matriz | de covarianza |     |     |     |     |     |     |
| -------- | ------------ | --- | ------ | ------------- | --- | --- | --- | --- | --- | --- |
1
|     |     |     |     | Cd  | =   |     | XTX, |     |     | (2) |
| --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- |
X
n−1
cuyos autovectores definen la base ortogonal de proyección. La transformación PCA con-
siste en proyectar los datos centrados en la media sobre los k autovectores asociados a los
| mayores | autovalores: |     |     |     |     |      |       |     |     |     |
| ------- | ------------ | --- | --- | --- | --- | ---- | ----- | --- | --- | --- |
|         |              |     |     | Y   | =   | V⊤(X | −µ ), |     |     | (3) |
|         |              |     |     |     |     | k    | X     |     |     |     |
mientras que la reconstrucción de los datos comprimidos se realiza aplicando la transfor-
| mación | inversa: |     |     |     |      |        |     |     |     |     |
| ------ | -------- | --- | --- | --- | ---- | ------ | --- | --- | --- | --- |
|        |          |     |     |     | Xc = | V Y +µ | .   |     |     | (4) |
|        |          |     |     |     |      | k      | X   |     |     |     |
Existe una relación directa entre los valores singulares de A y los autovalores de la
| covarianza | C   | :   |     |     |     |     |     |     |     |     |
| ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
X
s2
|     |     |     |     | λ = | i   | , i | = 1,...,m, |     |     | (5) |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- |
i
n−1
de modo que los autovectores de C coinciden con las columnas de V. Esta equivalencia
X
asegura que PCA puede resolverse directamente mediante SVD, con ventajas de estabili-
| dad numérica |     | y eficiencia | computacional. |     |     |     |     |     |     |     |
| ------------ | --- | ------------ | -------------- | --- | --- | --- | --- | --- | --- | --- |
Una vez obtenida la representación comprimida, surge la necesidad de evaluar su
calidad respecto de la imagen original. Para ello se emplean métricas cuantitativas, siendo
| el error | cuadrático | medio | (MSE) | una | de  | las más | utilizadas: |           |     |     |
| -------- | ---------- | ----- | ----- | --- | --- | ------- | ----------- | --------- | --- | --- |
|          |            |       |       |     |     | Nw N    |             |           |     |     |
|          |            |       |       |     | 1   | X X     | h (cid:16)  | (cid:17)2 |     |     |
|          |            |       | MSE   | =   |     |         | p −p        | ,         |     | (6) |
|          |            |       |       |     |     |         | ij bij      |           |     |     |
N N
|     |     |     |     |     | w   | h i=1j=1 |     |     |     |     |
| --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- |
1

donde N y N son las dimensiones de la imagen y p , p representan respectivamente los
w h ij bij
valores de los píxeles originales y reconstruidos. A su vez, el nivel de compresión alcanzado
se cuantifica a través del porcentaje de espacio ahorrado:
!
k
S = 1− ×100%. (7)
m
El objetivo del presente trabajo es implementar PCA en el contexto de compresión
de imágenes, evaluar su desempeño mediante métricas cuantitativas y estudiar la relación
entre la correlación espacial de los píxeles y la eficiencia de la compresión. Con ello, se
busca profundizar tanto en la comprensión teórica del algoritmo como en su aplicación
práctica en el análisis moderno de datos visuales.
2. Metodología
En la primera etapa del trabajo se estudió la correlación entre píxeles vecinos de dos
imágenes distintas. Para ello se construyeron pares de valores correspondientes a píxeles
contiguos en dirección vertical, que luego fueron representados en gráficos de dispersión.
Las distribuciones obtenidas evidenciaron que las imágenes no se comportan como con-
juntos aleatorios de intensidades, sino que presentan una marcada relación entre valores
cercanos. Esta observación se cuantificó mediante el cálculo de coeficientes de correlación
de Pearson y, a continuación, se aplicó una transformación lineal que permitió desacoplar
las variables y generar un nuevo sistema de ejes con componentes menos correlacionadas.
Dicho procedimiento puso de manifiesto la capacidad de PCA para concentrar la varia-
bilidad en una única dirección predominante, justificando así su utilización como técnica
de reducción de dimensión.
PosteriormenteseimplementólafuncióndetransformaciónPCAsinrecurriralibrerías
externas que resuelvan el problema automáticamente. A partir de la segmentación de
la imagen en bloques de 8 × 8. Con esta información utilizamos una implementación
propia de descomposición de valores singulares (SVD) con la que fue posible proyectar los
bloques originales en un espacio de menor dimensión que conserva la mayor parte de la
variabilidad(1).Sefijóunahorrodeespaciodel80%,loqueimplicómantenerúnicamente
un subconjunto de componentes principales. El gráfico de autovalores permitió distinguir
claramente qué información se conservaba y qué parte se descartaba, mostrando una caída
pronunciada que justifica la reducción.
Asimismo, con el fin de evaluar el rendimiento de esta implementación, elaboramos
un algoritmo de descompresión que revierte el proceso anterior. A partir de los vectores
comprimidos se reconstruyó cada bloque según la ecuación (4) y, con ellos, la imagen
completa. El resultado visual mostró que, pese a la pérdida de información, la imagen
preservaba sus detalles principales.
Finalmente, se evaluó cuantitativamente el desempeño de la compresión. Se calculó el
error cuadrático medio (MSE) de la reconstrucción siguiendo la definición en (6) para dis-
tintos niveles de ahorro de espacio S definidos en (7). Los resultados permitieron observar
cómo el error crece al aumentar el porcentaje de compresión. Además, se compararon las
imágenes reconstruidas para diferentes valores de S, lo que puso en evidencia el impacto
visual de la reducción de información aplicada mediante la transformación PCA.
2

3. Resultados
| 3.1. Correlación |     | entre | píxeles | vecinos |     |     |
| ---------------- | --- | ----- | ------- | ------- | --- | --- |
Para analizar la redundancia espacial en imágenes, se extrajeron pares verticales de
píxeles utilizando la función extraer_pares_verticales, que recorre la imagen en blo-
ques 2×1 y construye vectores (X ,X ), donde X es el valor del píxel superior y X el
|     |     |     | 1 2 | 1   |     | 2   |
| --- | --- | --- | --- | --- | --- | --- |
inferior. Se seleccionaron dos imágenes de prueba con características contrastantes.
El análisis estadístico arrojó los siguientes coeficientes de correlación de Pearson:
|     |     | ρ       | = 0,9792, | ρ       | = 0,1459. |     |
| --- | --- | ------- | --------- | ------- | --------- | --- |
|     |     | Imagen1 |           | Imagen2 |           |     |
Estos valores reflejan la teoría de la redundancia espacial: en la Imagen 1, la alta
correlación indica que los valores de píxeles vecinos son similares, lo que implica que la
información está altamente repetida y, por lo tanto, la imagen es susceptible de compre-
sión eficiente. En cambio, la Imagen 2 presenta baja correlación, lo que sugiere mayor
variabilidad local y menor redundancia, dificultando la compresión sin pérdida signifi-
cativa de información. En los gráficos de dispersión, ambas imágenes muestran el efecto
de la proyección PCA en R2: la nube de puntos se realinea respecto a los ejes principa-
les, evidenciando el desacople de las variables correlacionadas y la concentración de la
| variabilidad | en la dirección | predominante. |     |     |     |     |
| ------------ | --------------- | ------------- | --- | --- | --- | --- |
Figura 1: Resultados obtenidos: (izquierda) imágenes originales de prueba; (centro) dis-
persión de pares de píxeles verticales; (derecha) histogramas de intensidades de píxeles,
evidenciando la distribución de valores y la redundancia espacial en cada imagen.
3

Figura 2: Dispersión de los pares verticales tras la proyección PCA en R2 para ambas
imágenes. La nube de puntos se realinea respecto a los ejes principales, mostrando cómo
PCA (3) desacopla las variables correlacionadas y concentra la variabilidad en la dirección
predominante.
3.2. Compresión mediante PCA
Para evaluar la compresión, se segmentó una tercera imagen en bloques de 8×8 píxeles
y se aplanaron por columnas, generando vectores de dimensión m = 64. Se implementó
PCA desde cero, haciendo uso de una implementación propia de SVD basada en la teoría
(1), seleccionando el número de componentes principales k según el criterio de Space
Saving (S) (7). El número de componentes principales k se seleccionó según el porcentaje
de ahorro de espacio S (7). Para un ahorro del 80% (S = 80%) se conservaron k = 13
componentes, descartando las 51 restantes.
Figura 3: Espectro de autovalores de la matriz de covarianza sobre bloques de 8 × 8.
Los componentes principales conservados (azul) corresponden a las direcciones de mayor
varianza, mientras que los descartados (rojo) representan información redundante. La
caída pronunciada evidencia que la mayor parte de la información se preserva utilizando
un subconjunto reducido de componentes, como se predice en (3).
4

Como vemos en la Figura 3, el espectro de autovalores decrece rápidamente, lo que
indica que la mayor parte de la varianza de los datos está concentrada en unas pocas com-
ponentes. Este comportamiento es consistente con la teoría de PCA, que busca identificar
lasdireccionesdemáximavarianzaparareducirladimensionalidadsinperderinformación
relevante.
3.3. Descompresión
La reconstrucción de la imagen se realizó revirtiendo la proyección PCA(4), utilizando
los componentes principales conservados (Y , Vk, µ). El resultado fue una imagen visual-
mente muy similar a la original, aunque con ligeras pérdidas en detalles finos y texturas,
atribuibles a la eliminación de componentes de menor varianza. Este resultado prácti-
co valida la capacidad de PCA para comprimir imágenes manteniendo la calidad visual,
especialmente cuando la redundancia espacial es alta.
Figura 4: Comparación visual entre la imagen original (izquierda) y la reconstruida me-
diante PCA (derecha).
3.4. Medidas de desempeño
El desempeño de la compresión se evaluó mediante el error cuadrático medio (MSE)
definido en (6) para distintos niveles de ahorro de espacio S, desde 5% hasta 95%. Los
resultadosmuestranqueelMSEaumentadeformaconstantealincrementarS,esdecir,al
retenermenoscomponentesprincipales.Estecomportamientoescoherenteconlateoría:al
reducir la dimensionalidad, se descarta información y aumenta el error. Cabe señalar que,
cómo se evaluó en la Sección 3.1, la relación entre el MSE y el porcentaje de compresión
depende de las características particulares de la imagen analizada.
5

Figura 5: Error cuadrático medio (MSE) de la reconstrucción en función del porcentaje de
ahorro de espacio S. Se observa que al retener menos componentes principales, aumenta
el error de reconstrucción, reflejando el compromiso entre compresión y calidad visual
Figura 6: Comparación entre la imagen original y su reconstrucción con S = 85%, S =
90%, S = 95%.
El análisis visual complementario evidenció una degradación progresiva de la calidad
a medida que aumentaba el valor de S. No obstante, incluso con un 85% de ahorro de
espacio, la imagen conserva una estructura global fácilmente reconocible y las pérdidas de
6

calidad se concentran principalmente en los detalles finos y la nitidez. Con S = 95% la
estructura general sigue siendo identificable, aunque la distorsión resulta ya notoria. Este
comportamiento, si bien esperable en términos teóricos, resulta llamativo por la magnitud
del ahorro de información logrado frente a la calidad aún preservada en la reconstrucción.
4. Conclusiones
Todo lo expuesto anteriormente demuestra el potencial del análisis de componentes
principales (PCA) para reducir la dimensionalidad de las imágenes preservando la mayor
cantidad posible de información. Este efecto resulta particularmente evidente cuando la
correlación local entre píxeles es alta, ya que la redundancia de datos se traduce en una
concentración del peso de la varianza en pocos autovalores. En consecuencia, es posi-
ble descartar una mayor cantidad de componentes sin generar pérdidas significativas, lo
que refuerza la coherencia entre los resultados obtenidos y los fundamentos teóricos del
método.
A continuación, se implementó el algoritmo de PCA desde cero, segmentando las imá-
genes en bloques y proyectando los datos en un subespacio de menor dimensión mediante
una implementación propia de la descomposición en valores singulares (SVD). Durante
este proceso, al comparar el rendimiento de nuestra función our_svd con la función nativa
de NumPy (np.linalg.svd), se observó la aparición de una distorsión en los resultados
al emplear la segunda, lo que motivó un análisis más detallado de las diferencias entre
ambas implementaciones.
Figura 7: Comparación entre reconstrucciones obtenidas con nuestra implementación de
SVD (our_svd) y con np.linalg.svd. En este último caso se observaron distorsiones
visuales, atribuibles a la ausencia de la transposición necesaria en el procedimiento de
PCA.
Esta diferencia se identificó tras una tarea de depuración, en la cual comprobamos que
nuestrafunciónour_svdproducíareconstruccionescorrectasmientrasquenp.linalg.svd
introducía distorsiones visibles. La causa radica en que our_svd opera directamente sobre
la matriz de covarianza, obteniendo autovalores y autovectores ya alineados con la for-
mulación de PCA (ya que fue diseñada teniendo esto en mente), mientras que la función
nativa de numpy realiza la descomposición sobre la matriz de datos original y devuelve
7

la factorización estándar U,S,VT. Aunque ambas aproximaciones son matemáticamente
equivalentes, la salida de NumPy no está adaptada de manera inmediata para PCA: los
vectores aparecen como VT en lugar de V, los signos pueden invertirse y los valores singu-
lares requieren reinterpretarse para reflejar la varianza explicada. La falta de estos ajustes
fue lo que generó las distorsiones, y la depuración realizada nos permitió concluir la im-
portancia de controlar explícitamente la correspondencia entre autovalores, autovectores
y valores singulares en la implementación del método.
Finalmente, este trabajo abre la puerta a posibles mejoras y extensiones. Una pri-
mera línea sería comparar el desempeño de PCA con otros métodos de compresión más
utilizados en la práctica y evaluar sus rendimientos computacionales. También resultaría
interesante analizar la sensibilidad del algoritmo frente a distintos tipos de imágenes (fo-
tografías, texturas, patrones sintéticos) y estudiar cómo la correlación espacial afecta de
manera diferencial la compresibilidad.
8
