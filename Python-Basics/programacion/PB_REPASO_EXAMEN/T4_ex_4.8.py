"""
4.8 Crea un programa llamado ex_4_8 que pida al usuario dos números enteros a y b por teclado y
devuelva el resultado de realizar su multiplicación mediante sumas. Es decir:
"""
a=int(input("da un valor a a:\n"))#pedimos el vaslor de a
b=int(input("da un valor a b:\n"))#pedimos el valor de b
mult=a*b#efectuamos la multiplicaion 
print(f"usando multiplicacion:{mult}")
print("<<<calculamos usando sumas>>>")
suma=0
i=1
if a<0 or b<0:
    a=-a
    b=-b
while i<=b:
    suma+=a
    print(suma)
    i+=1
    