'''L'exercici per fer aquesta setmana, prèvia a l'inici del projecte, és aquest: 
Crea un programa client i un programa servidor que faran el següent: 
- El programa client es connecta a un servidor, li envia un número, rep la resposta, i la imprimeix. 
- El programa servidor rep un número del client que es connecta, i li reenvia aquest número multiplicat per dos. 
Intenta fer-lo sense mirar els programes d'exemple dels apunts. Si et veus perdut, 
llavors agafa els programes d'exemple dels apunts i adapta'ls a que facin això que et demanen. 
Si a casa tens dos ordinadors, prova el client i servidor a diferents ordinadors. Si no, prova'ls al mateix ordinador.'''
# Programa socket Cliente
import socket
#Creamos un objeto socket para el servidor. Podemos dejarlo sin parametros pero si 
#quieren pueden pasarlos de la manera server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Nos conectamos al servidor con el metodo connect. Tiene dos parametros
#El primero es la IP del servidor y el segundo el puerto de conexion
s.connect(("127.0.0.1", 12345))
mensaje = input("numero Cliente:")
#Creamos un bucle para retener la conexion
while True:
    #Instanciamos una entrada de datos para que el cliente pueda enviar mensajes
    msg=str.encode(mensaje, 'utf-8')
    #Con la instancia del objeto servidor (s) y el metodo send, enviamos el mensaje introducido
    s.send(msg)
    break
print("Server say: ", s.recv(1024))
#Cerramos la instancia del objeto servidor
s.close()


