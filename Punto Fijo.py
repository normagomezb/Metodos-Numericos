import numpy as np

def PuntoF(funcion, p0, No_iteraciones =100, error_r = 0.001):
    i = 1
    Error = 101
    while i <= No_iteraciones and Error >= error_r:
        p = funcion (p0)
        Error = abs(p - p0)/abs(p)*100
        if Error < error_r:
            print('La raiz solucion es: ', p)
            break
        p0 = p
        i += 1
        if i > No_iteraciones:
            print('Procedimiento completado sin exito')
    
PuntoF(lambda x: np.cos(x), 10, 100,0.001)
