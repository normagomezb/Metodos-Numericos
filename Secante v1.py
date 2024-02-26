import math
import numpy as np

valor_pi = np.pi
tolerancia = 0.001
No_iteraciones = 20
p0 = 0.5
p1 = valor_pi/4

def Funcion(x):
    fun = math.cos(x) - x
    return(fun)
    
i = 2

q0 = Funcion(p0)
q1 = Funcion(p1)

while i <= No_iteraciones:
    p = p1 - q1*(p1 - p0) /(q1 - q0)
    
    if abs(p - p1) < tolerancia:
        print('La solucion para p es: {0}'. format(p))
        break
    
    i = i + 1
    
    p0 = p1
    q0 = q1
    p1 = p1
    q1 = Funcion(p)
    
    if i > No_iteraciones:
        print('Procedimiento completado sin exito')
