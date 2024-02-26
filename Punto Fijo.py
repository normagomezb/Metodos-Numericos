import numpy as np

def Funcion(x):
    fun = np.cos(x) - x
    return(fun)
    

p0  = 1
tolerancia = 0.001
No_iteraciones = 20

i = 1

while i <= No_iteraciones:
    p = Funcion (p0)
    
    if abs(p - p0) < tolerancia:
        print('La solucion para p es: {0}'.format (p))
        break
    p0 = p
    i = i + 1
    
    if i > No_iteraciones:
        print('Procedimiento completado sin exito')

