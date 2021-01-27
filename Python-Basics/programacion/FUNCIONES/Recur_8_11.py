#Recursividad

"""
8.11 Programa una función recursiva y otra iterativa para calcular el máximo común divisor de dos
números enteros aplicando las siguientes propiedades recurrentes:
mcd(a , b) = mcd(a-b , b) si a > b
mcd(a , b) = mcd(a , b-a) si a < b
mcd(a , b) = a si a = b

El algoritmo de Euclides para encontrar MCD(A,B) es como sigue:

Si A = 0 entonces MCD(A,B)=B, ya que el MCD(0,B)=B, y podemos detenernos.  
Si B = 0 entonces MCD(A,B)=A, ya que el MCD(A,0)=A, y podemos detenernos.

Escribe A en la forma cociente y residuo (A = B ⋅Q + R).
Encuentra MCD(B,R) al usar el algoritmo de Euclides, ya que MCD(A,B) = MCD(B,R).

si queremos encontrar el mcd de (a,b) donde a!=0 y b!=0
ejemplo: mcd(15,4) si a>b hay que cambiarlos para que sea mas facil.
podemos escribir esto asi: 15/4=3 con resto 3 entonces ahora tenemos que calcular el mcd(4,3) osea mcd(b,r) hasta que en el resto sea 0
4/3= 1 con resto 1 ---- mcd(3,1)= 3/1=3 con resto 0 mcd(1,0)
el MCD(15,4)=1

"""
#Recursiva
def mcdRecursivo(a,b):
    if (a < b):
        return mcdRecursivo(b,a)
    elif (b==0):
        return a
    else:
        return mcdRecursivo(b,a%b)
            
a=int(input("valor a: "))
b=int(input("valor b: "))
print("el mcd entre a y b es: ", mcdRecursivo(a,b))
