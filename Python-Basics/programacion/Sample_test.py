class Hora:
    def __init__(self):
        self.hora= 0
        self.minutos= 0
        
class Paciente():
    def __init__(self):
        self.nombre= ""
        self.llegada= Hora()
        
class ListaPacientes:
    def __init__(self):
        #self.pacientes= []
        self.doctor= ""
        
pacientes=[]

while True:
    print('---------------------------------------------')
    print('1. introducir paciente')
    print('2. lista de pacientes')
    print('3. Modificar lista de pacientes')
    print('0. Salir')
    print('---------------------------------------------')

    opcion = input('¿Qué opción quieres? ')
    print('\n\n\n')
#añadir pacientes si  comprobar si ya estan en la lista.
    nombres=Paciente()
    #lista=ListaPacientes()
    i=0
    if opcion=="1":
    
        print("AÑADIR PACIENTES!!!\n\n")
        numpaci=int(input("cuantos pacientes deseas añadir? "))
        for i in range (numpaci):
            nombres.nombre=input(f"introduce el nombre del paciente {i+1}: ")
            nombres.llegada.hora=input(f"introduce la hora a la que llego el paciente {i+1}: ")
            nombres.llegada.minutos=input(f"introduce los minutos en los que llego el paciente {i+1}: ")
            pacientes.append(nombres)
        
    elif opcion=="2":
        
        print("LISTA DE PACIENTES!!!\n\n")
        
        for nombres in pacientes:
            print("*****************************************************************************")
            print(f"paciente: {nombres.nombre}    llego a las: {nombres.llegada.hora} horas    y {nombres.llegada.minutos} minutos")
            print("*****************************************************************************")
            print('\n\n\n')


            
"""

#ex2

# a) mostrar la cantidad de pacientes que hay
print(len(lista.pacientes))

# b) muestra a que hora llego el ultimo paciente
print(len(lista.paciente[len(lista.pacientes)-1])).llegada.hora

"""



