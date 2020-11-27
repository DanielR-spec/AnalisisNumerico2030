import numpy 
import matplotlib.pyplot as plt    #here we load matplotlib
from scipy import integrate
import matplotlib.animation as animation
import random as ran
from math import sqrt
class Hodgkin():
    I = 4.5
    C = 0.8
    taou = 1.9
    Vin = 0
    Ifn=2
    Rin=0
    t = numpy.linspace(0,100,300)

    f0= [0,0]
   # sol =  integrate.odeint(f,f0,t)
    y0 =  numpy.array([0,0])
    t0 = numpy.array([0,100])
    sol = []
    Rsol = []
    fig, axes = plt.subplots()
    #sol2=integrate.solve_ivp(lambda t,v: self.f(v,t), t0, y0,method='LSODA')
    def establecer(self,Iin,Ifn,C,taou,Vin,Rin):
        self.I = Iin
        self.Ifn = Ifn
        self.C = C
        self.taou =taou
        self.Vin = Vin
        self.Rin = Rin
        self.f0 = [Vin,Rin]
        self.y0 =  numpy.array([Vin,Vin])
        pass

    def f(self,c,t):
        V = c[0]
        R = c[1]
        dVdt = (-(17.81 + 47.71*V + 32.63*V**2) * (V - 0.55) - 26.0*R*(V +0.92)+self.I)/self.C
        dRdt = (1/self.taou) *(-R  + 1.35*V +1.03)
        return [dVdt,dRdt]


    def actualizar(self,i):
        self.ax.clear()
        self.I =i
        sol =  integrate.odeint(self.f,self.f0,self.t)
        plt.plot(self.t,sol[:,0],'r-')
        plt.title(self.I)
       

    def graficarMovimiento(self):
        self.fig =  plt.figure()
        self.ax = plt.gca()
        self.ani =animation.FuncAnimation(self.fig,self.actualizar,range(self.I,self.Ifn,1))     
        self.plot()


    def plot(self):
        plt.show()

    def graficarRK(self):     
        sol2=integrate.solve_ivp(lambda t,v: self.f(v,t), self.t0,self.y0,method='RK45')
        self.fig, self.axes = plt.subplots()
        self.sol = sol2.y[0]
        self.t = sol2.t
        self.axes.plot(sol2.t,sol2.y[0],'r-')
        plt.xlabel('T[ms]')
        plt.ylabel('V')
        plt.title('Hodgkin-huxley')
        plt.legend(("RK45"))
        self.plot()

    def graficarOde(self):
        sol1 =  integrate.odeint(self.f,self.f0,self.t)
        self.sol = sol1[:,0]
        self.Rsol = sol1[:,1]
        self.fig, self.axes = plt.subplots()
        self.axes.plot(self.t,sol1[:,0])
        plt.xlabel('T[ms]')
        plt.ylabel('V')
        plt.title('Hodgkin-huxley')
        plt.legend("Adams Bashforth")
        
        self.plot()

    def campodePendientes(self):
        color=['red','green','blue','yellow', 'magenta']
        X,Y = numpy.meshgrid(self.t,self.sol)
        U = 1
        V= self.sol
        print(V)
        V =self.f([self.sol,self.Rsol],self.t)
        V = V[0]
        j = []
        y = []
        for i in V:
            U2, V2 = U/sqrt(U**2+i**2), i/sqrt(U**2+i**2)
            j .append(U2)
            y.append(V2)

        plt.quiver(self.t,self.sol,j,y)

        self.plot()
    
    
    def mapalogistico(self):
        minimo = min(self.sol)*100
        maximo = max(self.sol)*100
        print(minimo)
        print(maximo)
        valor_r = numpy.linspace(int(minimo),int(maximo),6000 )       
        print(valor_r[0])
        valor_f = list()
        eje_r = list()
        
        for i in valor_r:
            l= self.logistic_iteration(ran.randint(100,2000),0.45,i)
            valor_f.append(l)
            eje_r.append(i)


        plt.plot(eje_r,valor_f)
        self.plot()

    def logistic_iteration(self,N, xinicial, r):
        logistic=0
        for i in range(N):
            logistic = r*xinicial*(1-xinicial)
            xinicial = logistic
        return logistic
    def graficarDos(self):
        self.graficarOde()
        self.graficarsAdamsBashforth()
        self.plot()






if __name__ == "__main__":

    c = Hodgkin()
    c.graficarDos()

    #c.mapalogistico()
    
    pass