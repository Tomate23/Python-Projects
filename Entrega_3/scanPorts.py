import socket
#creating the socket
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

#scanning ports
def scanPort(host):
    ports = []
    for i in range (1,1025):
        try:
            mySocket2.bind(("host", "i"))
            ports.append("OPEN:"+str(i))
            mySocket2.close()
        except:
            ports.append("CLOSED:"+str(i))
    return ports
#connect the socket host and port
try:
    host = ""
    port = 8888
    mySocket.bind((host, port))
    print("Scoket connected to port: {}".format(port))
except socket.error as error:
    print("Something went wrong Error: {}".format(error))

#put the socket in listen mode
mySocket.listen(1)

#while loop, reciving and sending data - GET /scan.html HTTP/1.1
while True:
    client, add = mySocket.accept()#accpept the connection and create a new socket (client)
    msgHost = client.recv(1024)
    msgHost = msgHost.decode('utf-8')#this turn bytes into string
    #takin' what we need form the array...
    separate = msgHost.split("\n")
    url = separate[0]
    print(url)
    if url == "GET /scan.html?192.168.1.1 HTTP/1.1\r":
        client.send(b"GOOD: Page Scan found")
        Bytes = str.encode(str(scanPort("url")),'utf-8')
        client.send(Bytes)
    else:
        client.send(b"WRONG: Page not Found")
    client.close()
    #10.0.2.15
    #GET /scan.html?10.0.2.15 HTTP/1.1
    
