
f = function(x){log(x+2)}
g = function(x){sin(x)}
Tolerancia = 0.00000001
q = function(x){log(x+2)-sin(x)}
Teorico = uniroot(q, c(-1.8,-1), tol = 1e-9) 


#grafica funcion f
plot(f, xlim = c(-4,4), ylim=c(-4,4), ylab = "f(x)", col = "green")
par(new = TRUE)
#grafica funcion g
plot(g, xlim = c(-4,4), ylim=c(-4,4), ylab = "g(x)", col = "blue")
plot(q, xlim = c(-4,4), ylim=c(-4,4), ylab = "f(x) - g(x)", col = "red")
par(new = TRUE)
#grafica donde la funcion q intercepta con x = 0
abline(0,0, col = "green")

#Variables
a = -1.9
b = -1
arr = c(0)
arr[1] = a
arr[2] = b
i=3
errorRec1 = c() 
errorRecSig = c()

#Inicio del while
while(abs(Teorico$root-arr[i-2]) > Tolerancia){
  errorRec1[i-2]=abs(Teorico$root-arr[i-2])
  arr[i]= arr[i-1]-((q(arr[i-1])*(arr[i-1]-arr[i-2]))/(q(arr[i-1])-q(arr[i-2])))
  i = i+1
}

i=1
while(i<length(errorRec1)+1){
  errorRecSig[i]=errorRec1[i+1]
  i = i+1
}
plot(errorRec1,errorRecSig, type="l")

numero_iteraciones = length(arr)

Metodo2 = c(0)
errorIt = c(0)
errorItsig = c(0)
Metodo2[1] = a
Metodo2[2] = b
i=3

while(abs(Teorico$root-Metodo2[i-2]) > Tolerancia){
  errorIt[i-2]=abs(Teorico$root-arr[i-2])
  Metodo2[i]= Metodo2[i-1]-((q(Metodo2[i-1]))*(Metodo2[i-1]-Metodo2[i-2])/(q(Metodo2[i-1])-q(Metodo2[i-2])))
  i = i+1
}

i=1
while(i<length(errorIt)+1){
  errorItsig[i]=errorIt[i+1]
  i = i+1
}

plot(errorIt,errorItsig, type ="l",col ="blue")

tabla = data.frame(errorRec1,errorRecSig,errorIt,errorItsig)
tabla


