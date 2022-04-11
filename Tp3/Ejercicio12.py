'''Ingresar un número n, validar que sea positivo. Luego: 
a) Mostrar los primeros n números impares hasta el número ingresado.
Ejemplo:
• Si se ingresa 5, se debe mostrar 1 3 5
• Si se ingresa 8, se debe mostrar 1 3 5 7
• Si se ingresa -5, se debe pedir otro número.
b) Informar la suma de esos números impares.'''

numero = -1
suma = 0

while numero <= 0:
    print('El numero tiene que ser positivo')
    numero = int(input('Ingresar un numero: '))

for i in range(numero):
    if (i + 1) % 2 != 0:
        print(i + 1)
        suma += i + 1 

print(f'La suma es: {suma}')