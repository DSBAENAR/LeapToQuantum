import matplotlib.pyplot as plot
import numpy as np
from LibreriaCompleja import *
def ActionBooleanMatrix(matrix, vector):
    row, column = len(matrix), len(matrix[0])
    lengvector = len(vector)

    if column == lengvector:
        answer = [False for columna in range(row)]

        for i in range(row):
            booleanvariable = True

            for j in range(column):
                booleanvariable = matrix[i][j] and vector[j]
                answer[i] = answer[i] or booleanvariable

        return answer
    print("Las dimensiones de las matrices no permiten la multiplicacion")


def BoolClic(booleanmatrix, booleanvector, Numberclicks):
    for c in range(Numberclicks):
        booleanvector = ActionBooleanMatrix(booleanmatrix, booleanvector)
    return booleanvector


def ProbabilisticClicks(matrix, statevector, Numberclicks):
    for i in range(Numberclicks):
        statevector = ActionBooleanMatrix(matrix, statevector)
    return statevector

def QuantumClicks(matrix, statevector, Numberclicks):
    L=[]
    for i in range(Numberclicks):
        statevector = ActionBooleanMatrix(matrix, statevector)
    for row in statevector:
        fila = (ComplexMod(row))**2
        L +=[fila]
    return L

def ProbabilisticPlot(vector):
    Axes = len(vector)
    x = np.array([x for x in range(Axes)])
    y = np.array([round(vector[x]*100, 3) for x in range(Axes)])
    plot.bar(x, y, color="blue", align="center")
    plot.title("Vector Probabilities")
    plot.show()
    