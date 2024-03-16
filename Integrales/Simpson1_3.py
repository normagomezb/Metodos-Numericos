#Regla de Simpson (1/3)

def Simpson13 (funcion, a, b, N):
    Fa = funcion(a)
    Fb = funcion(b)
    h = (b-a)/N          #N = pares de paneles
    sumatoria1 = 0
    sumatoria2 = 0
    for i in range(1, N):  
        if i%2 != 0:
            xi = a + i*h
            sumatoria1 += funcion(xi)
        
        else:
            xi = a + i*h
            sumatoria2 += funcion(xi)
    I = h*(Fa + 4*sumatoria1 + 2*sumatoria2 + Fb)/3
    return I

resultado = Simpson13(lambda x: x**2 -4*x +3, 0, 1, 1000)
print(resultado) 
