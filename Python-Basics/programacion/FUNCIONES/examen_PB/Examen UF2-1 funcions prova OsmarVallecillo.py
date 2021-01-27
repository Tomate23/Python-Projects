#Ejercicio 1:
#Examen 1
def f(n):
    n=2
    print(j)
    i=4
n=4
i=2
j=1
f(5)
print(n)
print(i)

#¿Qué aparecerá por la pantalla al ejecutar el programa examen 1?
'''
1
4
2
'''

#Examen 2
def f(v,n):
    for i in range(0,n):
        v[i]=i
    n=0
    return 1
a=[4,5,6]
b=3
b=f(a,b)
print(a)
print(b)
#¿Qué aparecerá por la pantalla al ejecutar el programa examen 2?
'''
[0,1,2]
1
'''

#Ejercicio 2:
'''
escribe una funcion que pasado como parametro un vector que contiene para un conjunto de vasos su cantidad de agua tendremos que
vaciar en total para que todos los vasos queden igual de llenos que el que menos agua contiene
'''
#genero un vertor de 5 valores, que representan las cantidades (en ml) de los vasos
from random import randint
def total(vector):
    resta=0
    for i in range(1,len(vector)):
        if vector[0]<vector[i]:#restamos el valor mas pequeño con los demas, si es el mas pequeño la operacion dara como resultado un numero negativo.
            #lo que queremos es saber cuanto hay que quitar a los demas para hacer que valgan el valor del mas pequeño
            #podriamos decirlo como: cuanto le tengo que restar y para que me de x, pero ya sabemos x que es el valor mas pequeño.
            #resta=(x-y)/-1
            resta+=(vector[0]-vector[i])*-1
    return resta
cantidad=[]
for i in range(5):
    num=randint(5,250)
    cantidad.append(num)
print('vector desordenado: ',cantidad)
#primero deberiamos encontrar el valor mas pequeño dentro del vector para eso podemos ordenar el vector y coge el primer valor
for recorrido in range(1,len(cantidad)):
        for pos in range(len(cantidad)-recorrido):
            if cantidad[pos]>cantidad[pos+1]:
                temp=cantidad[pos]
                cantidad[pos]=cantidad[pos+1]
                cantidad[pos+1]=temp
print('vector oredenado: ',cantidad)
print(f"habria que quitar en total: {total(cantidad)} de los otros vasos para que queden al mismo valor de {cantidad[0]}")

#ejercicio 3:
'''
escribe la siguiente funcion recursiva:
Acker(m,n)=n+1 si m=0
Acker(m,n)=Acker(m-1,1) si n=0
Acker(m,n)=Acker(m-1, Acker(m,n-1)) en otro caso
Dibuja el arbol de llamadas recursivas para evaluar Acker(2,1). ¿Cuanto vale?
'''
def acker(m,n):
    if m==0:
        return (n+1)
    elif n==0:
        return acker(m-1,1)
    else:
        return acker(m-1,acker(m,n-1))
 
x=int(input("introduce valor:"))
print("m: ",x)
y=int(input("introduce valor:"))
print("n: ",y)
print("el valor segun la funcion recursiva acker es: ",acker(x,y))

print("valor para acker(2,1) es: ",acker(2,1))

'''
Acker(2,1) output
+++++++++++++++++
a(1,a(2,0))
a(1,1)
a(0,a(1,0))
a(0,1)
2
#no se como seguir los outputs

'''

#Ejercicio 4:
'''
funcion recursiva y iterativa para calcular a^b, mediante multiplicaciones sucesivas donde a y b son numeros enteros, el valor b puede ser negativo
en cuyo caso seria a^-b=1/a^b
'''

#codigo iterativo
a=int(input("introduce value for a: "))
b=int(input("introsduce value for b: "))
if b > 0:
    resul=1
    for i in range(0,b):
        resul*=a
    print("resultado de codigo iterativo de a^b: ",resul)
    
elif b < 0:
    #a^-b = 1/a^b
    resul=1
    b=-(b)
    for i in range(0,b):
        resul*=a
    x=1/resul
    exp=1/x
    print(f"el resultado es cuando b<0 usando codigo iterativo: {exp:.2f}")


#codigo recursivo ejercicio 4:

def expo(a,b):
    
    if b==0:
        return 1
    else:
        return a*expo(a,b-1)

def expoNeg(a,b):#si pasamos un valor de b negativo
    if b==0:#b<0 tenemos que llegar a 0 para que devuelva 1, para llegar a cero b+1
        return 1
    else:
        return a*expoNeg(a,b+1)#hasta que la b sea 0.
    
a2=int(input("introduce value for a: "))
b2=int(input("introduce value for b: "))
if b2<0:
    print("exponente con a^b<0 usando recursion: ",expoNeg(a2,b2))
else:
    print("exponente con a^b>0 usando recursion: ",expo(a2,b2))

#Ejercicio 5:
'''
funcion que sirva para leer por teclado las coordenadas de un punto, otra funcion que calcule y retorne la distancia al origen de un
punto que recibe como parametro
'''
from funcionesExamenEX5 import *
class punto:
    def __init__(self):
        self.x=0
        self.y=0
        self.z=0
p=punto()

lee_punto(p)

print("Distancia: ",distancia(p.x,p.y,p.z))





















