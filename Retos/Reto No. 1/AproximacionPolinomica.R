#Desarrollado por Julian Builes,Santiago Bermudez, Daniel Reyes y Daniel Fierro
#Instalar Pracma
library(pracma)
library(MASS)
library(signal)
library(Rmpfr)
bits = 128
# -------------------------------------------------------------------------------------
#     Evaluar en Taylor
#     Para este punto se hizo uso de la funcion Taylor en la libreria Pracma
#     para asi poder obtener el polinomio de taylor y luego esta la funcion 
#     evaluarla dentro de los intervalos 
#          
# -------------------------------------------------------------------------------------
#Polinomio de Taylor
f = function(x)
{
  return (exp(sin(x)-sin(x)^2))
  #return(sin(x))
}

polinomioCalculado = mpfr(taylor(f,0,3),bits)

inicio = mpfr( -2^(-8),bits)
final = mpfr(2^(-8),bits)
s = seq( inicio,final,0.0005 )
error = c()
for (i in seq(length(s))){
cat("Numero Evaluado en la funcion y el polinomio ")
  print(s[i])
  r =horner(p = polinomioCalculado, s[i])
  cat("el valor con taylor es\t")
  print(r$y)
  plot(asNumeric(r$y),s[i],type='p',col = 'red')
  x = mpfr(f(s[i]),bits)
  cat("el valor esperado es ")
  print(x)
  print('------------------------------------')
  error <- c(error,abs(x-r$y))
} 
# Evaluar Ramez con la fuuncion que usa los numeros de cehvicev y da una aproximacion 
# al poliomio
ramez = polyApprox(f = f, a = -2^(-8),b = 2^(-8),n = 3)
error2 <- c()
for(i in seq(length(s))){
  cat("Numero Evaluado en la funcion y el polinomio ")
  print(s[i])
  r =horner(p = ramez$p, s[i])
  cat("el valor con taylor es\t")
  print(r$y)
  plot(asNumeric(r$y),s[i],type='p',col = 'red')
  x = mpfr(f(s[i]),bits)
  cat("el valor esperado es ")
  print(x)
  print('------------------------------------')
  error2 <- c(error,abs(x-r$y))
}
