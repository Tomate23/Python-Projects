                                                                                                                          #listas vectores
#fibonacci
def fib(n):
    a, b = 0,1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()
fib(1000)
#suma de listas.
v1=[1,2,3,4,5]
v2=[6,7,8,9,10]
vsuma=[]
for i in range(len(v1)):
    vsuma.append(v1[i]+v2[i])


#recorrer lista al reves
lista = [100, 200, 500, 2, 36]
longitud = len(lista)
for i in range(longitud):
      print(lista[longitud-i-1])
      
for i in range(longitud-1, -1, -1):
    print(lista[i])

#ordenar una lista de elementos
from random import randint
v=[]
for _ in range(0,15):
    num=randint(0,15)
    v.append(num)
    print(v)
    
for recorrido in range (1,len(v)):
    for posicion in range (len(v)-recorrido):
        if v[posicion]>v[posicion+1]:
            temp=v[posicion]
            v[posicion]=v[posicion+1]
            v[posicion+1]=temp
            
#freses de adelante hacia atras (palindromo)
frase = input('Introduce una frase: ')
frase2 = ''
for c in frase:
  frase2 = c + frase2

if frase == frase2:
  print('La frase es palindroma')
else:
  print('La frase no es palindroma')
  
#5.6 Crea un programa llamado ex_5_6, en el que el usuario introduzca una número y el programa
#genere una frase con las palabras correspondientes a cada cifra. Por ejemplo, 547 devolvería
#“cinco cuatro siete”.
letras=["cero","uno","dos","tres","cuatro","cinco","seis","siete","ocho","nueve"]
anw=[]
index=int(input("introduce un numero:"))
cifra1=index//100
cifra2=(index//10)%10
cifra3=index%10
print(letras[cifra1],letras[cifra2],letras[cifra3])
  
#matrices

#crear una matriz con valores que da el usuario
matriz1=[]
filas=int(input("numeros de filas:"))
columnas=int(input("numeros de columnas:"))
for i in range(filas):
    matriz1.append([0]*columnas)
for f in range(filas):
    for c in range(columnas):
        matriz1[f][c]=int(input(f"elementos {f},{c}:"))
print(matriz1)

"""
Para procesar una matriz bidimensional, normalmente utiliza bucles anidados.
El primer ciclo itera a través del número de fila, el segundo ciclo recorre los elementos dentro de una fila.
Por ejemplo, así es como se visualiza la lista numérica bidimensional en la pantalla línea por línea
separando los números con espacios:
"""
#recorrer matrices
a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=' ')
    print()
#suma se matrices
matriz1=[]
matriz2=[]
matrizResultado=[]
 
print("Matriz 3*3")
for a in range(3):
    matriz1.append([])
    matriz2.append([])
    matrizResultado.append([])
 
for a in range(3):
    for b in range(3):
        matriz1[a].append(input("Ingresar valor de la primera matriz: "))
 
for c in range(3):
    for d in range(3):
        matriz2[c].append(input("Ingresar valor de la segunda matriz: "))
 
for a in range(3):
    for b in range(3):
        matrizResultado[a].append( matriz1[a][b] + matriz2[a][b] )
 
print matriz1
print matriz2
print matrizResultado

#REGISTROS
#como crear un registro
class name:
    def __init__(self):
        self.variable1=""
        self.variable2=0
        self.variable3="eva"
        