m1=[[1,2,3],[3,2,1],[2,1,3]]
m2=[[7,8,6],[3,4,5],[1,7,5]]
m3=[]
filas=3
columnas=3
for i in range(filas):
    for j in range(columnas):
        m3[i][j]+=m1[i][j]+m2[i][j]
print(m3)
    
        