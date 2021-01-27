'''
2. (2 punts) Fes un programa que calculi i imprimeixi per pantalla totes les taules de
multiplicar des del 0 fins al 9, separant les diferents taules per una línia de guions:
'''
for i in range(10):
    for j in range(10):
        producto = i * j
        print(producto)
        if j == 9: # para separar cada tabla por un linea de guiones
            print("*************************")