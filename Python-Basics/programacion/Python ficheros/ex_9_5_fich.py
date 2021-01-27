'''
9.5 Dado un fichero de texto que guarda en líneas consecutivas nombres de alumnos y su nota:
Ana
7.5
Bob
10
Pep
4.95
Escribe una función que abra un fichero de estas características, el nombre del cual le pasamos
como parámetro, y retorne la nota media del grupo de alumnos. Si el fichero no existe o está
vacío lanza una excepción.
'''
def media(nombre_fichero):
  file = open(nombre_fichero, 'rt')
  n = 0#para contar las notas que hay(tres en este caso)
  suma = 0#para suamr las notas
  chivato = False#sabemos que las notas estan en una posicion entre medio de los nombre de los alumnos, el fichero inicia con el nombre de un alumno asi que or eso es false y sera false cada vez que sea un nombre y no una nota.
  for l in file:#recorremos el fichero
    if chivato:#dado que el valor del chivato es False, no entrara al bucle, eso nos conviene ya que el pimer valor es el nombre ana y no lo queremos 
      suma = suma + float(l)
      n = n + 1
    chivato = not chivato#sabemos que el segundo valor si es una nota y por eso cambiamos el False a True, asi esta nota que es un string se convierte es un float para poder operar con el
  file.close()
  return suma/n

print(media('notasAlumnos.txt'))



