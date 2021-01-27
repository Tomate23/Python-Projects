'''
5. (3 punts) Crea un programa que empri estructures i vectors per emmagatzemar les
dades personals dels alumnes. De cadascun d’ells guardarem el nom, i las notes
obtingudes a cinc exàmens. El programa calcularà i guardarà la nota final com la
mitja de les cinc anteriors.
L’aplicació demana a l’usuari el nombre d’alumnes amb els que treballarà i les
dades de cadascun d’ells. A continuació, calcula la nota final de tots els alumnes i
visualitza el nom i la nota final de tots els alumnes.

(1 punt) Declarar els nous tipus Alumne i qualsevol altre tipus que sigui necessari
(1 punt) Llegir el nom i les notes dels alumnes
(1 punt) Recórrer el vector d’alumnes per calcular la mitja, i imprimir els resultats
'''
# Pedimos al usuario en numero de alumno/as y sus notas que son 5
num_alum = int(input("Cuantos alumnos:"))
num_notas = 5


# Creamos la clase alumnos
class Alumno():
    def __init__(self):
        self.nombre = ''
        self.nota = [0.0]*num_notas #pongo num_notas porque es el numero de notas a guardar de cada alumno/a
        self.final = 0.0
        
# Creo un vector donde guardar a los alumnos y sus datos
clase = []


# Para cada alumno pedimos sus datos, usamos un bucle for para recorrer
for i in range(num_alum):
    a = Alumno() #creamos una variable de tipo alumno para poder acceder a sus datos.
    a.nombre = input(f"Alumno/a:{i+1}, introduce el nombre:\t") # pedimos el nombre del alumno/a
    # para pedir las notas recorremos el vector notas
    for j in range(num_notas):
        nt = float(input(f"Alumno/a:{i+1}, introduce notas:\t")) # pedimos las notas
        a.nota[j] = nt # guardamos las notas en el vector nota
    clase.append(a) # guardamos cada alumno en el vector clase
    
    
# Calculo de las notas finales y la media
for i in range(0, len(clase)):
    for j in range(0, len(clase[i].nota)):
        clase[i].final = clase[i].final + float(clase[i].nota[j]) # suma las notas
    clase[i].final = clase[i].final / len(clase[i].nota) # calcula la media de las notas
    
    # Imprimimos el resultado
    print(clase[i].nombre , '-' , clase[i].final)


    
    
    
    
    
    
    
    
    
    
    
    
        