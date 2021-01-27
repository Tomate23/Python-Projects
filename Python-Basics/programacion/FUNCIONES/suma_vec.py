"""
from random import randint
v1=[]
v2=[]
for _ in range(0,10):
    n=randint(0,15)
    v1.append(n)
print(v1)

for _ in range(0,10):
    n2=randint(0,15)
    v2.append(n)
print(v2)
"""
v1=[1,2,3,4,5]
v2=[6,7,8,9,10]
vsuma=[]
#suma de vectores
for i in range(len(v1)):
    vsuma.append(v1[i]+v2[i])
print(vsuma)

        
        