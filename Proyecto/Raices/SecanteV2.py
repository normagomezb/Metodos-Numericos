import numpy as np

def SecV2(funcion, a, b, No_iteraciones = 100, error_r = 0.001):
    Error = 101 
    i = 2
    Fa = funcion (a)
    if Fa > 0:
       p0 = b
       q0 = funcion(a)
       q1 = funcion(b)
    else:
        p0 = a
        q0 = funcion(b)
        q1 = funcion(a)
    while i <= No_iteraciones and Error >= error_r:
        if Fa > 0:
            p = p0 - (q1/q1 - q0) * (p0 - a)
        else:
            p = p0 - (q1/q0 - q1) * (b - p0)
        Error = abs(p - p0)/abs(p)*100
        if Error < error_r:
            print('La raiz solucion es: ', p)
            break
        i += 1
        p0 = p
        q1 = funcion(p)
        if i > No_iteraciones:
            print('Procedimiento completado sin exito')


#SecV2(lambda x: np.cos(x) - x, 0.5, np.pi/2, 1000, 0.001)
