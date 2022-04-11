'''Una empresa aplica el siguiente procedimiento en la comercialización de sus productos:
• Aplica el precio base a la primera docena de unidades.
• Aplica un 10% de descuento a todas las unidades entre 13 y 100.
• Aplica un 25% de descuento a todas las unidades por encima de las 100.
Por ejemplo, supongamos que vende 230 unidades de un producto cuyo precio base es 100. El 
cálculo resultante sería:
100 * 12 + 90 * 88 + 75 * 130 = 18870, y el precio promedio será 18870 / 230 = 82,04
Escribir un algoritmo que lea la cantidad solicitada de un producto y su precio base, y muestre 
el valor total de la venta y el precio promedio por unidad. El fin de carga se determina 
ingresando -1 como cantidad solicitada. 
Al finalizar informar:
a) Cantidad de ventas realizadas total.
b) Cantidad de ventas que se aplicaron un 10% de descuento.
c) Cantidad de ventas que SOLO se aplicó el precio base, no se le realizaron 
descuentos.'''

unidades = 0
precio = 0
precio_final = 0
descuento_10 = 0
contador_ventas = 0
contador_ventas_10 = 0
contador_ventas_10_totales = 0
contador_ventas_sin_descuento = 0
contador_ventas_sin_descuento_totales = 0

while True:
    unidades = int(input('Ingrese las unidades que lleva: '))
    precio = int(input('Ingrese el precio por unidad: '))
    if unidades < 1 or precio < 1:
        if unidades == -1 or precio == -1:
            break
        else:
            print('No podes ingresar numeros negativos!!\n')
    else:
        contador_ventas += unidades
        if unidades <= 12:
            precio_final = unidades * precio
            contador_ventas_sin_descuento = unidades
        elif unidades <= 100:
            descuento_10 = precio * 10 / 100
            unidades -= 12
            contador_ventas_sin_descuento = 12
            precio_final = 12 * precio + unidades * (precio - descuento_10)
            contador_ventas_10 = unidades
        else:
            descuento_10 = precio * 10 / 100
            descuento_25 = precio * 25 / 100
            unidades -= 100
            contador_ventas_sin_descuento = 12
            precio_final = 12 * precio + 88 * (precio - descuento_10) + unidades * (precio - descuento_25)
            contador_ventas_10 = 88 
    contador_ventas_sin_descuento_totales += contador_ventas_sin_descuento
    contador_ventas_10_totales += contador_ventas_10
    print(f'El valor de la venta es: {precio_final}\n')

print(f'Las ventas totales fueron: {contador_ventas}')
print(f'Las ventas con 10% de descuento fueron: {contador_ventas_10_totales}')
print(f'Las ventas sin descuento fueron: {contador_ventas_sin_descuento_totales}')