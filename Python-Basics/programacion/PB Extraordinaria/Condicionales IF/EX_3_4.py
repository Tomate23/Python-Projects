'''
Crea un programa llamado ex_3_4, que pida un número por teclado e indique si es positivo,
negativo o cero. Intenta hacerlo con el mínimo número de comparaciones.
'''
num = int(input("introduce un numero:\n"))
if num<0:
    print("el numero es -")
elif num>0:
    print("el numero es +")
else:
    print("el numero es 0")