'''Leer tres números D, M y A correspondientes al día, mes y año de una fecha, y un número 
entero N que representa una cantidad de días. Realizar un programa que imprima la nueva 
fecha que resulta de sumar N días a la fecha dada. Tener en cuenta los años bisiestos tal como 
se detalla en el ejercicio 9 de la práctica 3.'''

def anio_bisiesto(anio):
    if anio % 4 == 0 and anio % 100 == 0 and anio % 400 == 0:
        return True
    elif anio % 4 == 0 and not(anio % 100 == 0):
        return True
    else:
        return False

d = int(input('Ingrese el dia: '))
m = int(input('Ingrese el mes: '))
a = int(input('Ingrese el año: '))

n = int(input('Ingrese el numero de dias que quiere avanzar en el tiempo: '))

anios =  n // 365
for anio in range(anios):
    if anio_bisiesto(anio + 1):
        n -= 1

n = n % 365
meses = n // 30
n = n % 30
dias = n
if dias + d > 30:
    dias -= 30
    meses += 1
    if meses > 12:
        meses -= 12
        anios += 1

d += dias
m += meses
a += anios

print(f'Estas en el {d}/{m}/{a}')



