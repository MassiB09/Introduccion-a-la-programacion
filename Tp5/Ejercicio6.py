'''Hora de jugar: Una calculadora tiene cuatro operaciones básicas (a saber: sumar, restar, 
multiplicar, dividir). Desarrolle una función para realizar cada operación, que reciba como 
parámetros dos números ingresados por el usuario y devuelva el resultado de la operación. 
Resuelva la división por restas sucesivas (investigar cómo se resuelve). 
Desarrollar un programa principal con un menú que permita realizar una operación y posea 
una opción para Salir. Luego de cada operación realizada se debe volver a presentar el menú'''

def suma(numero1 ,numero2):
    return numero1 + numero2

def resta(numero1, numero2):
    return numero1 - numero2

def multiplicacion(numero1, numero2):
    return numero1 * numero2

def division(numero1, numero2):
    contador = 0
    while numero1 >= numero2:
        numero1 -= numero2
        contador += 1
    return contador

flag = True
while flag:
    print('MENU:\n1.Suma\n2.Resta\n3.Multiplicacion\n4.Division (por restas sucesivas)\nIngresar -1 para finalizar el programa')
    numero = int(input('\nIngrese una opcion: '))
    if numero == 1:
        print('SUMA')
        numero1 = int(input('Ingrese un numero: '))
        numero2 = int(input('Ingrese otro numero: '))
        print(f'\nEl resultado es: {suma(numero1,numero2)}\n')
    if numero == 2:
        print('RESTA')
        numero1 = int(input('Ingrese un numero: '))
        numero2 = int(input('Ingrese el numero que va a restar: '))
        print(f'\nEl resultado es: {resta(numero1,numero2)}\n')
    if numero == 3:
        print('MULTIPLICACION')
        numero1 = int(input('Ingrese un numero: '))
        numero2 = int(input('Ingrese otro numero: '))
        print(f'\nEl resultado es: {multiplicacion(numero1,numero2)}\n')
    if numero == 4:
        print('DIVISION')
        numero1 = int(input('Ingrese el dividendo: '))
        numero2 = int(input('Ingrese el divisor: '))
        print(f'\nEl resultado es: {division(numero1,numero2)}\n')
    if numero == -1:
        flag = False
        print('Fin del programa')
    else:
        print('La opcion ingresada no es valida\n')



