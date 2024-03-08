import numpy as np

print(" ")

def Bisec(funcion, a, b, No_iteraciones = 100, error_r = 0.001):
    #Valores
    Error = 101
    i = 1
    Fa = funcion(a)
    Fb = funcion(b)
    if Fa * Fb < 0:
        #Calcular soluc
        while i <= No_iteraciones and Error >= error_r:
            p = (a + b)/2
            Fp = funcion (p)
            Error = abs(p - a)/abs(p) * 100
            if Fp == 0 or ((b-a)/2) < error_r:
                No_iteraciones=0
                Error = error_r
                return p
            if Fa*Fp > 0:
                a = p
                Fa = Fp
            else:
                b = p
                Fb = Fp
            i += 1
        if i > No_iteraciones:
            print('Procedimiento completado sin exito')
 
#Bisec(lambda x: np.sin(x)-x/2, 1, 3, 20, 0.001)

#Bisec(lambda x: np.cos(x)-x, 0.5, np.pi/2, 20, 0.001)


