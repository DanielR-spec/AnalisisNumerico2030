library(pracma)
library(Rmpfr)
f = function(n){
  return(cos(1/n))
}

g =function(x){
  return(x^2-cos(x))
}
bits = 120
aitken( f = f,nmax = 10,tol = 1e-8, x0=1)
AITKEN = function(f,x0,tol,maxit){
  e = 1e10
  n = x0
  p= f(n)
  liste = c()
  valores = c() 
  i =0
  while (e > tol) {
    n1 = mpfr(f(n),bits)
    n2 = mpfr(f(n1),bits)
    p1 = f(n) - ((f(n1)-f(n))^2)/(f(n2)-2*f(n1)+f(n))
    e =  abs(p-p1)
    p = p1
    liste = c(liste,toNum(e))
    valores =  c(valores,toNum(p))
    n = p1
    i = i+ 1
    if(i == maxit){
      print(i)
      print("numero de iteraciones superado")
      return (list(lval = valores,ler =  liste, i = i))
      
    }
  }
  print(i)
  return (list(v = p,lval = valores,ler =  liste, i = i))
}
Steffensen = function(f,p0,tol){
  i = 0
  e = 150000
  lerrores = c()
  lval = c()
  while ( e > tol ) {
    p1 = mpfr(f(p0),bits)
    p2 = mpfr(f(p1),bits)
    p = p0 -((p1-p0)^2)/(p2-2*p1+p0)
    e = abs(p-p0)
    lerrores = c(lerrores,toNum(e))
    i = i + 1
    p0 = p
    lval = c(lval,toNum(p0))
    #cat("p ",p1," e",e ,"\n")
  }
  print(i)
  return(list(v = p,lval = lval, ler=lerrores , i = i))
}
s =Steffensen(f = g, p0 = 0.5,tol = 1e-8)
a = AITKEN(f = g, x0 = 1,tol = 1e-8,maxit = 30)
##aitken(f =g ,x0 = 1 ,tol = 1e-8)
#x = seq(1,10,by = 1)
#plot(x,g(x),type = 'l')

plot(a$ler,a$lval, col= 'red', type = 'b',xlim = c(0,1), main = 'Error vs Valor',xlab = 'Error',ylab = 'valores')
lines(s$ler,s$lval, col = 'blue', type = 'b')
legend("bottomright",col=c("red","blue"),legend =c("Aitken","Steffensen"), lwd=3, bty = "n")
z = Steffensen(f = g, p0 = 0.5,tol = 1e-16)
c = AITKEN(f = g, x0 = 1,tol = 1e-16,maxit = 30)


cat('Tolerancia de  10-8\nAitken\n Iteraciones : ',a$i,'\n')
print(a$v)
cat('Steffensem \nIteraciones : ',s$i,'\n')
print(s$v)

cat('Tolerancia de  10-16\nAitken\n Iteraciones : ',c$i,'\n')
print(c$v)
cat('Steffensem \nIteraciones : ',z$i,'\n')
print(z$v)
