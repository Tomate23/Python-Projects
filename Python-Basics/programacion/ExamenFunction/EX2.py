# ejercicio 2
'''
Escribe una función recursiva y otra iterativa que calcule z × v, mediante sumas sucesivas, siendo z y v números naturales.

'''
# codigo iterativo
z = int(input("introduce valor de z:\t"))
v = int(input("introduce valor de v:\t"))

def itera(z, v):
    suma = 0
    for i in range(v):
        suma += z
    return suma
print(f"con codigo iterativo: {itera(z, v)}")

# codigo recursivo
def recur(z, v):
    if v == 0:
        return 0
    else:
        return z + recur(z, v-1)
print(f"con codigo recursivo: {recur(z, v)}")