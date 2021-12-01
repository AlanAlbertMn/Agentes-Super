# Proyecto final - Sistemas inteligentes

Dentro de la carpeta datasets se puede encontrar los archivos originales de las opiniones de Amazon, Yelp e Imdb.

## merge.py

Este programa se encarga de realizar la mezcla de los 3 archivos mencionados (Amazon, Yelp, Imdb) y se escriben los datos en el archivo "merged-data.txt"

## preprocessing1.py

Este programa se encarga de recoger los datos de "merged-data.txt" y hacer el primer preprocesamiento, el cual consiste en cambiar todo el texto a minúsculas y también quitar los signos de puntuación. También dentro de este archivo se hace la conversión a un formato legible para Weka que es "reviews1.arff".

## reviews1_vectors.csv

Es el archivo resultante de la continuación del primer preprocesamiento, en este caso se introdujo el archivo "reviews1.arff" a Weka y se le aplicó TF-IDF para poder convertirlo a vectores y sea ejecutado por los distintos clasificadores.

## stopwords.py

Este programa se encarga de utilizar los datos del archivo "merged-data.txt", utilizar la librería de nltk para obtener las stopwords y quitarlas del texto. Luego se escribe el nuevo texto sin las stopwords en el archivo "filteredText.txt"

## preprocessing2.py

Este programa se encarga de recoger los datos del archivo "filteredText.txt" y continuar el segundo preprocesamiento. El primer paso fue remover las stopwords, ahora también se cambia el texto a minúsculas y se quitan los signos de puntuación. Finalmente se cambia el formato del archivo hacia uno que puede leer Weka, el archivo obtenido es "reviews2.arff"

## reviews2_vectors.csv

Esta es la última parte del segundo preprocesamiento. Se mete a Weka el archivo "reviews2.arff" y se le aplica TF-IDF para convertir las palabras a vectores y pueda ser ejecutado por los diferentes clasificadores.

## clasificador1.py

En este programa se implementa el clasificador de K Neighbors por medio de la librería de scikit-learn

## clasificador2.py

En este programa se implementa el clasificador de Gaussian Naive Bayes por medio de la librería de scikit-learn

## clasificador3.py

En este programa se implementa el clasificador de Decision Tree Classifier por medio de la librería de scikit-learn

## main.py

En este programa se determinaron las distintas pruebas a realizar, desde ahí se mandan los parámetros a usar en las clases de los clasificadores y se ejecutan desde este programa.

Dentro de este archivo tenemos 66 pruebas diferentes, 36 para el clasificador de K Neighbors, 10 pruebas para Gaussian Naive Bayes y 20 pruebas para el clasificador de Decision Tree Classifier. La mitad de las pruebas son para el archivo CSV del primer preprocesamiento y la segunda mitad es para el archivo CSV obtenido del segundo preprocesamiento.

Para el clasificador de K Neighbors cambiamos el número de vecinos k (3, 5, 7), la métrica a usar (euclidean, minkowski, manhattan) y el número de trabajos paralelos a realizar durante la búsqueda (1 = 1 solo trabajo, -1 todos los trabajos posibles usando toda la capacidad del procesador)

Para el clasificador de Gaussian Naive Bayes solo se puede modificar la suavidad de la curva con la cual se toman los valores o datos del conjunto de datos a evaluar, para esto usamos 0.06, 0.1, 1e-09, 2e-09.

Para el clasificador de Decision Tree Classifier cambiamos la estrategia a usar para dividir los nodos (best, random) y la  máxima profundidad del árbol (ninguna, 1, 2, 3, 4, 5)

Para obtener un análisis, se corrió el programa 4 veces, primero para conocer los datos a grosso modo, estas corridas se encuentran en los archivos "outFinal.txt", "outFinal1.txt", "outFinal2.txt" y "outFinal3.txt"

Luego se volvieron a ejecutar, pero ahora para exportar los datos a un formato más legible como es CSV, las ejecuciones se encuentran en los archivos "outFinal.csv", "outFinal1.csv", "outFinal2.csv" y "outFinal3.csv"

## Clasificador no supervisado

Para el clasificador no supervisado se hizo uso de Weka, dentro de Weka se eligieron los archivos CSV de los diferentes preprocesamientos y se les aplicó el cluster de SimpleKMeans, para esto no fue posible poner la clase por la cual se puedan agrupar los elementos, sino que se siguió el patrón de los clasificadores supervisados y se eligió que se tomara el 80% de los datos como entrenamiento y el resto como parte de la prueba.

Si bien no fue lo ideal, no se encontró otra forma de evaluar los datos.

De esto podemos ver cómo funcionan las distintas métricas y cómo agrupan los datos.

Los modelos de estos experimentos se encuentran en la carpeta de "modelos_no_supervisados"