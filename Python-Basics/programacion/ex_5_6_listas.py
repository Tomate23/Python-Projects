"""
5.6 Crea un programa llamado ex_5_6, en el que el usuario introduzca una número y el programa
genere una frase con las palabras correspondientes a cada cifra. Por ejemplo, 547 devolvería
“cinco cuatro siete”.
"""
letras=["cero","uno","dos","tres","cuatro","cinco","seis","siete","ocho","nueve"]
anw=[]
index=int(input("introduce un numero:"))
cifra1=index//100
cifra2=(index//10)%10
cifra3=index%10
print(letras[cifra1],letras[cifra2],letras[cifra3])

"""
index=str(input("introduce un numero:"))
letras=["cero","uno","dos","tres","cuatro","cinco","seis","siete","ocho","nueve"]
espa=""
for c in index:
    espa=c+espa
print(espa)
"""