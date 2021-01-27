# Ejercicio 1: Observa los siguientes programas:
# a) ¿Qué aparecerá por pantalla al ejecutar el programa examen1 ?

def f(n):
    global i
    n = 2
    i = 3
    print(i)# imprime 3, i = 3

n = 4
i = 2
f(5)
print(n)
print(i)

# output
# 3 => se imprime por la llamada de la función f(5)
# 4 => se imprime por, print(n) donde n =4 
# 3 => se imprime el 3, ya que es la variable global, no se imprime 2 porque llamamos a la funcion f(n) despues de declarar i = 2
          #si pusieramos el i = 2 despues de llamar a la funcion se imprimiria i = 2

# b) ¿Qué aparecerá por pantalla al ejecutar el programa examen2 ?

def f(v):
    for i in range(len(v)):
        v[i] = 0# convertira todos los valores del vector en 0
        
a = [4, 5, 6]
b = a# b = [4, 5, 6]
f(b)
print(a)
print(b)
# ya que a = b, y el vector b al ser nviado a la funcion todos sus valores se vuelven 0 entonces el vector a tambien.

# output
# >>> [0, 0, 0]
# >>> [0, 0, 0]