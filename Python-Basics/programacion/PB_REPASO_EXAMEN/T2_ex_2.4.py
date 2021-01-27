"""
2.4 Crea un programa llamado ex_2_4, que dado un número entero que designa un periodo de
tiempo expresado en segundos, imprima el equivalente en días, horas, minutos y segundos.
Por ejemplo: 300000 segundos serán 3 días, 11 horas, 20 minutos y 0 segundos.
Por ejemplo: 7400 segundos serán 0 días, 2 horas, 3 minutos y 20 segundos.
"""
seg=int(input("introduce un valor en segundos:\n"))
dias=seg//86400#para pasar a dias hacemos la convercion sabiendo los segundos en un dia.
print(f"dias:{dias}")
resto_dias=seg%86400#el resto de esta operacion son los segundos quedan al saber los dias que completa.
horas=resto_dias//3600#este resto se divide para sabes las horas a partir de los seg. restantes.
print(f"horas:{horas}")
resto_horas=resto_dias%3600#hacemos el resto en cuanto a las horas para saber los segundos y pasarlos a minutos.
minutos=resto_horas//60#pasamos a minutos 
print(f"minutos:{minutos}")
resto_minutos=resto_horas%60#con el resto de los minutos sabremos los segundos que quedan.
#segundos=resto_minutos//60#pasamos a segundos para saber los segundos restantes, a partir de los segundos que quedaban de los minutos
print(f"segundos:{resto_minutos}")
