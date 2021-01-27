#8.5 Observa el siguiente programa:
"""
Crea la biblioteca vectores.py que contenga el código de las siguientes funciones:

"""
from vectores import rellena_vector
from vectores import pide_vector
from vectores import suma_vectores
from vectores import ordena_vector
n = int( input('¿Cuántos elementos? ') )
"""
- Una función que inicializa con valores aleatorios los elementos de un vector:
rellena_vector(vector[], longitud, min, max)
"""
w = rellena_vector(n, -10, 10)
print("\n")
print(w)
print("\n")
print("****************************************************************************")

"""
- Una función que lee un vector, y otra que lo imprime:
  pide_vector(vector[], longitud)
  imprime_vector(vector[])
"""

n2 = int( input('¿Cuántos elementos? ') )

v = pide_vector(n2)
print(f"vector es: {v} , y su longitud es: ",len(v))



suma = suma_vectores(v, w)
print(f"la el resultado de la suma de los vectores {v} y {w} es: {suma}")



#ordenar vector

ordenadov=ordena_vector(v)
ordenadow=ordena_vector(w)
#print(f"vector desordenado: {no_ordenado}")
print(F"vector v ordenado: {ordenadov}")
print(F"vector w ordenado: {ordenadow}")







