#8.16 Programa un método recursivo que calcule la suma de un vector de números enteros.
"""
v1=[1,2,3,4,5]
v2=[6,7,8,9,10]
vr=[]
#metodo iteratívo
for i in range(len(v1)):
    vr.append(v1[i]+v2[i])
print(vr)

#Método Recursivo
def suma_vec(vector1,vector2):
    if len(vector1)<2:
        return vector1[0]+vector2[0]
    else:
        resul.append(vector1[0]+vector2[0])
        cut=suma_vec(vector1[1:],vector2[1:])
        
    return resul
    
    
v1=[1,2,3,4,5]
v2=[6,7,8,9,10]
resul=[]
print(suma_vec(v1,v2))

#no he podido lograr que devuelva la ultima suma 5+10, estaba probando a sumar dos vectores
"""
"""
suma de un vector Recursivamente
"""
def sumar(v):
  if len(v) == 0:
    return 0
  else:
    return v[0] + sumar(v[1:])

vector1 = [10,20,30,40,50]
print(vector1)
print(sumar(vector1))
