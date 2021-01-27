import math

class Punto:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y
 
    def __str__(self):
        return f'({self.x:.3f} , {self.y:.3f})'

#funciones
def lee_punto():
    return Punto(float (input ("coordenada x: ") ),float (input ("coordenada y: ") ) )#los puntos aqui introducidos seran los nuevos valores (x,y) de Punto

def escalar(punto,a):
    return Punto( punto.x * a , punto.y * a )

def despla(punto, punto2):
  return Punto( punto.x + punto2.x , punto.y + punto2.y )#ahora usamos las coordenadas x,y de los dos puntos.
    
#lo de rotar el punto no me ha salido. T-T </3


#iniciamos con un punto (0,0), lo cambiamos a otro (2,2) por ejemplo
punto1=Punto(2,2)#estos valores (2,2) estan como que simpre ya que estan asignados a Punto(x,y)
print(punto1)#lo imprimimos

punto2=lee_punto()
print(f"has introducido las coordenadas: {punto2}")

punto3=escalar(punto1,2)
punto3_2=escalar(punto2,2)
print(f"el escalar de {punto1.x},{punto1.y} tomando a=2 es: {punto3}")
print(f"el escalar de {punto2.x},{punto2.y} tomando a=2 es: {punto3_2}")

punto4=despla(punto1, punto2)
print(f"punto desplazado: {punto4}")
