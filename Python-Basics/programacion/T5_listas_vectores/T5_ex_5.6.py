"""
5.6 Crea un programa llamado ex_5_6, en el que el usuario introduzca una número y el programa
genere una frase con las palabras correspondientes a cada cifra. Por ejemplo, 547 devolvería
“cinco cuatro siete”.
"""
letras=[]
num=int(input("introduce un numero entero:\n"))
while num<0:
    print("por favor introduce un numero entero!!!")
    num=int(input("introduce un numero entero:\n"))
nums=[0,1,2,3,4,5,6,7,8,9]
if num==0:
    letras.append("zero")
elif num==1:
    letras.append("uno")
elif num==2:
    letras.append("dos")
elif num==3:
    letras.append("tres")
elif num==4:
    letras.append("cuatro")
elif num==5:
    letras.append("cinco")
elif num==6:
    letras.append("seis")
elif num==7:
    letras.append("siete")
elif num==8:
    letras.append("ocho")
elif num==9:
    letras.append("nueve")
print(letras)
