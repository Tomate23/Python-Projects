#vamos a intentar hacer un socket que conecte con google (SOCKET CONNECT TO SERVER)
import socket
#creamos el socket 
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket has been successfully created")
except socket.error  as error:
    print(f"Socket creation has filed, Error: {error}")

# default port for socket 
port = 80

#cogemos la ip host, es la de google.
try:
    ip_host = socket.gethostbyname('www.google.com')
except socket.gaierror:
    #This exception is raised for address-related errors

    # this means could not resolve the host 
    print ("there was an error resolving the host")

#connection to the server
s.connect((ip_host,port))

print(f"the socket has successfully connected to google on port {ip_host}")

