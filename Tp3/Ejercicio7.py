'''Un negocio desea saber el importe total recaudado al fin del día, desea contar con un programa 
que pueda ingresar el importe de cada venta realizada. Para indicar que finalizó el día se ingresa 
-1. ¿Cuál fue el monto total vendido y cuántas ventas se realizaron? El importe de cada venta 
realizada debe ser un valor positivo.'''

numero = int(input('Ingrese el valor de la venta: '))
contador = 0
suma = 0

while numero != -1:
    if  numero > 0:
        contador += 1
        suma += numero
    else:
        print('El valor tiene que ser positivo')
    numero = int(input('Ingrese el valor de la venta: '))

print(f'La ganancia total de este dia es: {suma}')
print(f'Las ventas de hoy fueron: {contador}')