'''
Crea un programa llamado ex_3_7, que pida los coeficientes a y b de una ecuación de primer
grado y calcule la solución.
'''
a = float(input("introduce el valor de a:\n"))
b = float(input("introduce el valor de b:\n"))



if a != 0:
    x = -(b)/a
    print(f"resultado: {x}")
elif a == 0:
    print("indeterminacion!, devision entre 0")
else:
    print("soluciones infinitas")