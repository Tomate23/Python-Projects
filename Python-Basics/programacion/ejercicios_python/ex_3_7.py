print("segun la formula de primer grado ax+b=0")
a=float(input("introduce un valor para a:\n"))
b=float(input("introduce un valor para b:\n"))
if a!=0:
    x= -b / a
    print("la salucion a la ecuacion es: %3.1F" % x)
elif a==0 and b!=0:
    print("no existe solucion")
    
elif a==0 and b==0:
    print("soluciones infinitas")


        