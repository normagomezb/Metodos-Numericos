import math
import numpy as np


def Funcion(x):
    fun = math.cos(x) - x
    return(fun)
valor_pi = np.pi

a = 0.5
b = valor_pi/2

tolerancia = 0.001
No_iteraciones = 20

i = 1

Fa = Funcion (a)

while i <= No_iteraciones:
    p = a + (b-a)/2
    Fp = Funcion (p)
    
    if Fp == 0 or ((b-a)/2) < tolerancia:
        print('La raiz solucion es {0}'.format(p))
        break
    
    if Fa*Fp > 0:
        a = p
        Fa = Fp
    
    else:
        b = p
    i = i + 1
    
    if i > No_iteraciones:
        print('Procedimiento completado sin exito')


