'''
#codigo iterativo
a=int(input("intriduce value for a: "))
b=int(input("intriduce value for b: "))
resul=1
for i in range(0,b):
    resul*=a
print(resul)

#codigo recursivo
def expo(a,b):
    
    if b==0:
        return 1
    else:
        return a*expo(a,b-1)
    
a2=int(input("intriduce value for a: "))
b2=int(input("intriduce value for b: "))
print(expo(a2,b2))

#caso que b sea un numero negativo
#codigo iterativo:

a=int(input("intriduce value for a: "))
b=int(input("intriduce value for b: "))

if b > 0:
    resul=1
    for i in range(0,b):
        resul*=a
    print(resul)
    
elif b < 0:
    #a^-b = 1/a^b
    resul=1
    b=-(b)
    for i in range(0,b):
        resul*=a
    x=1/resul
    exp=1/x
    print(f"el resultado es: {exp:.2f}")
 
#codigo recursivo caso b<0:

def expo(a,b):
    
    if b==0:
        return 1
    else:
        return a*expo(a,b-1)

def expoNeg(a,b):#si pasamos un valor de b negativo
    if b==0:#b<0 tenemos que llegar a 0 para que devuelva 1, para llegar a cero b+1
        return 1
    else:
        return a*expoNeg(a,b+1)#hasta que la b sea 0.
    
a2=int(input("intriduce value for a: "))
b2=int(input("intriduce value for b: "))
if b2<0:
    print(expoNeg(a2,b2))
else:
    print(expo(a2,b2))


from funcionesExamenEX5 import *
class punto:
    def __init__(self):
        self.x=0
        self.y=0
        self.z=0
p=punto()

lee_punto(p)

print("Distancia: ",distancia(p.x,p.y,p.z))

def acker(m,n):
    if m==0:
        return (n+1)
    elif n==0:
        return acker(m-1,1)
    else:
        return acker(m-1,acker(m,n-1))
 
x=int(input("introduce valor:"))
print("m: ",x)
y=int(input("introduce valor:"))
print("n: ",y)
print("el valor segun la funcion recursiva acker es: ",acker(x,y))

print("valor para acker(2,1) es: ",acker(2,1))


Acker(2,1) output
+++++++++++++++++
a(1,a(2,0))
a(1,1)
a(0,a(1,0))
a(0,1)
2
#no se como seguir los outputs

'''
def expo(a,b):
    
    if b==0:
        return 1
    else:
        return a*expo(a,b-1)
print(expo(2,3))


    
    
    
    