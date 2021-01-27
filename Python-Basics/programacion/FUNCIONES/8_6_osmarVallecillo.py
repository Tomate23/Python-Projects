"""
8.6 Crea un programa llamado ex_8_6, que contenga el código de las siguientes funciones para
trabajar con puntos del espacio bidimensional definidos por el tipo de datos:
"""
import math
class Punto:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y
p1=Punto()
# Una función que lee un punto por teclado, y otra función que lo imprime en pantalla.
def lee_punto():
    p1.x=int(input("introduce la coordenada x: "))
    p1.y=int(input("introduce la coordenada y: "))
    return(p1.x,p1.y)


def imprime_punto():
    print(lee_punto())
imprime_punto()


# Una función que transforma un punto (x, y) en otro (a·x, a·y), donde a es un número real que
#indica el factor de escala.

def escalar(a):
    escx=p1.x*a
    escy=p1.y*a
    return(escx,escy)

a=int(input("introduce el valor de a: "))
escalar_punto=escalar(a)
print(f"el escalar del punto {p1.x},{p1.y} es: {escalar_punto}")


#Una función que desplaza un punto (x, y) hacia (x+a, y+b), donde (a, b) es otro punto que
#indica el desplazamiento.

class punto2:
    def __init__(self):
        self.a=0
        self.b=0
p2=punto2()

def desplaza(a,b):
    desx=p1.x+p2.a
    desy=p1.y+p2.b
    return(desx,desy)
p2.a=int(input("valor de coordenada a: "))
p2.b=int(input("valor de coordenada b: "))

a=p2.a
b=p2.b

desplazamiento=desplaza(a,b)
print(f"punto desplazado: {desplaza(a,b)}")

#Una función que rota un punto (x, y) hasta (x·cos θ − y·sin θ, x·sin θ + y·cos θ), donde θ es un
#número real que indica el ángulo en radianes.
def rotar(numR):
    rotax=p1.x*math.cos(numR)-p1.y*math.sin(numR)
    rotay=p1.x*math.sin(numR)+p1.y*math.sin(numR)
    return(rotax,rotay)
numR=int(input("angulo en radianes: "))
rotacion=rotar(numR)
print(f"el resultado de rotar el punto {p1.x} , {p1.y} es: {rotar(numR)} ")
