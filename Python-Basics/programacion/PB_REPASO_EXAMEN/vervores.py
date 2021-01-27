from random import randint
v=[]
for _ in range(10):
    num=randint(0,11)
    v.append(num)
    print(v)
    if (num%2)==0:
        print(f"numero par,{num}")
    else:
        print(f"numero impar,{num}")