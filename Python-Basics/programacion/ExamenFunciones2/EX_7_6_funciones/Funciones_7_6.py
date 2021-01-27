# Fucnion para imprimir el menu de opciones
def menu():
    print('''
********************
* MENU DE OPCIONES *
********************
1. Añadir un Producto
2. Eliminar un Producto
3. Listar los Productos
0. salir
'''
        )
    op = int(input("Que operacion deseas hacer?\t"))
    return op
# preguntamos el nombre, precio y cantidad de los productos
def ask_name(clase):
    clase.nombre = input("Nombre del Producto:\t")
    return clase.nombre

def ask_amount(clase):
    clase.cantidad = input("Cantidad:\t")
    return clase.cantidad

def ask_prize(clase):
    clase.precio = input("Precio:\t")
    return clase.precio






# comprobacion que el producto no esta ya dentro del vector
def existe(vector, nombre):
    existe = False# usamos el chivato
    for i in range(0, len(vector)):
        if nombre == vector[i].nombre:
            existe = True
    return existe

# muestra producto
def show(vector):
    for i in range(len(vector)):
        print(vector[i].nombre, vector[i].cantidad, 'x', vector[i].precio, 'euros')

# eliminar un producto
def delete(nombre, compra):
    en_lista = existe(compra, nombre)
    if en_lista == True:
        for i in range(len(compra)):
            compra.pop(i)
        return "Poducto eliminado correctamente!"
    else:
        return "Este producto no esta en la lista!"
def listar(items, compra):
    for items in compra:
        print(f'{items.nombre:20}   {items.cantidad:2.1f} unidades   {items.precio:3.2f} euros')
        
    














