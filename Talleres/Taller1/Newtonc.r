

#polinomio en una variable
polinomio = expression (exp(x) - x-1) 
#Al coger el polinomio le hicimos la derivada
derivada = D(polinomio, "x") 
#Variables
x = 0 ;
xaproximado = 0.000005
resultado = c(0)

i =1
#Inicio del while
while ( x != xaproximado) {
  
  x = xaproximado 
  reemplazarPoli = eval(polinomio)
  
  remplazarDeri = eval(derivada) 
  
  xaproximado = x - (reemplazarPoli/remplazarDeri) 
  resultado[i] =x
  i = i +1
}
#Grafica de la funcion

Polinom =function(x)(exp(x) - x-1)
curve(Polinom,-2,4,100, ylim = c(0,15),main = "Newton Cuadratico",col ="blue")

abline(0,0,col="red")

#Tabla

tabla = data.frame(resultado)
tabla
