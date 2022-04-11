'''Leer 10 números enteros e imprimir el promedio, el mayor y en qué orden fue ingresado el 
mayor valor, si se ingresó más de una vez debe informar el primer ingreso.'''

lista = []
mayor = 0

for i in range(10):
    numero = int(input('Ingrese un numero: '))
    lista.append(numero)
    if mayor < numero:  
        mayor = numero
        indice = i + 1

promedio = sum(lista) / 10
print(f'El promedio es: {promedio}')
print(f'El mayor numero ingresado es: {mayor} y fue el {indice}° numero en ser ingresado')