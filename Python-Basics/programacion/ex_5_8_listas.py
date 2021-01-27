"""
5.8 Crea un programa llamado ex_5_8, que dado un vector de 15 elementos con valores aleatorios,
sea capaz de ordenar el vector y dar el resultado por pantalla.
"""
import random
v1=[]
i=0
for x in range(5):
    numeros=random.randint(0,15)
    v1.append(numeros)
#print(f"vector desordenado: {v1}")

#longitud=len(v1)
for recorrido in range(1,len(v1)):
    for posicion in range(len(v1)-recorrido):
        if v1[posicion]>v1[posicion+1]:
            temp=v1[posicion]
            v1[posicion]=v1[posicion+1]
            v1[posicion+1]=temp
print(f"vector ordenado: {v1}")
            
            
            
            
            
            
        
    
    
    