"""
st=input("introduce un numero binario: ")
v=[]
for i in st:
    bi=int(i)
    v.append(bi)
v.reverse()   
suma=0
n=0
for i in range(len(v)-1,-1,-1):
    suma+=v[i]*(2**n)
    n+=1
print(suma)
"""
def Bi_a_dec(num_bi):
    for i in num_bi:
        bi=int(i)
        v.append(bi)
    v.reverse()
    suma=0
    n=0
    for i in range(len(v)-1,-1,-1):
        suma+=v[i]*(2**n)
        n+=1
    return suma
v=[]
st=input("introduce un numero binario: ")
conver= Bi_a_dec(st)

print(f"{st} en base dos es: {conver} en base 10")

    