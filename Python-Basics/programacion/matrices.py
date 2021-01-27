"""
m=[]
m2=[]
filas=int(input("numeros de filas:"))
columnas=int(input("numero de columnas:"))
for i in range(filas):
    m.append([0]*columnas)
for f in range (filas):
    for c in range(columnas):
        m[f][c]=int(input(f"elemento {f},{c}:"))
print(m)

filas2=int(input("numeros de filas:"))
columnas2=int(input("numero de columnas:"))
for i in range(filas2):
    m.append([0]*columnas2)
for f2 in range (filas2):
    for c2 in range(columnas2):
        m[f2][c2]=int(input(f"elemento {f2},{c2}:"))
print(m2)
"""
matriz1=[]
filas=int(input("numeros de filas:"))
columnas=int(input("numeros de columnas:"))
for i in range(filas):
    matriz1.append([0]*columnas)
for f in range(filas):
    for c in range(columnas):
        matriz1[f][c]=int(input(f"elementos {f},{c}:"))
print(matriz1)
for i in range(filas):
    for j in range(columnas[i]-1):
        if (matriz1[i][j]<=matriz1[i][j+1]) and (matriz1[i][j]<=matriz1[i+1][j]):
            print("matriz creciente")
            break
        else:
            print("matriz no creciente")

        
