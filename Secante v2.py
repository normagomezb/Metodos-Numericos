import math
import numpy as np

valor_pi = np.pi
a = 0.5
b = valor_pi/4
tolerancia = 0.001
No_iteraciones = 20

def Funcion(x):
    fun = math.cos(x) - x
    return(fun)
    
i = 2
if Funcion(a) > 0:
    p0 = b
    q0 = Funcion(a)
    q1 = Funcion(b)
    
else:
    p0 = a
    q0 = Funcion(b)
    q1 = Funcion(a)
    
while i <= No_iteraciones:
    if Funcion(a) > 0:
        p = p0 - (q1/q1 - q0) * (p0 - a)
    else:
        p = p0 - (q1/q0 - q1) * (b - p0)
        
    if abs(p - p0) < tolerancia:
        print('La solucion para p es: {0}'. format(p))
        break
    
    i = i + 1
    p0 = p
    q1 = Funcion(p)
    
    if i > No_iteraciones:
        print('Procedimiento completado sin exito')

