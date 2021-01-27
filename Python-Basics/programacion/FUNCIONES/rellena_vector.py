from random import randint#para generar los valores aleatorios.

def rellena_vector(n,min,max):#creamos la funcion, con el vector, el valor min y el vaor max
    for _ in range(min,max):
        num=randint(0,n)
        v.append(num)
    return(v)
v=[]
"""
min=int(input("introduce el min: "))
max=int(input("introduce el max: "))
"""
w=rellena_vector(15,0,3)
print(w)