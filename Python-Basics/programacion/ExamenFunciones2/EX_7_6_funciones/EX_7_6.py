from Funciones_7_6 import *

class Productos():
    def __init__(self):
        self.nombre = ""
        self.cantidad = 0
        self.precio = 0.0
        
compra = []

while True:
    operacion = menu()
    if operacion == 1:# añadir un producto
        items = Productos()# guardamos la clase en una varibale para acceder a las propiedades
        
        items.nombre = ask_name(items)#pedimos el nombre del producto
        producto_dentro = existe(compra, items.nombre)#comprobamos que ese producto no este ya en la lista de compra
        
        if producto_dentro == True:
            print("Este producto ya esta en la lista de compra!")
            show(compra)
        else:
            #pedimos los otros datos, si el producto no esta en la lista de compra
            items.contidad = ask_amount(items)
            items.precio = ask_prize(items)
            print("\n")
            try:
                compra.append(items)
                print("Producto añadido correctamente!\n")
                show(compra)
            except:
                print("producto no añadido!")
    elif operacion == 2:# eliminar producto
        print("*** ELIMINAR PRODUCTO ***")
        nombre = input("Que producto desea eliminar:\t")
        resultado = delete(nombre, compra)
        print(resultado, end="\n")
        print(compra)
    elif operacion == 3:# listar productos
        print(listar(items, compra))
        
        
    elif operacion == 0:
        print(">> Hsta luego")
        break 
        
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
                
        