#Regla del rectangulo

def Rectangulo(funcion, a, b, N):
    sumatoria = 0
    h = (b-a)/N
    for i in range(1, N):
        xi = a + i*h
        sumatoria += funcion(xi)
    I = h*sumatoria
    return I 

#resultado = Rectangulo(lambda x: x**2 -4*x +3, 0, 1, 1000)
#print(resultado)

