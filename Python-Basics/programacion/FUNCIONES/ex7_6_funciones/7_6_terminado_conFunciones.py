"""
from compraFunciones import menu
from compraFunciones import buscar
from compraFunciones import pedir_nombre
"""


from compraFunciones import *
#creamos la clase:
class producto:
    def __init__(self):
        self.nombre=""
        self.precio=0.0
        self.cantidad=0.0


#cremos una lista de la compra donde guardar cada producto con sus valores
compra=[]
#imprimimos el menu, llamando a la funcion menu()
while True:
    opcion=menu()#guardo la opcion elegida por el usuario en una variable.
    if opcion==1:
        #para añadir productos o comprobar si ya existen, creamos una nueva variable producto
        #si ya existe el producto actualizamos el precio y la cantidad sino lo añadimos
        p=producto()
        #p.nombre=input("Introduce el nombre del producto a añadir: ")
        p.nombre=pedir_nombre(p)
        existe=buscar(p.nombre,compra)#esta funcion nos devuelve True si el producto esta dentro del vector
        if existe==True:
            print("Este producto ya existe en la lista de la compra")
            print(compra[i].nombre, compra[i].cantidad, 'x', compra[i].precio, 'euros')
        else:
            p.precio=pedir_precio(p)#funcion para pedir el precio
            p.cantidad=pedir_cantidad(p)#funcion para pedir la cantidad del producto
            compra.append(p)#metemos los valores del producto al vertor
            
        clean()
            
    elif opcion==2:
        #para eliminar un producto, lo buscamos dentro del vector comopra y lo eliminamos
        #pedimos el nombre del producto a eliminar
        print("***ELIMNAR PRODUCTO***")
        nombre=input("que producto deseas eliminar? ")
        existe=delete(nombre,compra)#le pasamos a la funcion de buscar(la que tiene el chivato) el nombre del producto que queremos borrar
        clean()
        print(existe)
        print(compra)
        
    elif opcion==3:
        print("***LISTA DE PRODUCTOS***")
        #for i in range(0,len(compra)):
        print(listar(p,compra))
        
    elif opcion==0:
        print("Hasta la próxima!!!")
        break
    
 

