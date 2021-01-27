# Ejercicio 5
'''
Escribe una función que calcule y retorne el punto medio de dos puntos
que recibe como parámetros, y otra función que imprime por pantalla el punto que
recibe como parámetro.
'''
class Punto:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0
# funcion para pedir las corrdenadas de los puntos
def lee_punto(clase):
    clase.x = int(input("valor de x:\t"))
    clase.y = int(input("valor de y:\t"))
    clase.z = int(input("valor de z:\t"))
    return f"punto: ({clase.x}, {clase.y}, {clase.z})"

# funcion para calcular el punto medio
def puntoM(p1, p2):
    puntoMedio = (p1.x + p2.x)/2, (p1.y + p2.y)/2, (p1.z + p2.z)/2
    return puntoMedio

p1 = Punto()
p2 = Punto()
print(lee_punto(p1))
print(lee_punto(p2))
print(f"Punto medio es:\t{puntoM(p1, p2)}")