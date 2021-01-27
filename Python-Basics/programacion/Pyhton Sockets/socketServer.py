# Program socket server
import socket
#creamos el socket con IPv4 y TCP
try:
    socketServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("socket creado satisfactoriamente")
except socket.error as error:
    print("Algo ha ido mal: ", error)

#todas las ip y el puerto
host = ''
port = 12345
#hacemos la union bind 
try:
    socketServer.bind((host,port))
    print("socket unido a: ", port)
except socket.error as error:
    print("has ha salido mal con bind() : ", error)
#ponemos el socket en modo listening
socketServer.listen(1)
#iniciamos el bucle infinito 
while True:
    #aceptamos y recibimos los datos que el cliente envia
    cliente, address = socketServer.accept()
    #recibimos el mensaje con recv()
    msgClient = cliente.recv(1024)
    #convertimos de bytes a str y *2
    msgClient = msgClient.decode('utf-8')
    msgToClient = int(msgClient) * 2
    msgToClient2= str(msgToClient)
    #pasamos a bytes el resultado
    msg=str.encode(msgToClient2, 'utf-8')
    #enviamos el mensaje 
    cliente.send(msg)
    cliente.close()
socketServer.close()



