#Regla de boole

def Boole(funcion, a, b, N):
    Fa = funcion(a)
    Fb = funcion(b)
    h = (b - a) / N  
    sumatoria1 = 0
    sumatoria2 = 0
    for i in range(1, N):
        xi = a + i * h
        if i % 2 == 0:
            sumatoria1 += funcion(xi)
        else:
            sumatoria2 += funcion(xi)
    xhn = a + h*(N - 1)
    I = (2 * h / 45) * (7 * Fa + 32 * sumatoria2 + 12 * sumatoria1 + 14 * funcion(xhn) + 7*Fb)
    return I

resultado = Boole(lambda x: x**2 - 4*x + 3, 0, 1, 1000)
print(resultado)



