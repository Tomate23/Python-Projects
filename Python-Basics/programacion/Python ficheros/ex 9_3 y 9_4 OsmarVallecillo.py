"""
9.3 Crea un programa llamado ex_9_3, que pida el nombre de un fichero de texto, y reescriba el
contenido de dicho fichero en otro fichero, convirtiendo todo el texto leído a mayúsculas.
"""
fich1=input("introduce fichero.txt: ")
fich2=input("introduce fichero.txt: ")

dato1 = open(fich1, 'rt')
dato2 = open(fich2, 'wt')
for i in dato1:
  dato2.write(i.upper())
dato1.close()
dato2.close()

"""
9.4 Crea los siguientes programas:
a) Un programa llamado ex_9_4_a que genere un fichero llamado “multiplos.txt” con los diez
primeros múltiplos de 5.
b) Un programa llamado ex_9_4_b que lee el contenido del fichero “multiplos.txt” y lo
imprime por pantalla.
c) Un programa llamado ex_9_4_c que añade al fichero “multiplos.txt” los diez siguientes
múltiplos de 5. Para ello el programa deberá averiguar cuál fue el último número escrito.
"""
#ex_9_4_a
fich = open('multiplos.txt', 'wt')

for i in range(1*5, 11*5, 5):
  fich.write(str(i)+'\n')
fich.close()

#ex_9_4_b

fich2 = open('multiplos.txt', 'rt')

for j in fich2:
  i = int(j)
  print(i)

fich2.close()

#ex_9_4_c

fich3 = open('multiplos.txt', 'r+t')

for k in fich3:
  i = int(k)
  print(i)

print('añadiendo del 50 al 100')
  
for n in range(i+5, i+55, 5):
  fich3.write(str(n)+'\n')

fich3.close()







