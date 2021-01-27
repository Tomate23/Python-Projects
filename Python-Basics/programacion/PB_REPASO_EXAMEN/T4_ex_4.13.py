"""
4.13 Queremos pedir una nota que será un valor real entre 0 y 10. ¿Te atreves a combinar
iteraciones con gestión de excepciones para que si el valor introducido no es numérico lo
vuelva a pedir en lugar de romper la ejecución del programa?
"""
#pedimos al usuario un valor entre el intervalo
while True:
    
    try:
        n=int(input("introduce un valor entre 0 y 10:\n"))
        break
    except ValueError:
            print("por favor introduce un valor numerico real!!!")
            #n=int(input("introduce un valor entre 0 y 10:\n"))
while True:
    try:
        n=int(input("introduce un valor entre 0 y 10:\n"))
        if n>=0 and n<=10:
            print("numero correcto!!!")
            break
    except ValueError:
        print("no es un numero, vuelve a probar")
        
        
        
        
        