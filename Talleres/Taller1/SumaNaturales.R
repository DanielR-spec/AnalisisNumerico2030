#Suma cuadrado

Sumar = function(n){
  while (n>0){
    SumSerie=SumSerie+n**2
    n = n-1
    i+1
    return(SumSerie)
  }
  
}
n = 5
SumSerie = 0
i = n
j = 0
SumResultado = 0
Conve <- seq(from=0, to=n-1)
while (n>0){
  Conve[n]<-Sumar(n)
  n = n-1
  i = i-1
}

SumResultado = sum(Conve)
write.csv(Conve, "Convern2.cvs")

