print("el programa terminara cuando introduzca el numero 0!!!")
num=int(input("introduce un valor:"))
suma=0
div=0
while num!=0:
    num=int(input("introduce un valor:"))
    suma+=num
    div+=1
    print(div)
    if num<0:
        print(f"numero negativo:{num}")
    if num==0:
        print("el programa ha acabado!!!")
        media=suma/div
        print(f"la media de los valores introducidos es:{media}")
    