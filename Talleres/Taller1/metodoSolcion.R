
library(pracma)
f =  function(x){
  
  return(3*sin(x)^3 - -1)
}

g = function(x){
  return(4*sin(x)*cos(x))
}

p = function(x){
  
  return( f(x) - g(x))
}

x =  seq(-10,10, by =(0.05))

plot(x,p(x), type = 'l',xlim = c(-5,5))
plot(x ,f(x), col = "red",type = 'l',xlim = c(-5,5), main = "Puntos de union entre f(t) y g(t)")
lines(x,g(x),col= "blue")

legend("topright",col=c("red","blue"),legend =c("f(x)"," g(t)"), lwd=1, bty = "n")
abline(h = 0 ,v = 0)
r = newton(p,x0= 0,maxiter = 300,tol= 1e-16)
cat("El valor de x es ",r$root,"\n","el valor de  f(x):",f(r$root),'\n',"el valor de  g(x):",g(r$root))

