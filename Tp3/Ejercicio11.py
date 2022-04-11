'''Cada cliente que va al banco Express, indica su número de documento y aguarda a ser atendido, 
cuando finaliza la atención del día se ingresa -1 para indicar que no hay más clientes para ser 
atendidos. El banco desea saber quién fue el primer cliente atendido y quién fue el último.'''

cliente = int(input('Ingrese su numero de documento: '))
primer_cliente = cliente

while cliente != -1:
    cliente_final = cliente
    cliente = int(input('Ingrese su numero de documento: '))


print(f'El primer cliente fue: {primer_cliente}')
print(f'El ultimo cliente fue: {cliente_final}')