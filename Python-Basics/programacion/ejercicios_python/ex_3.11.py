"""
3.11 Crea un programa llamado ex_3_11, que pida una fecha formada por tres valores numéricos
(día, mes y año), y determine si la fecha corresponde a un valor válido.

Pista: se debe tener presente el valor de los días en función de los meses y de los años. Es decir:
- Los meses 1, 3, 5, 7, 8, 10 y 12 tienen 31 días.
- Los meses 4, 6, 9 y 11 tienen 30 días.
- El mes 2 tiene 28 días, excepto cuando el año es divisible por 4, que tiene 29 días. (¡pero no
cuando es divisible por 100, a menos que sea divisible también por 400!)

Pista: para saber si un número es divisible por 4, pregunta si el resto de dividirlo por 4 es cero.
"""
dia=int(input("introduce un dia en formato:/dd/:\n"))
mes=int(input("introduce un mes en formato:/mm/:\n"))
año=int(input("introduce un año en formato:/aaaa/:\n"))
bici=(año % 4) / 4 

if mes == 4 and dia > 30:
    print("ese mes no tiene mas de 30 dias, numero de dias de para ese mes invalido")
elif mes== 6 and dia > 30:
    print("ese mes no tiene mas de 30 dias, numero de dias de para ese mes invalido")
elif mes== 9 and dia > 30:
    print("ese mes no tiene mas de 30 dias, numero de dias de para ese mes invalido")
elif mes== 11 and dia > 30:
    print("ese mes no tiene mas de 30 dias, numero de dias de para ese mes invalido")   

    if mes == 1 and dia > 31:
        print("ese mes no tiene mas de 31 dias, numero de dias de para ese mes invalido")
    elif mes == 3 and dia > 31:
        print("ese mes no tiene mas de 31 dias, numero de dias de para ese mes invalido")   
    elif mes == 5 and dia > 31:
        print("ese mes no tiene mas de 31 dias, numero de dias de para ese mes invalido")
    elif mes == 7 and dia > 31:
        print("ese mes no tiene mas de 31 dias, numero de dias de para ese mes invalido")
    elif mes == 8 and dia > 31:
        print("ese mes no tiene mas de 31 dias, numero de dias de para ese mes invalido")
    elif mes == 10 and dia > 31:
        print("ese mes no tiene mas de 31 dias, numero de dias de para ese mes invalido")
    elif mes == 12 and dia > 31:
        print("ese mes no tiene mas de 31 dias, numero de dias de para ese mes invalido")
else:
    print("fecha valida")
    
        
        
        
if bici == 0:
     print("<<<segun este año, el mes 2 tiene 29 dias, fecha valida>>>")     
elif mes==2 and dia > 28:
    print("ese mes no tiene mas de 28 dias, numero de dias de para ese mes invalido")
elif dia<28:
    print("mes valido")  
else:
    print("<<<fecha invalida>>>")
    

    




  
    


    
    