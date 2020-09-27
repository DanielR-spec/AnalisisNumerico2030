# -*- coding: utf-8 -*-
"""
Created on Thu Sep 25 20:45:45 2020
@author: Daniel Reyes,Julian Builes,SAntiago Bermudez,Daniel Fierro
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


def hornerd1(polinomio, x):
    r = 0
    cont = 0
    mayor = 0
    alturaMax = 0
    polinomio = Derivada(polinomio)
    for i in range(len(polinomio)):
        # multiplica el valor de la x
        # luego suma el coeficinte
        cont += 1
        r = r * x + polinomio[i]
        alturaMax = r
        if (alturaMax > mayor):
            mayor = alturaMax
            
    print("El numero de multiplicaciones con horner es  {}".format(cont))
    print ("La altura maxima del cohete es de {}".format(alturaMax))
    return r


if __name__ == "__main__":
    polinomio = [6,0,2.13,0,0.0013]
    hornerd1(polinomio,3)
    p = np.array(polinomio)
    r = lagval(x= 1 ,c=p)#no tiene sentido lo que da
    print(r)