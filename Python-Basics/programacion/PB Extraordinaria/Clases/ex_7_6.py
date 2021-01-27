# Creamos la clase con los datos de los productos
class Producto:
    def __init__(self):
        self.nombre = ''
        self.precio = 0.0
        self.cantidad = 0
        

        
# creamos un vector que es la lista de la compra donde guardar los productos
compra = []

# creamos el menu 
while True:
    print('''
**************************************
* 1.Añadir Producto                  *
* 2.Quitar Producto                  *
* 3.Listar productos                 *
* 4.Oidenar lista por dinero gastado *
* 0.Finalizar                        *
**************************************
''')
    operacion = int(input("Que operacion deseas hacer:\t"))

    # programamos las operaciones
    p = Producto() # guardamos la calse y sus carat. en una variable para poder acceder mejor a ellas
    if operacion == 1:
        print("+++ AGREGAR PRODUCTO +++\n")
        
        p.nombre = input("Introduce el nombre del producto:\t") # preguntamos el nombre del producto
    
        existe = False
        for i in range(len(compra)):
            if p.nombre == compra[i].nombre: # comprobamos si el producto ya esta dentro del vector compra
                existe = True
    
        if existe:
            print("Este producto ya esta en la lista!")
            print(compra[i].nombre, '-', compra[i].precio, 'X', compra[i].cantidad)
        else:
            p.precio = float(input("Introduce el precio del producto:\t"))
            p.cantidad = int(input("Introduce la cantidad de unidades de este producto:\t"))
            compra.append(p)
    
    elif operacion == 2:
        print("+++ ELIMINAR PRODUCTO +++\n")
        nombre = input("Producto a Eliminar:\t")
        
        existe = False
        for i in range(len(compra)):
            if nombre == compra[i].nombre:
                existe = True
                
        if existe:
            print("Borrando...")
            print(compra[i].nombre, '-', compra[i].precio, 'X', compra[i].cantidad)
            compra.pop(i)
        else:
            print("Este producto no esta en la lista de compra!")
            
    elif operacion == 3:
        # Modificar un producto. Pedimos su nombre y lo buscamos
        print('MODIFICAR PRODUCTOS\n')
        nombre = input('¿Qué nombre de producto a modificar? ')
        
        # Comprueba que el producto estuviera en la llista
        encontrado = False
        for i in range(0, len(compra)):
          if nombre == compra[i].nombre:
            encontrado = True
            break
    
        if encontrado:
          print(compra[i].nombre, compra[i].cantidad, 'x', compra[i].precio, 'euros')
          compra[i].precio = float( input('¿Qué nuevo precio tiene? ') )
          compra[i].cantidad = float( input('¿Qué nueva cantidad a comprar? ') )
        else:
          print('El producto no existía')

    
    
    elif operacion == 4:

        # Listar productos, mostrando el total a pagar
        print('LISTAR PRODUCTOS\n')
        total = 0
        for p in compra:
          print(f'{p.nombre:20}   {p.cantidad:2.1f} unidades   {p.precio:3.2f} euros')
          total = total + p.cantidad*p.precio
        print('------------------------------------------------')
        print(f'TOTAL                                {total:5.2f} euros')
        
    elif operacion == 0:
        # Salir del programa
        print('¡Adios!')
        break
            
    
    
