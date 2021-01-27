import socket
from tkinter import *
from tkinter.ttk import *

# Entorno tkinter
root = Tk()
root.title("Socket's Connesction")
root.geometry('500x300')


# Creacio del Socket
try:
    mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
    Label(root, text="El socket ha sido creado!").grid(row=0, column=0)
except socket.error as ErrorCreation:
    Label(root, text="El socket no puedo ser credo!", fg="red").grid(row=0, column=0)


# Bind the socket to a port
def connSock(host):
    try:
        port = 80
        conn80 = mySocket.bind((host, port))
        Label(root, text="Socket binded to port 80!").grid(row=1, column=0)
    except:
        port = 8888
        conn8888 = mySocket.bind((host, port))
        Label(root, text="Socket binded to port 8888!").grid(row=1, column=0)
connSock('')
root.mainloop()
