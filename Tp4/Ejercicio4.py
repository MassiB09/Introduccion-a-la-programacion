'''Una empresa factura a sus clientes el último día de cada mes. Si el cliente paga su factura 
dentro de los primeros 10 días del mes siguiente, tiene un descuento de $120 o del 2% de la 
factura, lo que resulte más conveniente para el cliente. Si paga en los siguientes 10 días del 
mes deberá pagar el importe original de la factura, mientras que si paga después del día 20 
deberá abonar una multa de $150 o del 10% de su factura, lo que resulte mayor. Escriba un 
algoritmo que lea el número del cliente y el total de la factura, y emita un informe donde conste 
el número del cliente y los tres importes que podrá abonar según la fecha de pago'''

importe1 = 0
importe2 = 0
importe3 = 0
descuento_2 = 0
multa = 0

numero_cliente = int(input('Ingrese el numero de cliente: '))
factura = float(input('Ingrese el total de su factura: '))

descuento_2 = factura * 2 / 100
if descuento_2 > 120:
    importe1 = factura - descuento_2
else:
    importe1 = factura - 120

importe2 = factura

multa = factura * 15 / 100
if multa > 150:
    importe3 = factura + multa
else:
    importe3 = factura + 150

print(f'Cliente: {numero_cliente}')
print(f'El importe de la factura en los primeros 10 dias es: {importe1}')
print(f'El importe de la factura entre el 10 y el 20 es: {importe2}')
print(f'El importe de su factura mas la multa es: {importe3}')