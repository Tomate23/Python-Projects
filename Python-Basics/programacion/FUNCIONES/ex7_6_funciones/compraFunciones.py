"""
Adapta l’exercici 7.6 (llista de la compra) per que treballi amb funcions.
Algunes de les funcions:
- menu() : dibuixa el menú i retorna l’opció escollida per l’usuari
- buscar(nom) : retorna la posició dins la llista o -1 si no hi és
- imprimir(producte) : imprimeix un producte
- demanar(producte) : demana les dades d’un producte i totes les funcions que vegis necessàries
"""
#la clase y el vector vacio (se supone que ya estan en el programa principal).
#Creamos la funcion del menu de opciones. Que devuelve la opcion que el usuario haya elegido
def menu():
    print("""
****************************
MENU DE OPCIONES
****************************
1. Añadir Producto
2. Eliminar Producto
3. Listar Producto
0. Salir
"""
        )
    op=int(input("Que operación deseas realizar: "))
    return(op)

#funcion de buscar el producto dentro de la lista
def buscar(nombre,compra):#tenemos que darle a la funion el vector donde buscar el producto.
    existe=False#usamos el chivato
    for i in range(0,len(compra)):#recorremos cada elemento de la lista
        if nombre==compra[i].nombre:#si el nombre introducido, esta dentro de los nombres de la lista
            existe=True#entonces si que esta dentro de la lista el chivato obtiene el valor True
            break
        return existe
    
def pedir_nombre(clase):#el parametro que le damos a la funcion es la clase, donde se encuentra el nombre del producto
    clase.nombre=input("Introduce el nombre del producto a añadir: ")
    return clase.nombre
def pedir_precio(clase):
    clase.precio=float(input("que precio tiene: "))
    return clase.precio
def pedir_cantidad(clase):
    clase.cantidad=cantidad=float(input("que cantidad: "))
    return clase.cantidad
    
#cremos la funcion para borrar un producto, cogiendo su nombre como parametro y el vector
def delete(nombre,vector):
    existe=False
    for i in range(0,len(vector)):
        if nombre==vector[i].nombre:
            existe=True
            break
    if existe==True:
        print(vector[i].nombre, vector[i].cantidad, 'x', vector[i].precio, 'euros')
        vector.pop( i )#borramos el producto
        return "El producto se ha borrado correctamente!!!"
    else:
        return "Este producto no esta en la lista"
#funcion para listar los productos.
def listar(clase,vector):
    #for i in (vector):
        for p in vector:
            print (f'{p.nombre:20}   {p.cantidad:2.1f} unidades   {p.precio:3.2f} euros')
    
        
        
def clean():
    print("\n"*50)
        
            
    
    
    
    
    
    
    


