'''
Escribe una función recursiva y otra iterativa que calcule z × v, mediante
sumas sucesivas, siendo z y v números naturales.
'''
'''
z = 3
v = 4

#iterativo
def itera(z,v):
    suma = 0
    for i in range(v):
        suma += z
    return suma
print(itera(z,v))

#recursivo
def recur(z,v):
    if v == 0:
        return 0
    else:
        return z + recur(z, v-1)
print(recur(6,6))
'''
'''
Escribe una función que recibe un vector
con los precios unitarios de una serie de productos comprados, y otro vector con la
cantidad de unidades compradas, y calcule y retorne el total a pagar por la compra
(“producto escalar de vectores”).

v = [3,2,3]
w = [6,5,6]

def escalar(v,w):
    suma = 0
    for i in range(len(v)):
        producto = v[i]*w[i]
        suma += producto
    return suma

print(escalar(v,w))

class punto1:
    def __init__(self):
        self.x=0
        self.y=0
        self.z=0
        
class punto2:
    def __init__(self):
        self.x=0
        self.y=0
        self.z=0

def lee_punto(clase):
    #lo que tenemos que leer son las coordenada x,y,z de la clase
    clase.x=int(input("introduce un valor para x: "))
    clase.y=int(input("introduce un valor para y: "))
    clase.z=int(input("introduce un valor para z: "))
    print(f"punto: {clase.x}, {clase.y}, {clase.z}")
def puntoMedio(p1, p2):
    coor1 = (p1.x + p2.x) / 2
    coor2 = (p1.y + p2.y) / 2
    coor3 = (p1.z + p2.z) / 2
    print(f"punto medio: {coor1}, {coor2}, {coor3}")

p1 = punto1()
p2 = punto2()

lee_punto(p1)
lee_punto(p2)

puntoMedio(p1, p2)

def T(n,x):
    if n == 0:
        return 1
    if n == 1:
        return x
    return 2*x*T(n-1, x) - T(n-2,x)

print(T(4,2))

v = [4,8,3]
w = [6,2,8]

def vecRecur(v, w):
    suma = 0
    if len(v)==0:
        return 0
    else:
        v1 = v[1:]
        v2 = w[1:]
        suma += v1 * v2
        return vecRecur(v, w)
    return suma
print(vecRecur(v, w))
'''
v = [1,5,3,7,8]
long = len(v)

for i in range(long-1):
    print(v[i])













        

