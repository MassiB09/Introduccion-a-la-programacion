'''Leer dos números naturales A y B. Calcular AB mediante productos sucesivos y mostrar el 
resultado. Ejemplo: 4^3 = 4 * 4 * 4 (4 multiplicado 3 veces).'''

a = float(input('Ingrese el numero a multiplicar (natural): '))
b = float(input('Ingrese el numero de veces que se multiplicara (natural): '))
resultado = 0

if (a % 1 != 0 or b % 1 != 0) or (a <= 0 or b <= 0):
    print('Te volves a hacer el gracioso y te mato')
else:
    resultado = a * b
    print(f'El resultado es: {int(resultado)}')