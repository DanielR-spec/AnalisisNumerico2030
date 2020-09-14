# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 18:23:37 2020

autor original: Nick Ryan 
Modificado y adaptado por: Julian Builes, Santiago Dermudez,Daniel Fierro, Daniel Reyes 
"""
from scipy import optimize
import matplotlib.pyplot as plt



def brents(f, x0, x1, max_iter=50, tolerance=1e-8):
 
    fx0 = f(x0)
    fx1 = f(x1)
    ltolerance= []
    literations=[]
    lroots= []
    if (fx0 * fx1) >= 0:
        print("Raiz no esta detro de el rango dado")
        return 
 
    if abs(fx0) < abs(fx1):
        x0, x1 = x1, x0
        fx0, fx1 = fx1, fx0
 
    x2, fx2 = x0, fx0
 
    mflag = True
    steps_taken = 0
 
    while steps_taken < max_iter and abs(x1-x0) > tolerance:
        fx0 = f(x0)
        fx1 = f(x1)
        fx2 = f(x2)

        if fx0 != fx2 and fx1 != fx2:
            L0 = (x0 * fx1 * fx2) / ((fx0 - fx1) * (fx0 - fx2))
            L1 = (x1 * fx0 * fx2) / ((fx1 - fx0) * (fx1 - fx2))
            L2 = (x2 * fx1 * fx0) / ((fx2 - fx0) * (fx2 - fx1))
            new = L0 + L1 + L2
 
        else:
            new = x1 - ( (fx1 * (x1 - x0)) / (fx1 - fx0) )
 
        if ((new < ((3 * x0 + x1) / 4) or new > x1) or
            (mflag == True and (abs(new - x1)) >= (abs(x1 - x2) / 2)) or
            (mflag == False and (abs(new - x1)) >= (abs(x2 - d) / 2)) or
            (mflag == True and (abs(x1 - x2)) < tolerance) or
            (mflag == False and (abs(x2 - d)) < tolerance)):
            new = (x0 + x1) / 2
            mflag = True
 
        else:
            mflag = False
 
        fnew = f(new)
        d, x2 = x2, x1
 
        if (fx0 * fnew) < 0:
            x1 = new
        else:
            x0 = new
 
        if abs(fx0) < abs(fx1):
            x0, x1 = x1, x0
 
        steps_taken += 1
        ltolerance.append(abs(x1-x0))
        literations.append(steps_taken)
        lroots.append(x1)

    plt.plot(literations,ltolerance)
    plt.ylabel('Error')
    plt.xlabel('Iteracion')
    plt.title("Iteraciones contra el error")
    plt.show()
    return x1, steps_taken

if __name__ == "__main__":
    f = lambda x : x**3 - 2*x**2+(4*x)/3- (8/27)   
    root, steps = brents(f, -5, 5, tolerance=10e-9)
    print ("La raiz es:", root)
    print ("Iteciones:", steps)