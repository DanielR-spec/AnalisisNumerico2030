library(pracma)
library(Rmpfr)
f = function(n){
  return(cos(1/n))
}
g =function(x){
  return(x^2-cos(x))
}
bits = 120

AITKEN = function(f,x0,tol){
  e = 1e10
  n = x0
  p= f(n)
  liste = c()
  iteraciones = 0
  valores = c() 
  while (e > tol) {
    n1 = n+1
    n2 = n+2
    p1 = f(n) - ((f(n1)-f(n))^2)/(f(n2)-2*f(n1)+f(n))
    e =  abs(p-p1)
    p = p1
    liste = c(liste,e)
    iteraciones = iteraciones +1
    valores =  c(valores,p)
    n = 1 +n
  }
  print(p)
  return (list(v = valores,e =  liste))
}
v = AITKEN(f=f ,x0 =1, tol = 1e-8)

n =  seq(1 , 6 , by = 1)
plot(n,f(n),col = 'blue', type = 'b',ylab = 'sucesión {x} ', main = 'Convergencia de cos(1/n)')
points(n,f(n),col = 'blue')
lines(n,v$v[1:6],col = 'red',type = 'b')
legend("bottomright",col=c("blue","red"),legend =c("Normal","Aitken"), lwd=3, bty = "n")

ev = f(n)
for (i in seq(1,6)){
  cat('Valor de la sucesion ',ev[i],'Co Aitken',v$v[i], " con n = ",i,'\n')
  
}
