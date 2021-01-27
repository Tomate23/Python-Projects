'''
4. (2 punts) Un alumne d’informàtica vol realitzar estadístiques de les hores d’estudi
mensuals dedicades a cadascuna de les seves assignatures. Crea un programa que
donada la següent taula llegeixi les hores i calculi:

- El total anual d’hores dedicades a cada assignatura.
- El total mensual d’hores dedicades a estudiar.
'''
# Creamos la matriz 5x12 con valores iniciales de [0]

filas = 5
columnas = 12
matriz = []

for i in range (filas):
    matriz.append([0] * columnas)

# Pedimos al usuario los valores de la matriz
for f in range(filas): # recorre las 5 asignaturas
    for c in range(columnas): # recorre los 12 meses 
        matriz[f][c] = int(input(f"Introduce horas, para la asignatura:{f+1} del mes:{c+1}:\t"))
        
# Suma de filas y columnas, creamos dos vectores que contengan los resultados y al inicio estan en valor 0.0

suma_asig = [] # Este tendria las dimensiones de las asignaturas, es decir 5
for f in range(filas):
    suma_asig.append(0.0)
    
suma_mes = [] # Este tendria las dimensiones de los meses, las columnas = 12
for c in range(columnas):
    suma_mes.append(0.0)
    
for f in range(filas):
    for c in range(columnas):
        suma_asig[f] += matriz[f][c] # Suma el total de horas de cada asignatura en los 12 meses
        
        suma_mes[c] += matriz[f][c] # Suma el total de las horas de cada mes
        
    
print(f"Total de horas anuales dedicadas a cada asignatura:{suma_asig}")
print(f"Total mensual de horas dedicadas a estudiar :{suma_mes}")
    
    
    
    
    
    
    
    
    
    
    
    
    