library (pracma)
library(readxl)
#Se buscan los datos de la base de Quixeramobim por lo cual la base más cercana es la de Quixada 
QuixadaDatos <- read_excel("D:/Documentos/Analisis numerico/Estudio/Reto2/punto 2/QuixadaDatos.xlsx")
QuixeramobimDatos <- read_excel("D:/Documentos/Analisis numerico/Estudio/Reto2/punto 2/QuixeramobimDatos.xlsx")
datosOriginales = QuixeramobimDatos$`Temp. Interna (ºC)`
datosTempqx = QuixadaDatos$`Temp. Interna (ºC)`
tam = length(datosTempqx)
porcentaje = length(datosTempqx)*0.8
toma = sort(sample(1:length(datosTempqx),porcentaje, replace = F))
datosTempqx = datosTempqx[toma]
#Se saca la interpolación de la muestra de Quixada y se aplica spline 
inter = spline(toma,datosTempqx,n=length(datosOriginales))
length(inter$y)
plot(1:length(datosOriginales),datosOriginales,type = "l")
lines(1:length(datosOriginales),inter$y,col="red")
legend(555,46, legend=c("Original", "Spline"),
       col=c("black", "red"),lty=1:2, cex=0.8)
#------------------------
c <- splinefun(toma, datosTempqx )
c<-c(1:tam)
plot(1:length(datosOriginales),datosOriginales,type = "l")
lines(1:length(datosOriginales),c,col="blue")
legend(555,46, legend=c("Original", "Splinefun"),
       col=c("black", "blue"), lty=1:2, cex=0.8)
#----------------
l<-approx(toma, datosTempqx, method = "linear", n=length(datosOriginales))
plot(1:length(datosOriginales),datosOriginales,type = "l")
lines(1:length(datosOriginales),l$y,col="green")
legend(555,46, legend=c("Original", "lineal"),
       col=c("black", "green"), lty=1:2, cex=0.8)
#Error
eSpline<- c()
ec <- c()
el <- c()

for(i in 1:tam){
  #error spline
  e = 0
  e = abs(datosOriginales[i]-inter$y[i])
  eSpline<- c(eSpline,e)
  #error de la costante
  e = 0
  e = abs(datosOriginales[i]-c[i])
  ec<- c(ec,e)
  #error lineal
  e = 0
  e = abs(datosOriginales[i]-l$y[i])
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
