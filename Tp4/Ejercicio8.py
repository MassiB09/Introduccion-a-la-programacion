'''Ingresar por teclado la cantidad de términos a generar de la siguiente serie: 
1 7 19 43 91 187 379 763 1531 3067 6139 
El primer término es el 1 y cada término se genera como el doble del término anterior más 5. 
Mostrar la serie por pantalla e informar la suma de los términos generados.'''


cantidad = int(input('Ingrese la cantidad de terminos a generar: '))
lista = [1]
numero = 1

for i in range(cantidad):
    numero = numero * 2 + 5
    lista.append(numero)

for i in range(len(lista) - 1):
    numero = lista[i]
    print(numero)