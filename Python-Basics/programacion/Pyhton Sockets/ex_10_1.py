'''
10.1 Crea un programa llamado ex_10_1, que analice un rango de puertos TCP imprimiendo qué puertos están a la escucha.

Para ello puedes utilizar la instrucción socket.connect(…) de Python que si no se conecta a
un puerto lanza una excepción, o la instrucción socket.connect_ex(…) de Python que si no
se conecta a un puerto devuelve un código de error diferente de 0.

'''
import socket
#creamos el socket 
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#intentamos conectar con un servidor, para ver purtos 
ip=socket.gethostbyname('www.google.com')
port=80
sock.connect((ip,port))
sock.bind(('',ip))
sock.listen(5)
while True:
    clientsocket, address = sock.accept()
    print(address)
sock.close() 

import socket
ip = '127.0.0.1'
puertoI = 1
puertoF = 1024# el final es el 1024 porque es el puerto que usa el protocolo TCP
for p in range(puertoI, puertoF+1):
    try:

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, p))
        print('Puerto abierto:', p)
        s.close()
    except ConnectionRefusedError:
        pass

