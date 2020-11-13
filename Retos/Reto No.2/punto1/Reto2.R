library(readr)
library(PolynomF)
library(pracma)
library(readr)

#datos de fortaleza
fortaleza <- read.csv("D:/Documentos/Analisis numerico/Estudio/Reto2/punto 1/Reto21.csv")
humedad <-fortaleza$Umidade.Relativa.do.Ar.2m....

tam<-length(humedad)
por<-tam*0.8
sorteado<-sort(sample(1:tam,por, replace = F))
faltantes<-1:tam
faltantes <- faltantes[-sorteado]
plot(1:tam, humedad , type="l",xlab = "numeracion de dias",ylab = "Humedad relativa",main = "Humedad ")
datos<-humedad[sorteado]

#interpolacion por spline
spli<-spline(1:por, datos, n=tam)
print(spli)
length(spli$y)
plot(1:tam, humedad , type="l",xlab = "numeracion de dias",ylab = "Humedad relativa",main = "Humedad ")
lines(1:tam, spli$y, col="red")
legend(630, 60, legend=c("Original", "Spline"),
       col=c("black", "red"), lty=1:2, cex=0.8)
#interpolacion 
c <- splinefun(sorteado, datos )
c<-c(1:tam)
#c<-approx(1:por, datos, method = "constant", n=tam)
l <-approx(1:por, datos, method = "linear", n=tam)
plot(1:tam, humedad , type="l",xlab = "numeracion de dias",ylab = "Humedad relativa",main = "Humedad ")
lines(1:tam, c, col="blue")
legend(630, 60, legend=c("Original", "Splinefun"),
       col=c("black", "blue"), lty=1:2, cex=0.8)
plot(1:tam, humedad , type="l",xlab = "numeracion de dias",ylab = "Humedad relativa",main = "Humedad ")
lines(1:tam, l$y, col="green")
legend(630, 60, legend=c("Original", "lineal"),
       col=c("black", "green"), lty=1:2, cex=0.8)

#Error
eSpline<- c()
ec <- c()
el <- c()

for(i in 1:tam){
  #error spline
  e = 0
  e = abs(humedad[i]-spli$y[i])
  eSpline<- c(eSpline,e)
  #error de la costante
  e = 0
  e = abs(humedad[i]-c[i])
  ec<- c(ec,e)
  #error lineal
  e = 0
  e = abs(humedad[i]-l$y[i])
  el<- c(el,e)
  
} 
emcS = sqrt( (sum(eSpline^2))/tam)
emcC = sqrt( (sum(ec^2))/tam)
emcL = sqrt( (sum(el^2))/tam)
cat("error EMC del spline ",emcS,'\n')
cat("error medio del spline ",(sum(eSpline))/tam,'\n')
cat("error minimo  del spline ",min(eSpline),'\n')
cat("error maximo  del spline ",max(eSpline),'\n')
(1 - (sum(eSpline)/sum(datosOriginales)))*100
#-----------
cat("error EMC del hermite ",emcC,'\n')
cat("error medio del hermite ",(sum(ec))/tam,'\n')
cat("error minimo  del hermite ",min(ec),'\n')
cat("error maximo  del hermite ",max(ec),'\n')
(1 - (sum(ec)/sum(datosOriginales)))*100
#-----------
cat("error EMC del lineal ",emcL,'\n')
cat("error medio del lineal ",(sum(el))/tam,'\n')
cat("error minimo  del lineal ",min(el),'\n')
cat("error maximo  del lineal ",max(el),'\n')
(1 - (sum(el)/sum(datosOriginales)))*100
