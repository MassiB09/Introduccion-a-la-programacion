''' Escribir un algoritmo que lea números enteros hasta que se ingrese un 0, y muestre el máximo, 
el mínimo (sin considerar el 0) y la media (promedio) de todos ellos. Piense cómo debe 
inicializar las variables.'''

lista = []
mayor = 0
numero = -1
contador = 0

while numero != 0:
    numero = int(input('Ingrese un numero: '))
    lista.append(numero)

menor = lista[0]

for i in lista:
    if i > mayor:
        mayor = i
    elif i < menor and i != 0:
        menor = i

print(f'El promedio es: {sum(lista)/len(lista)}')
print(f'El mayor es: {mayor}')
print(f'El menor es: {menor}')