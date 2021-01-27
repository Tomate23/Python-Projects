"""3.11 Crea un programa llamado ex_3_11, que pida una fecha formada por tres valores numéricos
(día, mes y año), y determine si la fecha corresponde a un valor válido.
Pista: se debe tener presente el valor de los días en función de los meses y de los años. Es decir:
- Los meses 1, 3, 5, 7, 8, 10 y 12 tienen 31 días.
- Los meses 4, 6, 9 y 11 tienen 30 días.
- El mes 2 tiene 28 días, excepto cuando el año es divisible por 4, que tiene 29 días. (¡pero no
cuando es divisible por 100, a menos que sea divisible también por 400!)
Pista: para saber si un número es divisible por 4, pregunta si el resto de dividirlo por 4 es cero.
"""
#pedimos al usuario que introduzca la fecha
dia=int(input("introduce el dia:\n"))
mes=int(input("introduce el mes:\n"))
año=int(input("introduce el año:\n"))
#calculamos cunado el año sea bisiesto
div=año%4
#aseguramos que los daros son validos
while dia<0 or mes<0 or año<0:
    print("------------------------------")
    print("introduce valores validos!!!")
    print("------------------------------")
    dia=int(input("introduce el dia:\n"))
    mes=int(input("introduce el mes:\n"))
    año=int(input("introduce el año:\n"))
#creamos lista con los valores correctos
mes31=[1,3,5,7,8,10,12]
if mes in mes31:
    if dia>31:
        print("---------------------------------------------------")
        print("fecha invalida; este mes no tiene mas de 31 dias!!!")
        print("---------------------------------------------------")
    else:
        print("------------------------------")
        print("fecha valida!!!")
        print("------------------------------")
mes30=[4,6,9,11]
if mes in mes30:
    if dia>30:
        print("---------------------------------------------------")
        print("fecha invalida; este mes no tiene mas de 30 dias!!!")
        print("---------------------------------------------------")
    else:
        print("------------------------------")
        print("fecha valida!!!")
        print("------------------------------")
if mes==2 and dia>28 and div!=0:
    print("------------------------------------------------")
    print("fecha invalida; este mes no tiene mas de 28 dias")
    print("------------------------------------------------")
if mes==2 and div==0 and dia>=29:
    print("----------------------------------------------------")
    print("fecha valida; año bisiesto, febrero tiene 29 dias!!!")
    print("----------------------------------------------------")
        
