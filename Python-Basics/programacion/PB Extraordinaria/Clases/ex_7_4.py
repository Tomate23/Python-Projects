class Punto:
  def __init__(self, param1, param2):
    self.x = param1
    self.y = param2

  def __str__(self):
    return '(' + str(self.x) + ' , ' + str(self.y) + ')'# esto es para luego imprimirlo y que no salga la definicion de clase



print('Cálculo de la media de una serie de puntos (0 0 para acabar)')
print('------------------------------------------------------------')

# Inicializamos las variables

suma = Punto(0,0)
p = Punto(0,0)
num = 0

# Leemos datos y los procesamos hasta que introducen 0 0

p.x = float( input('Introduce la coordenada x del punto : ') )
p.y = float( input('Introduce la coordenada y del punto : ') )
print()

while (p.x != 0) or (p.y != 0):
  suma.x = suma.x + p.x
  suma.y = suma.y + p.y
  num = num + 1
  p.x = float( input('Introduce la coordenada x del punto : ') )
  p.y = float( input('Introduce la coordenada y del punto : ') )
  print()

# Damos los resultados

if num != 0:
  suma.x = suma.x / num
  suma.y = suma.y / num
  print('La media de los puntos es:', suma)
else:
  print('No has introducido ningún punto')


