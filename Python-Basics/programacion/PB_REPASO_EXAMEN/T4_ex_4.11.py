"""
4.11 Crea un programa llamado ex_4_11 que dibuje un triángulo con asteriscos, a partir de un
número entero introducido por el usuario que será el número de asteriscos de su anchura. Por
ejemplo, para el número 4 el programa debe imprimir:
"""
ast=int(input("da un valor a n:\n"))
icon="*"
i=1
while i<=ast:
    print(icon*i)
    i+=1
    if i==ast:
        while i!=0:
            print(icon*i)
            i-=1
        else:
            break
        