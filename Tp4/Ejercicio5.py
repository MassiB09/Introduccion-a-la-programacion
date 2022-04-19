'''El factorial de un número entero N mayor que cero se define como el producto de todos los 
enteros X tales que 0 < X <= N. Desarrollar un programa para calcular el factorial de un número 
dado hasta ingresar -1. Deberán rechazarse las entradas inválidas (menores que 0). Al finalizar 
informar cuantas veces se calculó el factorial'''

numero = 0
factorial = 1
contador_factorial = -1

while numero != -1:
    numero = int(input('Ingrese el numero: '))
    if numero < 0 and not(numero == -1):
        print('El numero tiene que ser mayor que 0!!')
    else:
        while numero >= 1:
            factorial = factorial * numero
            numero -= 1
        contador_factorial += 1
        if numero != -1:
            print(f'El factorial es: {factorial}')
            factorial = 1

print(f'La cantidad de veces que se calculo el factorial es: {contador_factorial}')
