# ejercicio 2.3
#pedimos las coordenadas de cada punto (a y b)
#en este programa considero que el usuario introducira valores enteros
ax=int(input("introduzca un valos para ax:"))
ay=int(input("introduzca un valos para ay:"))
bx=int(input("introduzca un valos para bx:"))
by=int(input("introduzca un valos para by:"))
#calculamos segun la formula dada
mx= (ax+bx)/2
my= (ay+by)/2
#mostramos el resultado
print("el punto medio es:(" ,mx, "," ,my, ")" )
#calculo de cuadrante
if mx>0 and my>0:
    print("primer cuadrante")
elif mx<0 and my>0:
    print("segundo cuadrante")
elif mx<0 and my<0:
    print("tercer cuadrante")
elif mx>0 and my<0:
    print("cuarto cuadrante")
#calculo de ejes positivos
elif mx==0 and my==0:
    print("origen de coodenadas")
elif mx>0 and my==0:
    print("se encuentra en el eje x, parte positiva")
elif mx==0 and my>0:
    print("se encuentra en el eje y, parte positiva")
#calculo de ejes negativos
elif mx<0 and my==0:
    print("se encuentra en el eje x,parte negativa")
elif mx==0 and my<0:
    print("se encuentra en el eje y,parte negativa")
    

    
    