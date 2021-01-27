"""
5.5 Crea un programa llamado ex_5_5, que dado un vector de 50 elementos enteros, lo
descomponga en dos, uno formado por los valores pares y otro formado por los valores
impares. En los dos vectores resultantes los valores se podrán consecutivamente, uno detrás del
otro, sin huecos.

from random import randrange
v1=[]
vpar=[]
vimpar=[]
for _ in range (50):
    ram=randrange(50)
    v1.append(ram)
    if (ram%2)==0:
        vpar.append(ram)
    else:
        vimpar.append(ram)
print(vpar+vimpar)
"""
cifra1=890//100
cifra2=(890/10)%10
cifra3=890%10
print(cifra1)
print(cifra2)
print(cifra3)

    
