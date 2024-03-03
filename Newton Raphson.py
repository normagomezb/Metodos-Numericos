import numpy as np

def NewtR(funcion, derivada, p0, No_iteraciones = 100, erro_r = 0.001):
    i = 1
    Error = 101
    while i <= No_iteraciones and (Error >= erro_r):
        p = p0 - (funcion(p0) / derivada(p0))
        Error = abs(p - p0)/abs(p)*100
        if Error < erro_r:
            print('La raiz solucion es: ', p)
            break
        i += 1
        p0 = p
        if i > No_iteraciones:
            print('Procedimiento completado sin exito')
         
NewtR(lambda x: np.cos(x)-x, lambda x: -np.sin(x)-1, 10, 1000, 0.001)
