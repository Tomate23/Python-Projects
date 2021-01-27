'''
9.7 Dado un fichero de texto “matriz.txt” que guarda en la primera línea las dimensiones de la
matriz (filas y columnas) y en líneas consecutivas los elementos de la matriz:
3 4
2 0 3 -1
3 -2 10 9
5 1 7 7
(a) Escribe el código de un programa que lea una matriz del fichero.
(b) Escribe el código de un programa que escriba una matriz en el fichero.
'''
file=open('matriz.txt','r')
line=file.readline(3)
print(line)
file.close()