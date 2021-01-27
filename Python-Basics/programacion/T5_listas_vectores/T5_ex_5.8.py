"""
5.8 Crea un programa llamado ex_5_8, que dado un vector de 15 elementos con valores aleatorios,
sea capaz de ordenar el vector y dar el resultado por pantalla.
"""
from random import randint
v=[]
for _ in range(0,15):
    num=randint(0,15)
    v.append(num)
    print(v)
"""
para ordenar los elementos de la lista, tenemos que comparar cada elemento y ver cual es mayor
"""
for recorrido in range (1,len(v)):#recorremos la lista a partir del primer elemento hasta la longitud de la lista 
    for posicion in range (len(v)-recorrido):
        if v[posicion]>v[posicion+1]:
            temp=v[posicion]
            v[posicion]=v[posicion+1]
            v[posicion+1]=temp
print(v)
    
    