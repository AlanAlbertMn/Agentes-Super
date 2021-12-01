from clasificador1 import clasificar1
from clasificador2 import clasificar2
from clasificador3 import clasificar3

filename = 'outFinal3.csv'
open(filename, 'w').close()
open(filename, 'a').write("Case, CSV, F-Score\n")

# Pruebas para clasificador 1 --> KNeighbors Classifier
# Se modifica el número de vecinos k (3, 5, 7)
# Se modifica la métrica (euclidean, manhattan, minkowski)
# Se modifica el número de trabajos paralelos a realizar para la búsqueda (1, -1), -1 significa que que va a usar todos los núcleos del procesador
# Se cambia el archivo a usar
def imprimir1(rList, n, name, distance, cores):
    with open(filename, "a") as file:
        file.write("C1 --> n={} distance metric={} parallel jobs={}, CSV={}," .format(n, distance, cores, name))
        file.write("{}" .format(str(rList)))
        file.write("\n")

# Pruebas para clasificador 1 --> Gaussian Naive Bayes
# Solo se puede modificar qué tan abierta o cerrada es la curva de la cual se toman los datos en el segmento de datos de entrenamiento
# Se cambia el archivo a usar
def imprimir2(rList, name, curve):
    with open(filename, "a") as file:
        file.write("C2 --> curve smoothing={}, CSV={}," .format(curve, name))
        file.write("{} " .format(str(rList)))
        file.write("\n")

# Pruebas para clasificador 1 --> Decision Tree Classifier
# Se modifica la estrategia a usar para dividir cada nodo (best, random)
# Se modifica la profundidad del árbol, usamos diversos valores (None, 1, 2, 3, 4)
# Se cambia el archivo a usar
def imprimir3(rList, name, split, depth):
    with open(filename, "a") as file:
        file.write("C3 --> split type={} tree depth={}, CSV={}," .format(split, depth, name))
        file.write("{} " .format(str(rList)))
        file.write("\n")

######################################################################################################

# Pruebas KNeighbors, Euclidian, n_jobs = 1
c1_3 = clasificar1(3, 'reviews1_vectors.csv', "euclidean", 1)
c1_5 = clasificar1(5, 'reviews1_vectors.csv', "euclidean", 1)
c1_7 = clasificar1(7, 'reviews1_vectors.csv', "euclidean", 1)

imprimir1(c1_3,3, "reviews1_vectors", "euclidean", 1)
imprimir1(c1_5,5, "reviews1_vectors", "euclidean", 1)
imprimir1(c1_7,7, "reviews1_vectors", "euclidean", 1)

c1_3 = clasificar1(3, "reviews2_vectors.csv", 'euclidean', 1)
c1_5 = clasificar1(5, "reviews2_vectors.csv", 'euclidean', 1)
c1_7 = clasificar1(7, "reviews2_vectors.csv", 'euclidean', 1)

imprimir1(c1_3,3, "reviews2_vectors", "euclidean", 1)
imprimir1(c1_5,5, "reviews2_vectors", "euclidean", 1)
imprimir1(c1_7,7, "reviews2_vectors", "euclidean", 1)

#Pruebas KNeighbors, euclidean, n_jobs = -1
c1_3 = clasificar1(3, 'reviews1_vectors.csv', 'euclidean', -1)
c1_5 = clasificar1(5, 'reviews1_vectors.csv', 'euclidean', -1)
c1_7 = clasificar1(7, 'reviews1_vectors.csv', 'euclidean', -1)

imprimir1(c1_3,3, "reviews1_vectors", "euclidean", -1)
imprimir1(c1_5,5, "reviews1_vectors", "euclidean", -1)
imprimir1(c1_7,7, "reviews1_vectors", "euclidean", -1)

c1_3 = clasificar1(3, "reviews2_vectors.csv", 'euclidean', -1)
c1_5 = clasificar1(5, "reviews2_vectors.csv", 'euclidean', -1)
c1_7 = clasificar1(7, "reviews2_vectors.csv", 'euclidean', -1)

imprimir1(c1_3,3, "reviews2_vectors", "euclidean", -1)
imprimir1(c1_5,5, "reviews2_vectors", "euclidean", -1)
imprimir1(c1_7,7, "reviews2_vectors", "euclidean", -1)

# Pruebas KNeighbors, Manhattan, n_jobs = 1
c1_3 = clasificar1(3, 'reviews1_vectors.csv', 'manhattan', 1)
c1_5 = clasificar1(5, 'reviews1_vectors.csv', 'manhattan', 1)
c1_7 = clasificar1(7, 'reviews1_vectors.csv', 'manhattan', 1)

imprimir1(c1_3,3, "reviews1_vectors", "manhattan", 1)
imprimir1(c1_5,5, "reviews1_vectors", "manhattan", 1)
imprimir1(c1_7,7, "reviews1_vectors", "manhattan", 1)

c1_3 = clasificar1(3, "reviews2_vectors.csv", 'manhattan', 1)
c1_5 = clasificar1(5, "reviews2_vectors.csv", 'manhattan', 1)
c1_7 = clasificar1(7, "reviews2_vectors.csv", 'manhattan', 1)

imprimir1(c1_3,3, "reviews2_vectors", "manhattan", 1)
imprimir1(c1_5,5, "reviews2_vectors", "manhattan", 1)
imprimir1(c1_7,7, "reviews2_vectors", "manhattan", 1)

# Pruebas KNeighbors, Manhattan, n_jobs = -1
c1_3 = clasificar1(3, 'reviews1_vectors.csv', 'manhattan', -1)
c1_5 = clasificar1(5, 'reviews1_vectors.csv', 'manhattan', -1)
c1_7 = clasificar1(7, 'reviews1_vectors.csv', 'manhattan', -1)

imprimir1(c1_3,3, "reviews1_vectors", "manhattan", -1)
imprimir1(c1_5,5, "reviews1_vectors", "manhattan", -1)
imprimir1(c1_7,7, "reviews1_vectors", "manhattan", -1)

c1_3 = clasificar1(3, "reviews2_vectors.csv", 'manhattan', -1)
c1_5 = clasificar1(5, "reviews2_vectors.csv", 'manhattan', -1)
c1_7 = clasificar1(7, "reviews2_vectors.csv", 'manhattan', -1)

imprimir1(c1_3,3, "reviews2_vectors", "manhattan", -1)
imprimir1(c1_5,5, "reviews2_vectors", "manhattan", -1)
imprimir1(c1_7,7, "reviews2_vectors", "manhattan", -1)

# Pruebas KNeighbors, Mikowski, n_jobs = 1
c1_3 = clasificar1(3, 'reviews1_vectors.csv', 'minkowski', 1)
c1_5 = clasificar1(5, 'reviews1_vectors.csv', 'minkowski', 1)
c1_7 = clasificar1(7, 'reviews1_vectors.csv', 'minkowski', 1)

imprimir1(c1_3,3, "reviews1_vectors", "minkowski", 1)
imprimir1(c1_5,5, "reviews1_vectors", "minkowski", 1)
imprimir1(c1_7,7, "reviews1_vectors", "minkowski", 1)

c1_3 = clasificar1(3, "reviews2_vectors.csv", 'minkowski', 1)
c1_5 = clasificar1(5, "reviews2_vectors.csv", 'minkowski', 1)
c1_7 = clasificar1(7, "reviews2_vectors.csv", 'minkowski', 1)

imprimir1(c1_3,3, "reviews2_vectors", "minkowski", 1)
imprimir1(c1_5,5, "reviews2_vectors", "minkowski", 1)
imprimir1(c1_7,7, "reviews2_vectors", "minkowski", 1)

# Pruebas KNeighbors, minkowski, n_jobs = -1
c1_3 = clasificar1(3, 'reviews1_vectors.csv', 'minkowski', -1)
c1_5 = clasificar1(5, 'reviews1_vectors.csv', 'minkowski', -1)
c1_7 = clasificar1(7, 'reviews1_vectors.csv', 'minkowski', -1)

imprimir1(c1_3,3, "reviews1_vectors", "minkowski", -1)
imprimir1(c1_5,5, "reviews1_vectors", "minkowski", -1)
imprimir1(c1_7,7, "reviews1_vectors", "minkowski", -1)

c1_3 = clasificar1(3, "reviews2_vectors.csv", 'minkowski', -1)
c1_5 = clasificar1(5, "reviews2_vectors.csv", 'minkowski', -1)
c1_7 = clasificar1(7, "reviews2_vectors.csv", 'minkowski', -1)

imprimir1(c1_3,3, "reviews2_vectors", "minkowski", -1)
imprimir1(c1_5,5, "reviews2_vectors", "minkowski", -1)
imprimir1(c1_7,7, "reviews2_vectors", "minkowski", -1)

##################################################################################

# Pruebas Gaussian Naive Bayes, var_smoothing = 0.06
c2 = clasificar2("reviews1_vectors.csv", 0.06)
imprimir2(c2, "reviews1_vectors", 0.06)

c2 = clasificar2("reviews2_vectors.csv", 0.06)
imprimir2(c2, "reviews2_vectors", 0.06)

# Pruebas Gaussian Naive Bayes, var_smoothing = 1e-09
c2 = clasificar2("reviews1_vectors.csv", 1e-09)
imprimir2(c2, "reviews1_vectors", 1e-09)

c2 = clasificar2("reviews2_vectors.csv", 1e-09)
imprimir2(c2, "reviews2_vectors", 1e-09)

# Pruebas Gaussian Naive Bayes, var_smoothing = 2e-09
c2 = clasificar2("reviews1_vectors.csv", 2e-09)
imprimir2(c2, "reviews1_vectors", 2e-09)

c2 = clasificar2("reviews2_vectors.csv", 2e-09)
imprimir2(c2, "reviews2_vectors", 2e-09)

# Pruebas Gaussian Naive Bayes, var_smoothing = 0.1
c2 = clasificar2("reviews1_vectors.csv", 0.1)
imprimir2(c2, "reviews1_vectors", 0.1)

c2 = clasificar2("reviews2_vectors.csv", 0.1)
imprimir2(c2, "reviews2_vectors", 0.1)

# Pruebas Gaussian Naive Bayes, var_smoothing = 0.08
c2 = clasificar2("reviews1_vectors.csv", 0.08)
imprimir2(c2, "reviews1_vectors", 0.08)

c2 = clasificar2("reviews2_vectors.csv", 0.08)
imprimir2(c2, "reviews2_vectors", 0.08)

############################################################################

# Pruebas Decision Tree Classifier, splitter = best, max_depth = None
c3 = clasificar3("reviews1_vectors.csv", 'best', None)
imprimir3(c3, "reviews1_vectors", "best", "None")

c3 = clasificar3("reviews2_vectors.csv", 'best', None)
imprimir3(c3, "reviews2_vectors", "best", "None")

# Pruebas Decision Tree Classifier, splitter = best, max_depth = 1
c3 = clasificar3("reviews1_vectors.csv", 'best', 1)
imprimir3(c3, "reviews1_vectors", "best", 1)

c3 = clasificar3("reviews2_vectors.csv", 'best', 1)
imprimir3(c3, "reviews2_vectors", "best", 1)

# Pruebas Decision Tree Classifier, splitter = best, max_depth = 2
c3 = clasificar3("reviews1_vectors.csv", 'best', 2)
imprimir3(c3, "reviews1_vectors", "best", 2)

c3 = clasificar3("reviews2_vectors.csv", 'best', 2)
imprimir3(c3, "reviews2_vectors", "best", 2)

# Pruebas Decision Tree Classifier, splitter = best, max_depth = 3
c3 = clasificar3("reviews1_vectors.csv", 'best', 3)
imprimir3(c3, "reviews1_vectors", "best", 3)

c3 = clasificar3("reviews2_vectors.csv", 'best', 3)
imprimir3(c3, "reviews2_vectors", "best", 3)

# Pruebas Decision Tree Classifier, splitter = best, max_depth = 4
c3 = clasificar3("reviews1_vectors.csv", 'best', 4)
imprimir3(c3, "reviews1_vectors", "best", 4)

c3 = clasificar3("reviews2_vectors.csv", 'best', 4)
imprimir3(c3, "reviews2_vectors", "best", 4)

# Pruebas Decision Tree Classifier, splitter = random, max_depth = None
c3 = clasificar3("reviews1_vectors.csv", 'random', None)
imprimir3(c3, "reviews1_vectors", "random", "None")

c3 = clasificar3("reviews2_vectors.csv", 'random', None)
imprimir3(c3, "reviews2_vectors", "random", "None")

# Pruebas Decision Tree Classifier, splitter = random, max_depth = 1
c3 = clasificar3("reviews1_vectors.csv", 'random', 1)
imprimir3(c3, "reviews1_vectors", "random", 1)

c3 = clasificar3("reviews2_vectors.csv", 'random', 1)
imprimir3(c3, "reviews2_vectors", "random", 1)

# Pruebas Decision Tree Classifier, splitter = random, max_depth = 2
c3 = clasificar3("reviews1_vectors.csv", 'random', 2)
imprimir3(c3, "reviews1_vectors", "random", 2)

c3 = clasificar3("reviews2_vectors.csv", 'random', 2)
imprimir3(c3, "reviews2_vectors", "random", 2)

# Pruebas Decision Tree Classifier, splitter = random, max_depth = 3
c3 = clasificar3("reviews1_vectors.csv", 'random', 3)
imprimir3(c3, "reviews1_vectors", "random", 3)

c3 = clasificar3("reviews2_vectors.csv", 'random', 3)
imprimir3(c3, "reviews2_vectors", "random", 3)

# Pruebas Decision Tree Classifier, splitter = random, max_depth = 4
c3 = clasificar3("reviews1_vectors.csv", 'random', 4)
imprimir3(c3, "reviews1_vectors", "random", 4)

c3 = clasificar3("reviews2_vectors.csv", 'random', 4)
imprimir3(c3, "reviews2_vectors", "random", 4)