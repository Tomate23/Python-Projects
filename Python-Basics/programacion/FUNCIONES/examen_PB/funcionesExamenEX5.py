import math
def lee_punto(clase):
    #lo que tenemos que leer son las coordenada x,y,z de la clase
    clase.x=int(input("introduce un valor para x: "))
    clase.y=int(input("introduce un valor para y: "))
    clase.z=int(input("introduce un valor para z: "))
    
def distancia(x,y,z):
    dist=math.sqrt((x**2+y**2+z**2))
    return dist
    