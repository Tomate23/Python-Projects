'''
3. (2 punts) Escriu un programa que demana una cadena de caràcters i crea una nova
cadena canviant les vocals ‘A’ per ‘4’, ‘E’ per ‘3’, ‘I’ per ‘1’ i ‘O’ per ‘0’. A
continuació imprimeix la cadena per pantalla.
'''
cad1 = input("introduce frase, (LETRAS EN MAYUSCULAS):\t")
cad2 = '' # para crear la nueva cadena con los caracteres cambiados 
for i in cad1:
    if i == 'A':
        cad2 += '4'
    if i == 'E':
        cad2 += '3'
    if i == 'I':
        cad2 += '1'
    if i == 'O':
        cad2 += '0'
    else:
        cad2+=i
        
print(f"Frase introducida: {cad1}\n")
print(f"Frase con caracteres cambiados: {cad2}")


# En el examen se me olvido poner los numeros como strings, los deje como enteros.