"""
- Una función que lee un vector, y otra que lo imprime:
  pide_vector(vector[], longitud)
  imprime_vector(vector[])
"""
from lee_vector import pide_vector

n = int( input('¿Cuántos elementos? ') )

v = pide_vector(n)
print(f"vector es: {v} , y su longitud es: ",len(pide_vector(n)))
