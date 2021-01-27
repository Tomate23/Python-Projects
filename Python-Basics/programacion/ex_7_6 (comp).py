"""
Nuestra lista de la compra está formada por la lista de productos a comprar. De cada producto
guardamos: nombre, precio por unidad, y unidades a comprar.
"""
class productos:
    def __init__(self):
        self.nombre=""
        self.precio=0
        self.unidades=0
        
vProd=[]
menos=0
#bucle del menu
while True:
    resp=input("quieres entrar al menú de operaciones? [ok|no]")
    if resp=="no":
        print("hasta la proximaaaaaaa!!!")
        break
    
    if resp=="ok":
        print("*******************_MENU_******************")
        print("1.añadir producto")
        print("2.Quitar producto")
        print("3.Listar productos ")
        print("0.Finalizar.")
        print("*******************************************")
        print("para añadir productos presiona 1")
        
    
        operacion=int(input("que operacion deseas hacer? : "))
        if operacion==1:
            num_produc=int(input("cuantos productos deseas añadir? : "))
            for i in range(0,num_produc):
                vProd.append(productos())
                vProd[menos].nombre=input(f"introduce nombre del producto {i+1}: ")
                vProd[menos].precio=float(input("introduce precio/unidad del porducto: "))
                vProd[menos].unidades=int(input("introduce las unidades del producto: "))
                menos+=1  
        if operacion == 3:
            for j in range(len(vProd)):
                print(f"producto: {vProd[j].nombre}\nprecio: {vProd[j].precio}\nunidad/s: {vProd[j].unidades}")
        
        if operacion == 2:
            delete=input(f"que producto deseas borrar: ")
            existe=False
            for x in range(0,len(vProd)):
                existe=True
            if existe:
                print(f"producto: {vProd[x].nombre}\nprecio: {vProd[x].precio}\nunidad/s: {vProd[x].unidades}")
                vProd.pop(x)
            else:
                print("no esxiste este producto")

                    
 

        
            
           
            
        

    
              
              
              
    
    
