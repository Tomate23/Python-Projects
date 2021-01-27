#8.13 Programa un método recursivo que transforme un número entero positivo de base 10 a base 2.
#algoritmo iterativo
bi=[]
def Dec_a_bi(n):
    if n==0:
        return 0
    else:
        bi.append(n%2)#guardo el resto de cada division en un vector
        return Dec_a_bi(n//2)#cada vuelta divido entre 2
    return bi

num=int(input("valor de n: "))
num2=Dec_a_bi(num)
bi.reverse()
print(bi)
"""
#hay que imprimir al revez el vector
for i in range(len(bi)-1,-1,-1):
    reverse=bi[i]
    print(reverse)
"""   