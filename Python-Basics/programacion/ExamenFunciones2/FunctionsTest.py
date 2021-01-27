#Ejercicio 2
'''
Escribe una función que pasado como parámetro un vector que contiene
para un conjunto de vasos su cantidad de agua, devuelva cuanta agua tendremos que
vaciar en total para que todos los vasos queden igual de llenos que el que menos
agua contiene.
'''
from random import randint
waterIn = []
#vamos a pedir al usuario un numero de vasos a llenar, estos vasos se llenaran de agua de entre 5 y 250 ml
def vasos(max):
    for i in range(0,max):
        ml = randint(5, 250)
        waterIn.append(ml)
    return waterIn
        
nVasos = int(input("cuantos vasos deseas tener: "))
vec = (vasos(nVasos))
#ahora debemos ordenar este vector, nos interesa saber que vaso tiene la cantidad mas baja de liquido
def ordenaVector(vector):
    for i in range(1, len(vector)):
        for j in range(len(vector)-i):
            if vector[j]>vector[j+1]:
                temp = vector[j]
                vector[j] = vector[j+1]
                vector[j+1] = temp
    return vector
print("vector ordenado:{}".format(ordenaVector(vec)))
vector = ordenaVector(vec)
'''
ahora sabemos que el valor mas pequeño es el vector.[0], debemos comprara este valor con los demas que tienen mas cantidad
debemos saber que la diferencia de esa cantidad con la canidad del valor mas bajo nos dara lo que buscamos que es cuanto debemos quitar a ese vaso
para que quede una cantidad igual al que tiene menos liquido
ecuacion ==> z = (x-y) * -1 donde x = vector[0] / y = vector[0+1] / z = resta

'''
def total_resta(vector):
    resta = 0
    for i in range(1, len(vector)):
        resta += (vector[0] - vector[i]) * -1
    return resta
print(f"Valor mas pequeño en un vaso {vector[0]}, total a restar de los otros {total_resta(vector)}")

#ejercic 4
'''
Escribe una función recursiva y otra iterativa que calcule a**b, mediante
multiplicaciones sucesivas, siendo a y b números enteros. b puede ser negativa, y en
ese caso a**b = 1/ a**b
'''
#codigo iterativo
'''
a elevado a b es igual que multiplicar a*a el numero de veces de b
'''
a = int(input("introduce base a: "))
b = int(input("introduce exponente b: "))
def Ieterat(a,b):
    if b>0:
        suma = 1
        for i in range(b):
            suma *= a
        return suma
    elif b<0:
        b = -(b)
        suma = 1
        for i in range(b):
            suma *= a
            x = 1 / suma
            resul = 1 / x
        return resul
print(Ieterat(a,b))

#codigo recursivo
def recursivo(a,b):
    if b==0:
        return 1
    else:
        return a*expo(a,b-1)
def expoNeg(a,b):#si pasamos un valor de b negativo
    if b==0:#b<0 tenemos que llegar a 0 para que devuelva 1, para llegar a cero b+1
        return 1
    else:
        return a*expoNeg(a,b+1)#hasta que la b sea 0.
            
            
            
            

    
    
    
    
    
    
    
    
