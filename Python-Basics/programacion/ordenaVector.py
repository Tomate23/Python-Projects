#ejercic 4
'''
Escribe una función recursiva y otra iterativa que calcule a**b, mediante
multiplicaciones sucesivas, siendo a y b números enteros. b puede ser negativa, y en
ese caso a**b = 1/ a**b
'''
#codigo iterativo
'''
a elevado a b es igual que multiplicar a*a el numero de veces de b
'''
a = int(input("introduce base a: "))
b = int(input("introduce exponente b: "))
def Ieterat(a,b):
    if b>0:
        suma = 1
        for i in range(b):
            suma *= a
        return suma
    elif b<0:
        b = -(b)
        suma = 1
        for i in range(b):
            suma *= a
            x = 1 / suma
            resul = 1 / x
        return resul
print(Ieterat(a,b))

#codigo recursivo
def recursivo(a,b):
    if b==0:
        return 1
    else:
        return a*expo(a,b-1)
def expoNeg(a,b):#si pasamos un valor de b negativo
    if b==0:#b<0 tenemos que llegar a 0 para que devuelva 1, para llegar a cero b+1
        return 1
    else:
        return a*expoNeg(a,b+1)#hasta que la b sea 0.
    
            
        




    













