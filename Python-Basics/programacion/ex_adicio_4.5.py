from random import randint
num_prog=randint(0,100)
print(num_prog)

num_usu=int(input("intenta adivinar el numero entre 0 y 100!!!\n introduce tu numero:\n"))

while num_usu < num_prog or num_usu > num_prog:
    print("el numero introducido es menor, intente otro numero!!!")
    num_usu=int(input("introduce otro numero\n"))
    while num_usu > num_prog:
        print("el numero introducido es mayor, intente otro numero!!!")
        num_usu=int(input("introduce otro numero:\n"))
        if num_usu == num_prog:
            print("has adivinado en numero!!!")