import math 
import numpy as np
def ComplexMod(c1):
    return abs(c1[0])
def norm_vec(vec):
    operator = 0
    for i in range(len(vec)):
        operator += (abs(vec[i]))**2
        #print(operator)
    norm = math.sqrt(operator)
    return norm

def Normalizar(vect):
    L=[]
    for elemento in vect:
        elemento=(1/norm_vec(vect))*elemento
        L.append(elemento)
    return L
print([[7+2j],[3-4j]])
def Probability(vector):
    print(norm_vec(vector))
    busqueda_arriba=ComplexMod(vector[0])/((norm_vec(vector))**2)
    busqueda_abajo=ComplexMod(vector[1])/((norm_vec(vector))**2)
    return busqueda_arriba
Probability([[7+2j],[3-4j]])