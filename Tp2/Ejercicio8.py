'''Diseñar un programa que calcule y muestre el sueldo neto de un empleado en base a su sueldo 
básico y su antigüedad en años. Si es soltero se le incrementa el sueldo en 5% del salario bruto 
por cada año de antigüedad, mientras que si es casado se le incrementa el sueldo en 7% del 
bruto por cada año de antigüedad. También se le realizan los siguientes descuentos: Jubilación: 
11%, Obra Social: 3%, Sindicato: 3%.
Como datos de entrada se ingresa por teclado el sueldo básico, antigüedad y estado civil (‘s’ o 
‘c’). Se debe informar: (reemplazar los 9 por los valores que correspondan'''

sueldo_basico = int(input('Ingrese su sueldo basico: '))
antiguedad = int(input('Ingrese sus años de antiguedad: '))
estado_civil = input('Ingrese su estado civil("S" o "C"): ')
soltero = sueldo_basico * 0.05
casado = sueldo_basico * 0.07
jubilacion = sueldo_basico * 0.11
obra_social = sueldo_basico * 0.03
sindicato = obra_social
sueldo_final = sueldo_basico - jubilacion - obra_social - sindicato

if estado_civil.upper() == 'S':
    sueldo_final = sueldo_final + soltero 
    estado_civil = 'SOLTERO'
else:
    sueldo_final = sueldo_final + casado
    estado_civil = 'CASADO'

print(f'\nDatos\nSueldo basico: {sueldo_basico}\nAntiguedad: {antiguedad}\nEstado civil: {estado_civil}')
print(f'Su sueldo neto es: {sueldo_final}')