'''Desarrollar dos funciones
1) Función para sumar los dígitos de un número. Recibe un número y retorna la suma de los
dígitos. (NO utilizar cadenas de caracteres str, para lograr el objetivo)
2) Extraer un dígito de un número. La función recibe como parámetros dos números enteros, 
uno será del que se extraiga el dígito y el otro indica qué cifra se desea obtener. La cifra 
de la derecha se considera la número 0. Retornar el valor -1 si no existe el dígito solicitado. 
Tener en cuenta que el número puede ser positivo o negativo. Ejemplo: 
extraerdigito(12345, 1) devuelve 4, y extraerdigito(12345, 8) devuelve -1.
Desarrollar un programa para generar valores al azar de 5 dígitos hasta que el dígito central 
sea cero. Mostrar por pantalla este número y la suma de sus dígitos utilizando ambas funciones 
creadas y no olvidar mostrar un título al inicio utilizando la función del ejercicio 3'''
from Ejercicio3 import titulo_asteriscos
import random

def sumar_digitos(numero):
    suma = 0
    while numero != 0:
        suma += numero % 10
        numero = numero // 10
    return suma

def extraer_digito(numero,digito):
    divisor_entero = 1
    aux = numero
    contador = 0
    for i in range(digito + 1):
        divisor_entero = divisor_entero * 10
    while aux >= 10:
        contador +=1
        aux = aux // 10
    if digito <= contador:
        resultado = numero % divisor_entero
        resultado = resultado // (divisor_entero / 10)
        return int(resultado)
    else:
        return -1

print(titulo_asteriscos('Suma de digitos', 25))

numero = 0
contador = 0

while extraer_digito(numero,2) != 0:
    numero = random.randint(10000,99999)
    contador += 1

print(f'El programa se ejecuto {contador} veces')
print(f'El numero es: {numero} y la suma de sus digitos es: {sumar_digitos(numero)}')