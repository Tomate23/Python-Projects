'''
Sean A, B y C tres variables enteras que representan las ventas de tres productos A, B y C,
respectivamente. Utilizando dichas variables, escribe las expresiones que representen cada una
de las siguientes afirmaciones:
'''
from random import randint
A = randint(0, 1000)
B = randint(0, 1000)
C = randint(0, 1000)

# calculo de la media
media = (A+B+C) / 3

# total de ventas
totalV = A+B+C

# a) Las ventas del producto A son las más elevadas.
if A > B or A>C:
    print("Las ventas de A son las mas elevadas", end="")
# b) Ningún producto tiene unas ventas inferiores a 200.
elif A<200 or B<200 or C<200:
    print("Alguna de las ventas es inferior a 200", end="")
# c) Algún producto tiene unas ventas superiores a 400.
elif A>200 or B>200 or C>200:
     print("Alguna de las ventas es superior a 200", end="")
# d) La media de ventas es superior a 500.
elif media>500:
    print(f"La media es superior a 500 media: {media}", end="")
# e) El producto B no es el más vendido.
elif B<A or B<C:
    print(f"B no es el mas vendido {C}", end="")
# f) El total de ventas esta entre 500 y 1000.
elif totalV>=500 and totalV<=100:
    print(f"el total de ventas esta entre 500 y 1000 {totalV}", end="")
    