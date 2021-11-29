from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, precision_recall_fscore_support

def clasificar3(archive):
    print("\nDecision Tree")
    Archivo = open(archive, 'r')
    Clases = []
    Valores = []
    for x in Archivo.readlines():
      if len(x) > 1 and x[:5] != "class":
        Atrib = x.replace('\n', '').split(',')
        Clases.append(Atrib[0])
        Valores.append(list(map(float, Atrib[2:])))

    Datos_train, Datos_test, Clase_Train, Clase_Test = train_test_split(Valores, Clases, test_size = 0.2)

    algoritmo = DecisionTreeClassifier()

    algoritmo.fit(Datos_train, Clase_Train)

    ClasesRecuperadas = algoritmo.predict(Datos_test)

    Matriz = confusion_matrix(Clase_Test, ClasesRecuperadas)
    tn, fp, fn, tp = confusion_matrix(Clase_Test, ClasesRecuperadas).ravel()
    print('\nMatriz de confusion:')
    print(Matriz)

    resultList = precision_recall_fscore_support(Clase_Test, ClasesRecuperadas, average = 'micro')
    precision, recall, fscore, _ = resultList
    print('\nPrecision:', precision, '\nRecuerdo:', recall, '\nF-score:', fscore, '\n')
    print(resultList)
    r = list(resultList)
    r.pop()
    return r