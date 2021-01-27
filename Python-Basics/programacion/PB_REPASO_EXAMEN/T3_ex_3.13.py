"""
3.13 Reescribe el programa anterior de la ecuación de segundo grado ex_3_12, para que la gestión
de los casos especiales (división por cero, raíz cuadrada de un número negativo) no se haga con
if … else … sino con el mecanismo de gestión de excepciones try … except … finally ...
"""
from math import sqrt
a=float(input("introduce un valor para a:\n"))
b=float(input("introduce un valor para b:\n"))
c=float(input("introduce un valor para c:\n"))
inraiz=b**2-(4*a*c)

try:
        raiz=sqrt(inraiz)
        x1=(-b+raiz)/2*a
        x2=(-b-raiz)/2*a
        x=-c/b
        #print(f"x1:{x1}")
        #print(f"x2:{x2}")
except ZeroDivisionError:
    if a!=0 and b!=0:
        x=-b/a
        print("la solucion es: %3.2f" %x)
    elif a==0 and b!=0:
        print("no existe solucion")
    elif a==0 and b==0:
        print("esta ecucaion tiene soluciones infinitas")
except ValueError:
    if inraiz<0:
        print("repuesta con numeros imaginarios!!!")
        x1 = complex( -b/(2*a) , +sqrt(-inraiz)/(2*a) )
        x2 = complex( -b/(2*a) , -sqrt(-inraiz)/(2*a) )
        print(f"x1:{x1}")
        print(f"x2:{x2}")
except:
    print("ErrorDesconocido")
finally:
    print("Thanks for using my program")

    
    

    