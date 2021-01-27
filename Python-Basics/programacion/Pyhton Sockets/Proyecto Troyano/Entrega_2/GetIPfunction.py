import socket
def GetIP():
    device_name = socket.gethostname()
    print("Device Name: {}".format(device_name))
    ip_device = socket.gethostbyname(device_name)
    print("Device IP address: {}".format(ip_device))
    return(device_name,ip_device)
GetIP()