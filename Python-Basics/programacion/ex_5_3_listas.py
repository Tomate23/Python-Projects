"""
 Crea un programa llamado ex_5_3 para rellenar un vector de 15 número enteros:
a) Con valores aleatorios entre 1 y 10, y a continuación diga cuantos pares e impares hay.
b) Con valores aleatorios entre 1 y 10, y a continuación sume los que estén en posiciones que
son múltiplos de 3.
c) Con los primeros valores de la serie de Fibonacci.
d) Con valores introducidos por el usuario, y a continuación que los imprima al revés.
e) Con valores introducidos por el usuario, donde cada valor se debe pedir de nuevo hasta que
35
esté entre 1 o 10.
f) Con valores introducidos por el usuario, que deben formar una secuencia creciente.
g) Con valores introducidos por el usuario, que no deben estar repetidos.

from random import randrange
v1=[]
suma_multiplos=0
vpar=[]
vimpar=[]
vmult3=[]
vusuario=[]
for _ in range(1,16):
    num=randrange(1,10)
    v1.append(num)
    if (num%2)==0:
        #print(f"numero par: {num}")
        vpar.append(num)
    else:
        #print(f"numero impar: {num}")
        vimpar.append(num)
        
    if (num%3)==0:
        #print(f"multiplo de tres: {num}")
        suma_multiplos+=num
        #print(f"la suma de los numeros multiplos de tres es: {suma_multiplos}")
        vmult3.append(suma_multiplos)  
print(f"vector numeros pares: {vpar}")
print(f"vector numeros impares: {vimpar}")
print(f"vector numeros suma de multiplos de 3 :{vmult3}")
"""
vusuario=[]
revez=[]

for x in range(1,5):
    num_usu=int(input("introduce un valor para el vector:"))
    vusuario.append(num_usu)
    n=len(vusuario)
for i in range(n):
    revez.append(vusuario[n-i-1])
print(vusuario)
print(revez)
    
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

        
        
        

        

    