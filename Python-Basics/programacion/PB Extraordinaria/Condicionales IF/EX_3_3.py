'''
 Crea un programa llamado ex_3_3, que pida una contraseña por teclado e indique si es correcta
o incorrecta. La contraseña correcta es “iloveyou123”.
'''
passwd = 'iloveyou123'
intentos = 3
while intentos != 0:
    passwd_user = input("Introduce la contraseña:\n")
    if passwd_user == passwd:
        print(f"Contraseña correcta: {passwd}", end="")
    intentos-=1
    print(f"te quedan: {intentos} intentos")
    if intentos == 0:
        print("has agotado tus intentos")
        break
        