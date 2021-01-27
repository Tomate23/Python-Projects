#ejercicio 2.4

seg = float(input("introduce un numero entero:"))
dia = seg // 86400 #el numero 86400 corresponde al equivalente en segundos de un dia
print("dias:",dia)
dia2 = seg % 86400
hora = dia2 // 3600 #el numero 3600 corresponde al equivalente en segundos de una hora
print("horas:",hora)
hora2 = dia2 % 3600
minu = (hora2 / 60)
print("minuts:",minu)
minu2 = minu % 60
segu = minu2 / 60
print("segundos:",segu)