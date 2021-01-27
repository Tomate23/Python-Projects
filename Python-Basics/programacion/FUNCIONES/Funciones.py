#8.3 Escribe los subprogramas o funciones correspondientes a las siguientes especificaciones:
"""
a) Un subprograma tal que, dados dos reales a y b, calcula el logaritmo en base b de a según la
siguiente fórmula: logba = (log a) / (log b).

import math

def logaritmo(a,b):
    calculo=(math.log(a,b))
    return calculo

a=int(input("valor de a: "))
b=int(input("valor de b: "))
print(logaritmo(a,b))


b) Un subprograma tal que, dado un número real, calcula el signo del número y devuelva -1, 0
ó 1 según si el número es negativo, cero o positivo.

def numero(n1):
    if n1<0:
        return "el numero es negativo {n1}"
    elif n1==0:
        return "el numero es cero"
    elif n1>0:
        return "el numero es positivo"
n1=int(input("dame un numero: "))
print(numero(n1))


c) Un subprograma tal que, dado un carácter, calcule si el carácter en cuestión es una letra o no.


def letra(a):
    abc=["a","b","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    letra=0
    for i in abc:
        if i==a:
            letra=1
    if letra==1:
        return "el caracter introducido es una letra"
    else:
        return "este caracter no es una letra"

a=input("introduce un caracter: ")

print(letra(a))

e) Un subprograma tal que, dados dos números reales, retorna un dato leído por teclado que se
encuentra dentro de los límites marcados por dichos valores. Si el número introducido no está
entre el mínimo y máximo marcado por los parámetros, debe continuar pidiéndolo.

def bucle(min,max):
    while True:
        valor=int(input("introduce un valor: "))
        if valor>=min and valor<=max:
            return valor
min=int(input("introduce el min: "))
max=int(input("introduce el max: "))
#valor=int(input("introduce un valor: "))
print(bucle(min,max))


f) Un subprograma tal que, dados dos vectores retorna el vector resultante de sumar los dos
anteriores, o lanza una excepción en caso de que no sean del mismo tamaño.

vec1=[1,2,3,4]
vec2=[5,6,7,8]
resul=[]

def suma_vec(resul):
    
    for i in range(len(vec1)):
        resul.append(vec1[i]+vec2[i])
        
    return resul
        
print(suma_vec(resul))


g) Un subprograma tal que, dada una matriz 3×3, retorna el valor de su determinante según la
regla de Sarrus:
"""
matriz=[]
filas=int(input("introduce el numero de filas: "))
column=int(input("introduce el numero de columnas: "))

def crea_matrix(matriz):
    for i in range(filas):
        matriz.append([0]*column)
    for f in range(filas):
        for c in range(column):
            matriz[f][c]=int(input(f"introduce el elemento {f},{c} de la matriz: "))
    return matriz
print(crea_matrix(matriz))

det=0#preguntar porque hay que declarar
def determinante(det):
    part1=(matriz[0][0]+matriz[1][1]+matriz[2][2])+(matriz[0][1]+matriz[1][2]+matriz[2][0])+(matriz[1][0]+matriz[2][1]+matriz[0][2])
    part2=(matriz[0][2]+matriz[1][1]+matriz[2][0])+(matriz[1][0]+matriz[0][1]+matriz[2][2])+(matriz[2][1]+matriz[1][2]+matriz[0][0])
    deter=part1-part2
    return deter
print("el determinante es: ", determinante(det))

        
    















