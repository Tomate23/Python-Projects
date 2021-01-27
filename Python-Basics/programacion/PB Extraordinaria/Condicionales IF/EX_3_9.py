# Pedimos el primer punto
ax = float( input('Introduce la coordenada x del primer punto: ') )
ay = float( input('Introduce la coordenada y del primer punto: ') )

# Pedimos el segundo punto
bx = float( input('Introduce la coordenada x del segundo punto: ') )
by = float( input('Introduce la coordenada y del segundo punto: ') )

# Calculamos el punto medio
mx = (ax + bx) / 2
my = (ay + by) / 2

# Damos los resultados
print('El punto medio es (', mx, ',', my, ')')

# Comprobamos y mostramos el cuadrante del punto resultante
if mx > 0:
  if my > 0:
    print('1er. cuadrante')
  elif my < 0:
    print('4o. cuadrante')
  else:
    print('Sobre el eje X')
elif mx < 0:
  if my > 0:
    print('2o. cuadrante')
  elif my < 0:
    print('3er. cuadrante')
  else:
    print('Sobre el eje X')
else:
  if my != 0:
    print('Sobre el eje Y')
  else:
    print('Origen de coordenadas')