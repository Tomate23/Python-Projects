"""
3.13 Reescribe el programa anterior de la ecuación de segundo grado ex_3_12, para que la gestión
de los casos especiales (división por cero, raíz cuadrada de un número negativo) no se haga con
if … else … sino con el mecanismo de gestión de excepciones try … except … finally ...
"""
import math
print("ECUACION: a x2+ b x + c = 0")
a=float(input("introduzca un valor para a:\n"))
b=float(input("introduzca un valor para b:\n"))
c=float(input("introduzca un valor para c:\n"))
imagi=b**2-(4*a*c)

#raiz=math.sqrt(imagi)
x0=-c/b
#x1=(-b+raiz)/2*a
#x2=(-b-raiz)/2*a
try:
    raiz=math.sqrt(imagi)
    div1=(-b+raiz)/2*a
    div2=(-b-raiz)/2*a
except:
    print("la raiz cuadrada de un numero negativo no existe, intneta otros valores")
else:
    print("si la a=0 se convierte en una ecuacion de primer grado grado")
finally:
    print("prueba valores que al hacer las operaciones dentro de la raiz cuadrada den > o")
    