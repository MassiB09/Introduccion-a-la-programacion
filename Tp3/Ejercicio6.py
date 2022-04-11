'''Ingresar números, hasta que la suma de los números pares supere 100. Mostrar Cuántos 
números en total se ingresaron.'''

numero = 0
suma = 0
contador = 0

while suma <= 100:
    numero = int(input('Ingrese un numero: '))
    if numero%2 == 0:
        suma = suma + numero
    contador = contador + 1
print(f'Se ingresaron {contador} numeros')
