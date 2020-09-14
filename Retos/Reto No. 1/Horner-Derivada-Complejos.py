# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 20:45:45 2020

@author: Julian Builes,SAntiago Bermudez,Daniel Reyes,Daniel Fierro
"""
import time
import matplotlib.pyplot as plt
import numpy as np
from numpy.polynomial.laguerre import lagval


def Derivada(C):
    m = len(C)-1
    j = 0
    D = [0 for i in range(len(C)-1)]
    while(j < len(C)-1):
        D[j] = C[j] * m
        j = j+1
        m = m-1
    return D


def horner(polinomio, x):
    r = 0
    cont = 0
    for i in range(len(polinomio)):
        # multiplica el valor de la x
        # luego suma el coeficinte
        cont += 1
        r = r * x + polinomio[i]
    rd = 0
    '''for i in range(len(polinomio)):
        # multiplica el valor de la x
        # luego suma el coeficinte
        cont += 1
        rd = rd * x + ( polinomio[-i] * i )
        print("pos i",polinomio[-i] * i)
        print(rd)'''
    print('Polinomio derivado {}'.format(rd))
    print("El numero de multiplicaciones con horner es  {}".format(cont))
    print(r)
    return r


def hornerd1(polinomio, x):
    r = 0
    cont = 0
    polinomio = Derivada(polinomio)
    for i in range(len(polinomio)):
        # multiplica el valor de la x
        # luego suma el coeficinte
        cont += 1
        r = r * x + polinomio[i]
    print("El numero de multiplicaciones con horner es  {}".format(cont))
    print(r)
    return r


def hornerd2(polinomio, x):
    r = 0
    cont = 0
    polinomio = Derivada(polinomio)
    polinomio = Derivada(polinomio)
    for i in range(len(polinomio)):
        # multiplica el valor de la x
        # luego suma el coeficinte
        cont += 1
        r = r * x + polinomio[i]

    print("El numero de multiplicaciones con horner es  {}".format(cont))
    print(r)
    return r

if __name__ == "__main__":
    polinomio = [1,-5,-9,155,-250]
    horner(polinomio,complex(1))
    hornerd1(polinomio, complex(1))
    hornerd2(polinomio, complex(1) )
    p = np.array(polinomio)
    r = lagval(x= 1 ,c=p)#no tiene sentido lo que da
    print(r)