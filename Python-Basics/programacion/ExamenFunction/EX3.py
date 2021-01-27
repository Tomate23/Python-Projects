# Ejercicio 3
# Dibuja el árbol de llamadas recursivas para T4(2), según la implementación:
def T(n,x):
    if n == 0:
        return 1
    if n == 1:
        return x
    return 2*x*T(n-1, x) - T(n-2,x)
print(T(4, 2))
'''
                    
T(0, 2)          T(4, 2)
   \              |    \
    T(2, 2) -- T(3, 2)  T(2, 2) -- T(1, 2)
   /          /            |         |   
T(1, 2)  T(1, 2)         T(0, 2)   T(0, 2)  
   |        |    
T(0, 2)  T(0, 2)   
             
             
'''