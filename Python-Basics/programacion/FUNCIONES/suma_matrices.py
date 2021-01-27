
m1=[]
m2=[]
msuma=[]

filas=int(input("introduce el numero de filas: "))
colum=int(input("introduce el numero de columnas: "))

for i in range(filas):
    m1.append([0]*colum)
    msuma.append([0]*colum)
    
for i in range(filas):
    for j in range(colum):
        m1[i][j]=int(input(f"introduce el valor {i},{j} :"))
print(m1)
    
filas2=int(input("introduce el numero de filas: "))
colum2=int(input("introduce el numero de columnas: "))

for i in range(filas2):
    m2.append([0]*colum2)
    
for i in range(filas2):
    for j in range(colum2):
        m2[i][j]=int(input(f"introduce el valor {i},{j} :"))
print(m2)

for i in range(filas):
    for j in range(colum):
        msuma[i][j]=(m1[i][j]+m2[i][j])
print(msuma)
"""
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
 
print (matriz1)
print (matriz2)
print (matrizResultado)
"""
