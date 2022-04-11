'''Leer dos números A y B (enteros positivos). Calcular el producto A * B por sumas sucesivas e 
imprimir el resultado. Ejemplo: 4*3 = 4 + 4 + 4 (4 sumado 3 veces).'''

a = int(input('Ingrese el numero a sumar: '))
b = int(input('Ingrese el numero de veces que se sumara: '))
resultado = 0

if a < 0 or b < 0:
    print('Amigo dejate de joder')
else:
    for i in range(b):
        resultado += a
    print(f'El resultado es: {resultado}')
