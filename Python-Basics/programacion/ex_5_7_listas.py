"""
5.7 Crea un programa llamado ex_5_7, en el que el usuario introduzca una palabra o frase y el
programa diga si es palíndromo, es decir, si se lee igual hacia delante que hacia atrás. Por
ejemplo “amor a roma” y “ojo” son palíndromos.
"""
frase = input('Introduce una frase: ')
frase2 = ''
for c in frase:
  frase2 = c + frase2

if frase == frase2:
  print('La frase es palindroma')
else:
  print('La frase no es palindroma')
