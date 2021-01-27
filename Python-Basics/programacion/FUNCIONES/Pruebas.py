"""
#Fibonacci
def Fibonacci(n):
    a,b = 0,1
    while a < n:
        print(a, end=" ")
        a,b = b,a+b
    print()
Fibonacci(50)

#suma de vectores
v1 = [1,2,3]
v2 = [4,5,6]
v3 = []
for i in range(len(v1)):
    v3.append(v1[i]+v2[i])
print(v3)

#vectores al reves
lista = [1,2,3,4,5]
listaRever = []
long = len(lista)
for i in range(long):
    listaRever.append(lista[long-i-1])
print(listaRever)

#metodo 2
for i in range(long-1,-1,-1):
    listaRever.append(lista[i])
print(listaRever)

#ordenar vector
v = [2,6,9,3,6]
for recorrido in range(1,len(v)):
    for posicion in range(len(v)-recorrido):
        if v[posicion]>v[posicion+1]:
            temp = v[posicion]
            v[posicion]=v[posicion+1]
            v[posicion+1]=temp
print(v)

#crear una matriz con valores que da el usuario
filas = int(input('Numero de filas:')
columnas = int(input('Numero de columnas:')
matrix = []
for i in range(filas):
    matrix.append([0]*columnas)
for f in range(filas):
    for c in range(columnas):
        matrix[f][c] = int(input(f"elementos {f},{c}:"))
print(matrix)

matriz1=[]
filas=int(input("numeros de filas:"))
columnas=int(input("numeros de columnas:"))
for i in range(filas):
    matriz1.append([0]*columnas)
for f in range(filas):
    for c in range(columnas):
        matriz1[f][c]=int(input(f"elementos {f},{c}:"))
print(matriz1)
a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=' ')
    print()

lista = [1,2,3,4,5]
listaRever = []
long = len(lista)
for i in range(long-1,1,-1):
    listaRever.append(lista[i])
print(listaRever)

# suma de matrices 3x3
m1 = []
m2 = []
ms = []

# pedimos las dimensiones de la matriz
filas = int(input("Numero de filas:\t"))
columnas = int(input("Numero de columnas:\t"))

# creamos las matrices con las dimensiones insertadas
for i in range(filas):
    m1.append([0]*columnas)
    m2.append([0]*columnas)
    ms.append([0]*columnas)

# pedimos los valores de las matriz, m1
for f in range(filas):
    for c in range(columnas):
        m1[f][c] = int(input(f"Matriz 1 valor {f},{c}:\t"))
        
        
# pedimos los valores de las matriz, m2
for f in range(filas):
    for c in range(columnas):
        m2[f][c] = int(input(f"Matriz 2 valor {f},{c}:\t"))
        
        
print(f"Matriz 1 :\t\n {m1}")
print(f"Matriz 2 :\t\n {m2}")

#sumamos las matrices
for i in range(filas):
    for j in range(columnas):
        ms[i][j] = (m1[i][j] + m2[i][j])
print(f"suma de las dos matrices:\n {ms}")

# Ordenamiento por insercion
v = [8,4,2,8,5,6,3,4]

for index in range(1, len(v)):
    valor = v[index]
    i = index - 1
    while i >= 0:
        if valor < v[i]:
            v[i+1] = v[i]
            
            v[i] = valor
            i = i - 1
        else:
            break
print(v)
"""
"""

  *
 ***
*****
def triangle(n):
    k = 2 * n -2
    for i in range(0, n):
        for j in range(0, k):
            print(end="")
        k = k-1
        for j in range (0, i+1):
            print('*', end="")
        print("\r")
triangle(5)

n = int(input("introduce un numero para hacer la piramide:\n"))
for i in range(n+1):
    print('*' * i, end="\n")
print("\t")
"""
# pedimos las dimensiones de la mtriz
filas = int(input("introduce el numero de filas:\t"))
columnas = int(input("introduce el numero de columnas:\t"))

matriz_1 = []
matriz_2 = []
matriz_suma = []


# creamos la matriz con elemetos [0]
for i in range(filas):
    matriz_1.append([0]*columnas)
    matriz_2.append([0]*columnas)
    matriz_suma.append([0]*columnas)

# pedimos los elementos de las matrices a sumar mtariz_1 y matriz_2
for f in range(filas):
    for c in range(columnas):
        matriz_1[f][c] = int(input(f"Matriz 1, elemeto: {f},{c}:\t"))
    

for f in range(filas):
    for c in range(columnas):
        matriz_2[f][c] = int(input(f"Matriz 2, elemeto: {f},{c}:\t"))

# sumamos las matrices
for i in range(filas):
    for j in range(columnas):
        matriz_suma[i][j] = (matriz_1[i][j] + matriz_2[i][j])
        
print(f"matriz 1: {matriz_1}")
print(f"matriz 2: {matriz_2}\n")
print(f"Las suma de las matrices es: {matriz_suma}")
    
    
    
    
    
    
    





