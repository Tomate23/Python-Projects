#Programa para abrir un fichero y ver su len()

'''
#funciones sobre ficheros:

fichero = open(nombre, modo)  # abre el fichero con dicho nombre
with open(nombre) as fichero: # abre el fichero con dicho nombre
fichero.close()               # cierra el fichero
var = fichero.read()          # lee todo el contenido del fichero
var = fichero.readline()      # lee una línea del fichero
for linea in fichero:         # lee todo el fichero, línea a línea
fichero.write(var)            # escribe contenido en el fichero
print(var, file=fichero)      # escribe contenido en el fichero
fichero.truncate()            # vacía el fichero
fichero.seek(bytes)           # se mueve a la posición indicada
fichero.tell()                # retorna la posición en el fichero

#Los modos de apertura de un fichero son:

'r'  → abre el fichero al inicio para la lectura
'r+' → abre el fichero al inicio para la lectura y escritura
'a'  → abre el fichero al final para añadir
'w'  → vacía o crea el fichero para la escritura
't'  → indica que el fichero es de texto
'b'  → indica que el fichero es binario
'''
file=open('fichero.txt','rt')#primero simpre hay que abrir el fichero (con su extension). el segundo param varia de lo que queramos hacer
datos=file.read()
pos=file.tell()
plus="that was an exit"
add=file.write(plus)#no tiene permiso de escritura
print(f"contenido del fichero: {datos} {add}\nposicion: {pos}")
print(f"el fichero de entrada mide : {len(datos)} bytes")
file.close()

#los ficheros al igual que las listas e strings podemos recorrerlos en un bucle for para ver su contenido:
#por ejemplo si queremos que el contenido de un fichero se pase a otro, calro!! en el segundo fichero ponemos el valor de escritura para poder insertar los datos.
file=open('fichero','rt')
fie2=open(''fichero2,'wt')
for i in (file):
    file2.write(i)
    #de esta forma recorremos el filey para cada elemento dentro de este (i) lo metemos dentro de file2
file.close()
file2.close()
#para generar un fichero usamos el modo de apertura w->write de esta froma:
file = open('multiplos.txt', 'wt')#en este caso se creara un fichero llamado multiplos.txt.

    








