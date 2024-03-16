# Regla del Punto Medio

def PuntoM (funcion, a, b, N):
    h = (b-a)/N
    sumatoria = 0
    for i in range(1, N):
        xih = a + i*h + (h/2)
        sumatoria += funcion(xih)
        I = h*sumatoria  
    return I    
    
resultado = PuntoM(lambda x: x**2 -4*x +3, 0, 1, 1000)
print(resultado)

