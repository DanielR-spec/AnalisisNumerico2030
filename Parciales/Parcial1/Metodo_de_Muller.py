from numpy import sign
from numpy import  arange
from numpy import cos,sin
from numpy.lib.scimath import sqrt
import matplotlib.pyplot as plt
import time
import  sys

# x0 , x1x ,x2 son valores de aparoximaciones de la raiz 
def muller(funcion, x0, x1, x2, toleracia,iteraciones):
    error = 1e9 # se define un error inicial grande 
    x3 = 0
    i = 0 
    lerror = []
    lraiz= []
    while (error > toleracia):
        fx0 = funcion(x0)
        fx1 = funcion(x1)
        fx2 = funcion(x2)
        # a, b ,c son los nuevos coeficientes que van a acompañar al polinomio de gradado dos por cada iteracion
        # las ecuaciones mostradas salen del resultado de reducir una matriz los cuales al final indican que los valores de a,b,c dependen de las ecuaciones
        c = funcion(x2)
        b = (
            ((x0-x2)**2*(fx1-fx2)-(x1-x2)**2*(fx0-fx2)) /
            ((x0-x2)*(x1-x2)*(x0-x1))
        )
        a = (
            ((x1-x2)*(fx0-fx2)-(x0-x2)*(fx1-fx2)) /
            ((x0-x2)*(x1-x2)*(x0-x1))
        )
        #se evalua la formula cuadratica de cuando el valor del polinomio dado da 0 
        x3 = x2-(2*c)/(b+sign(b)*sqrt((b**2) - 4*a*c))
        #genera la formula cuadratica que estima la psoible riz
        g = lambda x : a*(x-x2)**2 + b*(x-x2) + c
        plt.plot(x,f(x), label="Funcion original")
        plt.plot(x,g(x),color='red',label="Funcion cuadratica")
        plt.xlim(xmin=-50,xmax=50)
        
        plt.show()
        time.sleep(0.5)
        error = abs(x3-x2)#calcula el error 
        x0 = x1
        x1 = x2
        x2 = x3
        lerror.append(error)
        lraiz.append(x3)
        i+=1
        if i > iteraciones:
            break
    print("Numero de iteraciones {} y cantidad de errores {}".format(i,len(lerror)))
    d = arange(1,i+1,1)

    plt.plot( d ,lerror,label= str(error))
    
    return (lraiz,lerror,i)

f = lambda x: cos(2*x)**2 - x**2
#f = lambda x: x*sin(x)-1
#f = lambda x: x**3 -2*x**2+(4/3)*x -(8/27)
x = arange(-50,50,0.5)
plt.plot(x,f(x))

x = muller(funcion=f, x0=-5, x1=1, x2=9, toleracia=1e-8,iteraciones = 200)

for i in range(x[2]):
    print("Valor {} Error {} ".format(x[0][i],x[1][i]))





