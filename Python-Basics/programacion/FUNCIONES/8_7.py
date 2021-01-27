"""
8.7 Observa los siguientes programas con variables locales y globales. ¿Sabrías decir, a ojo, qué
imprimirá cada uno de ellos por pantalla?
"""
#a) Función que usa la variable global s
def f():
 print(s)#imprimirá el valor de s porque las funciones pueden usar las variables del programa principal.
s = 'Me gusta Python'
f()
print("\n")

#b) Función con una variable s que se llama igual que la variable global
def f():
 s = 'A mi también'#la funcion imprime a mi tambien y ni me gusta python por es la que esta dentro, es local
 print(s)
s = 'Me gusta Python'#debido a que esta es una variable global, el programa principal la usa
f()
print(s)
print("\n")

#c) Función con una variable s que se llama igual que la variable global
def f():
 #print(s)#daria un error por estas intentando imprimir una variable local que aun no ha sido declarada
 s = 'A mi también'
 print(s)
 
s = 'Me gusta Python'
f()
print(s)
print("\n")
#d) Función que utiliza la variable global s
def f():
    global s#esta variable s toma el valor de s = 'Me gusta Python' y se imprime en la funcion ya que es global
    print(s)
    s = 'A mi también'#luego este valor de s es la nueva variable gobal.
    print(s)
s = 'Me gusta Python'#esta variable del programa principal pasa a ser variable gobal
f()
print(s)