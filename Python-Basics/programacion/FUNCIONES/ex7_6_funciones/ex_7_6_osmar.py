#creamos nuestra clase con los parametros de produto
class producto:
    def __init__(self):
        self.nombre=""
        self.precio=0.0
        self.cantidad=0.0
#cremos una lista de la compra donde guardar cada producto con sus valores
compra=[]

#enseñmos el menu de seleccion de opciones al usuario
while True:
    
    print("***********************************")
    print("1. añadir producto")
    print("2. eliminar producto")
    print("3. listar producto/s")
    print("4. ordenar lista por dinero gastado en producto")
    print("0. salir")
    print("***********************************")
    print("\n\n\n")
    opcion=input("que operacion deseas hacer?")
    
    if opcion=="1":
        #para añadir productos o comprobar si ya existen, creamos una nueva variable producto
        #si ya existe el producto actualizamos el precio y la cantidad sino lo añadimos
        p=producto()
        p.nombre=input("nombre del producto: ")
        #buscamos dentro del vector compra para comprobar que el producto existe ya o no
        existe=False
        for i in range(0,len(compra)):
            if p.nombre==compra[i].nombre:#comrpbamos si el producto ya esta dentro del vector
                existe=True
                break
        if existe==True:
            print("este producto ya existe en la lista de la compra")
            print(compra[i].nombre, compra[i].cantidad, 'x', compra[i].precio, 'euros')
        else:
            p.precio=float(input("que precio tiene: "))
            p.cantidad=float(input("que cantidad: "))
            compra.append(p)#metemos los valores del producto al vertor
            
    elif opcion=="2":
        #para eliminar un producto, lo buscamos dentro del vector comopra y lo eliminamos
        #pedimos el nombre del producto a eliminar
        print("***ELIMNAR PRODUCTO***\n")
        nombre=input("que producto deseas eliminar? ")
        #comprobamos si el producto esta en la lista
        existe=False
        for i in range(0,len(compra)):
            if nombre==compra[i].nombre:
                existe=True
                break
        if existe==True:#si el producto esta en el vector lo borramos
            print(compra[i].nombre, compra[i].cantidad, 'x', compra[i].precio, 'euros')
            compra.pop( i )#borramos el producto
        else:
            print("este producto no esta en la lista")
            
    elif opcion=="3":
        for p in compra:
            print(f'{p.nombre:20}   {p.cantidad:2.1f} unidades   {p.precio:3.2f} euros')
        
        
        
            
        
        
    
        
        

        
    