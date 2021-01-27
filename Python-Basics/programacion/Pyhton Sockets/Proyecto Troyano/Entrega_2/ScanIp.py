import socket
import keyboard as key

try:
    socketTroy = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    socketTroy.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
    print("***Socket has been created***")
except socket.error as Error:
    print("Scoket couldn't be created Error:{}".format(Error))

message = (b"Hello Troyan! From Client")
port = 8888
address = ("127.0.0.1", port)
try:
    conn8888 = socketTroy.sendto(message, address)
    print("You're connected to port: {}\n".format(port))
except Exception as errorCon:
    print("couldn't do the connection: {}".format(errorCon))
try:
    print("Receiving data...")
    print("Taking the Device_s ip...")
    print("Device_IP info saved...\n")
    data ,server = socketTroy.recvfrom(1024)
    print(data)
    with open("IP_s.txt","a") as IPfile:
        """
        el archivo se creara en /home, porque no hay ruta especifica.
        """
        IPfile.write(str(data)+'\n')
    #si todo esta bien deberia haber creado el IPs.txt 
    #y meter la ip y el nombre del dispositivo dentro
except Exception as errorBro:
    print(errorBro)
key.write("Everything went allright\n", delay=0.1)#para ejecutar esto necesitas ejecutarlo con sudo
