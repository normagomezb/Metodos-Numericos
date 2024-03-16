#Regla del trapesio: Cuando tendencia de datos es lineal, buena

def Trapecio (funcion, a, b, N):
    Fa = funcion(a)
    Fb = funcion(b)
    h = (b-a)/N
    sumatoria = 0
    for i in range(1, N):
        xi = a + i*h
        sumatoria += funcion(xi)
    I = h*(Fa + 2*sumatoria + Fb )/2
    return I

resultado = Trapecio(lambda x: x**2 -4*x +3, 0, 1, 1000)
print(resultado) 

