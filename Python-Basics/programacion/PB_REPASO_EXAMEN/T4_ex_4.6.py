"""
4.6 En la tienda de los hermanos Roque es tradición presentar las latas de conserva apiladas
triangularmente: en el primer piso una lata, en el segundo piso dos latas, en el tercer piso tres, y
así sucesivamente. Por ejemplo, seis latas se ponen así:
"""
lat=int(input("da un valor a n:\n"))
valor1=1
while valor1<=lat:#esto lo que hace es contar las filas que pueden hacerse con el numero introducido
    lat=lat-valor1#cada ves restas del numero el numero de filas que pueden haber
    valor1+=1#si al final es 0 es porque se puede apilar
if lat>0:
     print("no es plilable")
else:
    print("es apilable")