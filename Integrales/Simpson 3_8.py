#Regla de Simpson (3/8)

def Simpson38 (funcion, a, b, N):
    Fa = funcion(a)
    Fb = funcion(b)
    h = (b-a)/N
    sumatoria1 = 0
    sumatoria2 = 0
    sumatoria3 = 0
    for i in range(1, N):
        xi = a + i * h
        if i % 3 == 0:
           sumatoria3 += funcion(xi)
        elif i % 3 == 1:
            sumatoria1 += funcion(xi)
        else:
            sumatoria2 += funcion(xi)
    I = (3 * h / 8) * (Fa + 3*sumatoria1 + 3*sumatoria2 + 2*sumatoria3 + Fb)
    return I

resultado = Simpson38(lambda x: x**2 - 4*x + 3, 0, 1, 1000)
print(resultado)


