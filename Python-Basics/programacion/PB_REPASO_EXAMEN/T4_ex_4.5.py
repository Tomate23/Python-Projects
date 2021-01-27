"""
 Crea un programa llamado ex_4_5, en el que el usuario introduzca números enteros hasta
adivinar el número aleatorio entre 0 y 100 generado al azar por el ordenador. El programa debe
avisar si el número introducido por el usuario es más grande o más pequeño que el número
generado aleatoriamente.
La instrucción de Python que te permite generar un número aleatorio entre a y b, ambos
incluidos, es random.randint(a, b)
"""
from random import randint
rand_num=randint(0,100)
inten=7
print(rand_num)
print("--------------------------------------------------------------------------------------")
print("tendras que intertar deivinar el numero que ha pensado el ordenador entre 0 y 100!!!")
print("--------------------------------------------------------------------------------------")
n_us=int(input("introduce posible numero:\n"))
while n_us!=rand_num and inten!=0:
    if n_us<rand_num:
        print(f"te quedan:{inten}, intentos")
        print("prueba con unos mas grande!!!")
        n_us=int(input("introduce posible numero:\n"))
        inten-=1
    else:
        print(f"te quedan:{inten}, intentos")
        print("prueba con uno mas pequeño!!!")
        n_us=int(input("introduce posible numero:\n"))
        inten-=1
    if inten==0:
        print("se han acabado los intentos")
        
if n_us==rand_num:
    print(f"lo has adivinado, era el:{rand_num}")

