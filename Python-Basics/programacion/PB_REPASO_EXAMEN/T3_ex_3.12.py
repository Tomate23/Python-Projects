"""
3.12 Crea un programa llamado ex_3_12, que pida los coeficientes a, b y c de una ecuación de
segundo grado y calcule la solución.
"""
#ax^2+bx+c=0
#primero impoertamos math para poder hacer la raiz cuadrada
from math import sqrt
#pedimos al usuario el valor de las variables
a=float(input("introduce un valor para a:\n"))
b=float(input("introduce un valor para b:\n"))
c=float(input("introduce un valor para c:\n"))
#decalramos una variable para hacer la raiz
inraiz=b**2-(4*a*c)
if inraiz<0:
    print("repuesta con numeros imaginarios!!!")
    x1 = complex( -b/(2*a) , +sqrt(-inraiz)/(2*a) )
    x2 = complex( -b/(2*a) , -sqrt(-inraiz)/(2*a) )
    print(f"x1:{x1}")
    print(f"x2:{x2}")
elif inraiz>0:
    #calculamos
    raiz=sqrt(inraiz)
    x1=(-b+raiz)/2*a
    x2=(-b-raiz)/2*a
    print(f"x1:{x1}")
    print(f"x2:{x2}")
#ecuacion de primer grado a=0 --> x=-c/b
if a==0 and b!=0 and c!=0:
    print("al ser a=0 se convierte en una ecuacion de primer grado")
    x=-c/b
    print("la solucion es: %3.2f" %x)
elif a==0 and b==0 and c!=0:
    print("no existe solucion")
elif a==0 and b==0 and c==0:
    print("esta ecucaion tiene soluciones infinitas")


    