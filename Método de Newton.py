import math

def Funcion(x):
    fun = math.cos(x) - x
    return(fun)
    
def DerivadaF(x):
    der = -math.sin(x) - 1
    return(der)

p0 = 1
tolerancia = 0.001
No_iteraciones = 20

i = 1
while i <= No_iteraciones:
    p = p0 - (Funcion(p0) / DerivadaF (p0))
     
    if abs(p - p0) < tolerancia:
        print('La solucion para p es: {0}'.format(p))
        break
    i = i + 1
    p0 = p
     
    if i > No_iteraciones:
        print('Procedimiento completado sin exito')
         

