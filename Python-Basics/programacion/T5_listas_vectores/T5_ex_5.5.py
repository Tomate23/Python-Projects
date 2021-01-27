"""
5.5 Crea un programa llamado ex_5_5, que dado un vector de 50 elementos enteros, lo
descomponga en dos, uno formado por los valores pares y otro formado por los valores
impares. En los dos vectores resultantes los valores se podrán consecutivamente, uno detrás del
otro, sin huecos.
"""
from random import randint
v=[]
vp=[]
vi=[]
for _ in range(0,50):
    num=randint(0,50)
    v.append(num)
    print(v)
    print("------------------------------------------------------")
    if (num%2)==0:
        vp.append(num)
        print(f"lista con numeros pares:{vp}")
        print("------------------------------------------------------")
    else:
        vi.append(num)
        print(f"lista con numeros impares:{vi}")
print("------------------------------------------------------")
print(vp+vi)
        