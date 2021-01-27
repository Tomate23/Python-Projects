"""
3.12 Crea un programa llamado ex_3_12, que pida los coeficientes a, b y c de una ecuación de
segundo grado y calcule la solución
"""
import math
print("ECUACION: a x2+ b x + c = 0")
a=float(input("introduzca un valor para a:\n"))
b=float(input("introduzca un valor para b:\n"))
c=float(input("introduzca un valor para c:\n"))
imagi=b**2-(4*a*c)
x0=-c/b

if imagi < 0:
    print("la ecuacion no tiene resultados reales")
elif imagi > 0:
    raiz=math.sqrt(imagi)
    x1=(-b+raiz)/2*a
    x2=(-b-raiz)/2*a
    print("x1=%3.2f" % x1)
    print("x2=%3.2f" % x2)
if a==0:
    print("la solucion es:%3.2f" % x0)
    print("al ser a=0 se convierte en una ecuacion de primer grado")
    

    