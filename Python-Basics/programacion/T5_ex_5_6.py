n=input("introduce un numero:\n")
letras={"0":"zero","1":"uno","2":"tres","3":"tres","4":"cuatro","5":"cinco","6":"seis","7":"siete","8":"ocho","9":"nueve"}
L1=[]
L1.append(n)
L1.split()
for x in range(0,len(L1.split)):
    for numero in range(len(L1.split)-x):
        if L1[numero] in letras:
            print(letras)
            
    
    