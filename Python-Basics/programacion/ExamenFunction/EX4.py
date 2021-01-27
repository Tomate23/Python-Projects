# Ejercicio 4
'''
Escribe una función que recibe un vector
con los precios unitarios de una serie de productos comprados, y otro vector con la
cantidad de unidades compradas, y calcule y retorne el total a pagar por la compra
(“producto escalar de vectores”).
'''
# forma iterativa
v = [5,3,9,3,6]
w = [2,8,4,2,7]

def escalarIter(v, w):
    suma = 0
    for i in range(len(v)):
        producto = v[i] * w[i]
        suma += producto
    return suma
print(escalarIter(v, w))

#forma recursiva
def escalarRecur(v, w):
    if len(v) == 0:
        return 0
    else:
        return (v[0] * w[0]) + escalarRecur(v[1:], w[1:])
print(escalarRecur(v, w))