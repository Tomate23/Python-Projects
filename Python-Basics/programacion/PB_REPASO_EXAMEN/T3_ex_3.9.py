"""
3.9 Amplia el ejercicio 2.3 para que además de encontrar el punto medio de dos puntos del espacio
bidimensional, escriba por pantalla a qué cuadrante del plano pertenece dicho punto medio.
"""
ax=float(input("introduce un valor para la coordenada ax:\n"))
ay=float(input("introduce un valor para la coordenada ay:\n"))
bx=float(input("introduce un valor para la coordenada bx:\n"))
by=float(input("introduce un valor para la coordenada by:\n"))
mx=(ax+bx)/2
my=(ay+by)/2
print(f"el punto medio de las coordenadas que has introducido es: {mx},{my}")
#cuadrantes
if mx>0 and my>0:
    print("se encuentra en el primer cuadrante")
elif mx<0 and my>0:
    print("se encuentra en el segundo cuadrante")
elif mx<0 and my<0:
    print("se encuentra en el tercer cuadrante")
elif mx>0 and my<0:
    print("se encuentra en el cuarto cuadrante")
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