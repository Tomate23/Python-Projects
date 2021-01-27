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
#w=rellena_vector(15,0,3)
#print(w)

def pide_vector(n2):
    for _ in range(n2):
        num=randint(0,15)
        v2.append(num)
    return(v2)
v2=[]
"""
n=int(input("cuantos elementos: "))
#max=int(input("introduce el max: "))
print(f"las longitud del vector es: ",pide_vector(min,n))
"""






#suma de vectores
def suma_vectores(v,w):
    for i in range(len(v)):
        vsuma.append(v[i]+w[i])
    return(vsuma)
vsuma=[]



#ordena vector
def ordena_vector(v):
    for recorrido in range(1,len(v)):
        for pos in range(len(v)-recorrido):
            if v[pos]>v[pos+1]:
                temp=v[pos]
                v[pos]=v[pos+1]
                v[pos+1]=temp
    return(v)
