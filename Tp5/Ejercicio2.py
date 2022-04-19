'''Diseñar una función que reciba dos números enteros como parámetros enteros A y B, y permita 
obtener AB mediante multiplicaciones sucesivas.
Desarrollar un programa principal para generar N veces dos valores al azar en un rango desde-hasta ingresado por teclado y calcular AB, 
mostrar por pantalla los valores creados y el resultado de la operación.'''
import random

def multiplicacion(A,B):
    resultado = 1
    for i in range(B):
        resultado *= A
    return resultado

n = int(input('Ingrese un numero: '))
desde = int(input('Ingrese el limite inferior: '))
hasta = int(input('Ingrese el limite superior: '))

for i in range(n):
    A = random.randint(desde, hasta)
    B = random.randint(desde, hasta)
    resultado = multiplicacion(A, B)

    print(f'El primer numero es: {A}')
    print(f'El segundo numero es: {B}')
    print(f'El resultado es: {resultado}')
