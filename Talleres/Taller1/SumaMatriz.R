
n = 5;
minN = 1;
maxN = 100;

A="Matriz cuadrada An con n = 3"
Matrx <- matrix(1:9,3,3)

Convergencia <- matriz(Matrx, 3)
matriz <- function(An, x0)
{
  An<-Matrx
  Sup <- An
  SumMatSup <- An
  SumMatInf <- An
  matrioSup <- An
  ValorInicial = 2
  
  
  Sup[lower.tri(Sup,diag = FALSE)]<-0
  matrizInf <- Sup
  SumMatSup[lower.tri(Sup,diag = TRUE)]<-0
  matrizSumaSup <- SumMatSup
  
  matrioSup[upper.tri(An,diag = FALSE)]<-0
  matrizSup<- matrioSup
  SumMatInf[upper.tri(An,diag = TRUE)]<-0
  matrizSumaInf <- SumMatInf
  
  SumSup = sum(matrizSumaSup)
  SumInf = sum(matrizSumaInf)
  n = 1
  
  MxmasNx<-matrizInf+matrizSup
  MatrizOrg<-Matrx
  while (n<nrow(An)){
    
    #B + Nx
    
    B<-(Matrx[n]*x0)**n
    BmasNx<-B+matrizInf
    
    a <-det(matrizSup)
    #M-1*Mx
    Minverso <- solve(matrizSup)
    MmenosunoporMx <- matrix(0:0,3,3)
    MmenosunoporMx <- Minverso*matrizSup
    
    #M-1*(B+Nx)
    MmenosunoporBmasNx <- matrix(0:0,3,3)
    MmenosunoporBmasNx <- Minverso*BmasNx
    
    x<-n
    n = n+1
    
    f <- c(MmenosunoporBmasNx)
    return(f)
  }
}


write.csv(Convergencia, "conver.cvs")
