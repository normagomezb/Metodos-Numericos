import numpy as np

def SecV1(funcion, p0, p1, No_iteraciones = 100, error_r = 0.001):
    Error = 101
    i = 2
    q0 = funcion (p0)
    q1 = funcion (p1)
    while i <= No_iteraciones and Error >= error_r:
        p = p1 - q1*(p1 - p0) /(q1 - q0)
        Error = abs(p - p1)/abs(p)*100
        if Error < error_r:
            print('La raiz solucion es: ', p)
            break
        i += 1
        p0 = p1
        q0 = q1
        p1 = p
        q1 = funcion(p)
        if i > No_iteraciones:
            print('Procedimiento completado sin exito')
   
#SecV1(lambda x: np.cos(x) - x, 0.5, np.pi/2, 100, 0.001)

