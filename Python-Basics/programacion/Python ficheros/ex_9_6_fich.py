'''
9.6 Dado un fichero de texto que tan solo guarda las visitas a una página:

38

Escribe una función que abra un fichero de estas características, el nombre del cual le pasamos
como parámetro, e incremente su nombre de visitas. Si el fichero no existía lo creará con una
visita. La función retorna el nombre de visitas que hay en el fichero
'''
def visitas(File):
    file=open(File,'r+t')
    numVisitas=file.read()
    #vamos a aumentar las vivitas hasta 45
    vi=int(numVisitas)#hacemos que el numero formato string del archivo sea un entero
    for j in range(vi+1,50,1):
        file.write(str(j)+'\n')
    file.close()
    
print(visitas('visitas.txt'))
#no he logrado hacer que el 38 se separe del 39 
