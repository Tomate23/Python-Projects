import socket
import sys

# Create the socket 
def socket_create():
    """
    We create global varibales in order to not repeat write in the other unctions
    """
    try:
        global host
        global port
        global s
        host = '' # don't specify an addres because any client could connect to the server
        port = 9999
        s = socket.socket()
        print("The socket has been created!")
    except socket.error as msg:
        print("Socket creation error: {}".format(msg))


# Bind the socket to the port and wait for connection client
def socket_bind():
    try:
        global host
        global port
        global s
        print("Binding socket to port: {}".format(port))
        s.bind((host, port))
        s.listen(5)
    except socket.error as msg:
        print("Scoket binding Error: " + str(msg) + "\n" + "Retrying...")
        socket_bind()


# Establish a connection with client 
def socket_accept():
    conn, address = s.accept()
    print("Connection has been established | " + "IP: " + address[0] + "| Port " + str(address[1]))
    send_commands(conn)
    conn.close()

# Send commands
def send_commands(conn):
    while True:
        cmd = input() # input() allows us to write in the terminal
        if cmd == "quit":
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd, "utf-8"))
            client_response = str(conn.recv(1024), "utf-8")
            print(client_response, end="")


def main():
    socket_create()
    socket_bind()
    socket_accept()

main()
