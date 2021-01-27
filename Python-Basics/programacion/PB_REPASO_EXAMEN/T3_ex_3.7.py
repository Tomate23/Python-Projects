"""
3.7 Crea un programa llamado ex_3_7, que pida los coeficientes a y b de una ecuación de primer
grado y calcule la solución.
"""
#ax + b = 0 y al despejar--> x=-b/a

#pedimos el valor de a y b
a=float(input("introduce un valor para a:\n"))
b=float(input("introduce un valor para b:\n"))
#hacemos calculos
if a!=0 and b!=0:
    x=-b/a
    print("la solucion es: %3.2f" %x)
elif a==0 and b!=0:
    print("no existe solucion")
elif a==0 and b==0:
    print("esta ecucaion tiene soluciones infinitas")