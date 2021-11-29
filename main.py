from clasificador1 import clasificar1
from clasificador2 import clasificar2
from clasificador3 import clasificar3

open('outFinal.txt', 'w').close()

def imprimir1(rList, n, name):
    with open("outFinal.txt", "a") as file:
        file.write("C1 n={} csv={}\n" .format(n, name))
        for i in rList:
            file.write("{} " .format(str(i)))
        file.write("\n")

def imprimir2(rList, name):
    with open("outFinal.txt", "a") as file:
        file.write("C2 csv={}\n" .format(name))
        for i in rList:
            file.write("{} " .format(str(i)))
        file.write("\n")

def imprimir3(rList, name):
    with open("outFinal.txt", "a") as file:
        file.write("C3 csv={}\n" .format(name))
        for i in rList:
            file.write("{} " .format(str(i)))
        file.write("\n")

c1_3 = clasificar1(3, 'reviews1_vectors.csv')
c1_5 = clasificar1(5, 'reviews1_vectors.csv')
c1_7 = clasificar1(7, 'reviews1_vectors.csv')

imprimir1(c1_3,3, "reviews1_vectors")
imprimir1(c1_5,5, "reviews1_vectors")
imprimir1(c1_7,7, "reviews1_vectors")

c1_3 = clasificar1(3, "reviews2_vectors.csv")
c1_5 = clasificar1(5, "reviews2_vectors.csv")
c1_7 = clasificar1(7, "reviews2_vectors.csv")

imprimir1(c1_3,3, "reviews2_vectors")
imprimir1(c1_5,5, "reviews2_vectors")
imprimir1(c1_7,7, "reviews2_vectors")

c2 = clasificar2("reviews1_vectors.csv")
imprimir2(c2, "reviews1_vectors")

c2 = clasificar2("reviews2_vectors.csv")
imprimir2(c2, "reviews2_vectors")

c3 = clasificar3("reviews1_vectors.csv")
imprimir3(c3, "reviews1_vectors")

c3 = clasificar3("reviews2_vectors.csv")
imprimir3(c3, "reviews2_vectors")