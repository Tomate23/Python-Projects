
#8.17 Programa un método recursivo que invierta el orden de un vector de números enteros.
#revertir el vector
def rever(vector):
    
        for i in range(len(vector)-1,-1,-1):
            v2.append(vector[i])
        return v2
    
#vector de 7 elementos
i=0
v=[]
v2=[]
while i!=7:
    valores=int(input("introduce valores: "))
    v.append(valores)
    i+=1
    

vec=rever(v)

print("vector introducido: ",v)
print("vector invertido: ", v2)
"""
#lo de arriba funciona pero no es recursivo

def inver(vector):
  if len(vector) < 2:
    return vector
  else:
    elem = inver(vector[1:])#pilla del v[1] hasta el ultimo indice del vector
    elem.append(vector[0])#añade el v[0] al asi cada ves se invierte.
    return elem

vec = [1, 2, 3, 4, 5]
print(vec)
print(inver(vec))
"""