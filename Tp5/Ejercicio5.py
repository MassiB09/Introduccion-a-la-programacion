'''Desarrollar dos funciones:
1) Diseñar una función que solicite por teclado un número y lo retorne solo si el número 
ingresado es natural, caso contrario la función deberá seguir solicitando el número.
2) Función para sumar los primeros N números naturales de un valor. Retorna la suma.
Desarrollar un programa principal para ingresar una cantidad de valores naturales (la cantidad 
se solicita al usuario). Para cada valor informar la suma de los primeros N valores naturales.
Al finalizar informar cuántos valores se ingresaron y cuál es el mayor valor ingresado.'''

def Es_natural(numero):
    if numero > 0 and numero % 1 == 0:
        return True
    else:
        return False

def Suma_naturales(numero):
    suma = 0
    while Es_natural(numero):
        suma += numero
        numero -= 1
    return suma

cantidad = int(input('Ingrese la cantidad de valores: '))
mayor = 0
for i in range(cantidad):
    numero = int(input('Ingrese un numero natura: '))
    while not Es_natural(numero):
        print('El numero no es natural!!')
        numero = int(input('Ingrese un numero natura: '))
    if numero > mayor:
        mayor = numero
    suma = Suma_naturales(numero)
    print(f'La suma de los n es: {suma}')

print(f'Se ingresaron {cantidad} valores')
print(f'El mayor valor ingresado es: {mayor}')