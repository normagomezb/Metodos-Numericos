import numpy as np
import Biseccion
import NewtonRaph
import PuntoFijo
import SecanteV1
import SecanteV2

print('Encontar Raiz')
print('\n Acontinuacion se le pediran datos referentes a su funcion, '+
    'si no posee la informacion, escriba: N/A')
Fun = (input('Ingrese la funcion: '))
Deri = (input('Ingrese la Derivada de la funcion: '))
Punto_0 = (input('Ingrese un punto inicial: '))
Intervalo = (input('Quiere ingresar un intervalo, (SI, N/A): '))
if Intervalo == 'SI':
    global a,b
    a = float(input('Ingrese el numero de menor valor de su intervalo: '))
    b = float(input('Ingrese  la otra componente de su intervalo: '))
NumeroItera = (input('Ingrese el numero de iteraciones que quiere realizar: '))
Tolerancia = (input('Ingrese una tolerancia: '))
SiMetodo = ((input('¿Tiene un metodo por el cual quiera realizar la busqueda?(Si es asi escriba SI): ')))
if SiMetodo == 'SI':
    print(' Escriba el numero correspondiente al metodo que prefiera')
    print('Biseccion -   1')
    print('Punto Fijo -  2')
    print('Newton Raph - 3')
    print('Secante V1 -  4')
    print('Secante V2 -  5')
    Metodo = (input('Ingrese el método por el cual quiere encontar la raíz: '))
    
NA = 'N/A'

Funcion = lambda x: eval(Fun)

if Deri != NA:
    Derivada = lambda x: eval(Deri)
else:
    Derivada = Deri


while SiMetodo == NA :  
    if Punto_0 != NA:  
        if Derivada != NA:
            if NumeroItera != NA: #Numero de iteraciones en vez de E
                Resultado = NewtonRaph.NewtR(Funcion, Derivada, float(Punto_0), float(NumeroItera), 0.001)
                break
            elif Tolerancia != NA:                 #Ep en vez de Numero de tolerancia
                Resultado = NewtonRaph.NewtR(Funcion, Derivada, float(Punto_0), 10000, float(Tolerancia))
                break
            else:
                print('No se puede encontar la raiz con los datos proporcionados')
                break
        else:
            print('No se puede encontar la raiz con los datos proporcionados')
            break
    elif Intervalo != NA:  #Si no tiene punto, tiene intervalo
        if Derivada != NA:
            if NumeroItera != NA: #Numero de iteraciones en vez de E
                Punto_0 = Biseccion.Bisec(Funcion, a, b, 1000, 0.001)
                Resultado = NewtonRaph.NewtR(Funcion, Derivada, Punto_0, float(NumeroItera), 0.001)
                break
            elif Tolerancia != NA:                 #Ep en vez de Numero de tolerancia
                Punto_0 = Biseccion.Bisec(Funcion, a, b, 10000, 0.001)
                Resultado = NewtonRaph.NewtR(Funcion, Derivada, Punto_0, 1000, float(Tolerancia))
                break
            else:
                print('No se puede encontar la raiz con los datos proporcionados')
                break
        else:
            if NumeroItera != NA:
                Resultado = Biseccion.Bisec(Funcion, a, b, float(NumeroItera), 0.001)
                print('La raiz solucion es: ', Resultado)
                break
            elif Tolerancia != NA:
                Resultado = Biseccion.Bisec(Funcion, a, b, 10000, float(Tolerancia))
                print('La raiz solucion es: ', Resultado)
                break
            else:
                print('No se puede encontar la raiz con los datos proporcionados')
                break
    else:
        print('No se puede encontar la raiz con los datos proporcionados')
        break


while SiMetodo != NA:
    if Metodo == '1':  #Biseccion
        if Derivada == NA:
            if Intervalo != NA:
                if NumeroItera != NA: #Numero de iteraciones en vez de E
                    Resultado = Biseccion.Bisec(Funcion, a, b, float(NumeroItera), 0.001) 
                    print('La raiz solucion es: ', Resultado)
                    break
                elif Tolerancia != NA:                 #Ep en vez de Numero de tolerancia
                    Resultado = Biseccion.Bisec(Funcion, a, b, 10000, float(Tolerancia))
                    print('La raiz solucion es: ', Resultado)
                    break
                else:
                    print('No se puede encontar la raiz con los datos proporcionados')
                    break
            else:
                print('No se puede encontar la raiz con los datos proporcionados')
                break
        else:
            print('No se puede encontar la raiz con los datos proporcionados')
            break
    elif Metodo == '2':#Punto Fijo
        if Punto_0 != NA:
            if NumeroItera != NA:
                print(Funcion, Punto_0, NumeroItera)
                Resultado = PuntoFijo.PuntoF(Funcion,float(Punto_0), float(NumeroItera),0.001)
                print('La raiz solucion es: ', Resultado)
                break
            elif Tolerancia != NA:
                Resultado = PuntoFijo.PuntoF(Funcion, float(Punto_0), 1000, float(Tolerancia))
                print('La raiz solucion es: ', Resultado)
                break
            else:
                print('No se puede encontar la raiz con los datos proporcionados')
                break
        else:
            print('No se puede encontar la raiz con los datos proporcionados')
            break        
    elif Metodo == '3':  #Newton Raphson
        if Derivada != NA:
            if Intervalo != NA:
                if NumeroItera != NA: #Numero de iteraciones en vez de E
                    Punto_0 = Biseccion.Bisec(Funcion, a, b, 10000, 0.001) 
                    Resulatado = NewtonRaph.NewtR(Funcion, Derivada, float(Punto_0), float(NumeroItera), 0.001)
                    break
                elif Tolerancia != NA:                 #Ep en vez de Numero de tolerancia
                    Punto_0 = Biseccion.Bisec(Funcion, a, b, 10000, 0.001)
                    Resultado = NewtonRaph.NewtR(Funcion, Derivada, float(Punto_0), 10000, float(Tolerancia))
                    break
                else:
                    print('No se puede encontar la raiz con los datos proporcionados')
                    break
            elif Punto_0 != NA:
                if NumeroItera != NA: #Numero de iteraciones en vez de E
                    Resulatdo = NewtonRaph.NewtR(Funcion, Derivada, float(Punto_0), float(NumeroItera), 0.001)
                    break
                elif Tolerancia != NA:                 #Ep en vez de Numero de tolerancia
                    Resultado = NewtonRaph.NewtR(Funcion, Derivada, float(Punto_0), 1000, float(Tolerancia))
                    break
                else:
                    print('No se puede encontar la raiz con los datos proporcionados')
                    break
            else:
                print('No se puede encontar la raiz con los datos proporcionados')
                break
        else: 
            print('No se puede encontar la raiz con los datos proporcionados')
            break
    elif Metodo == '4':  #Secante V1
        if Intervalo != NA:
            if NumeroItera != NA:
                Resultado = SecanteV1.SecV1(Funcion, a, b, float(NumeroItera), 0.001)
                break
            elif Tolerancia != NA:
                Resultado = SecanteV1.SecV1(Funcion, a, b, 1000, float(Tolerancia))
                print('La raiz solucion es: ', Resultado)
                break
            else:
                print('No se puede encontar la raiz con los datos proporcionados')
                break
        else:
            print('No se puede encontar la raiz con los datos proporcionados')
            break
    elif Metodo == '5':  #Secante V2
        if Intervalo != NA:
            if NumeroItera != NA:
                Resultado = SecanteV2.SecV2(Funcion, a, b, float(NumeroItera), 0.001)
                print('La raiz solucion es: ', Resultado)
                break
            elif Tolerancia != NA:
                Resultado = SecanteV2.SecV2(Funcion, a, b, 1000, float(Tolerancia))
                print('La raiz solucion es: ', Resultado)
                break
            else:
                print('No se puede encontar la raiz con los datos proporcionados')
                break
        else:
            print('No se puede encontar la raiz con los datos proporcionados')
            break
    else:
        print('La opcion seleccionada no esta en la lista, verifique su respuesta')
        break
    

#Acomoda en __int__
#Probar que funcione en paquete





