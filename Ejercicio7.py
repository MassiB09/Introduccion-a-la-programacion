# Una inmobiliaria paga a sus vendedores un salario base, más una comisión fija por cada venta realizada,
#  más el 5% del valor de esas ventas.
#  Realizar un programa que imprima el número del vendedor y el salario que le corresponde en un determinado mes.
#  Se leen por teclado el número del vendedor, la cantidad de ventas que realizó y el valor total de las mismas.
numero_vendedor = int(input('Ingrese su numero de vendedor: '))
ventas_realizadas = int(input('Ingrese la cantidad de ventas realizadas: '))
valor_total = int(input('Ingrese el valor total: '))
salario_base = 100
comision_fija = 2
salario = salario_base + comision_fija * ventas_realizadas + valor_total * 5 / 100
print(f'Nro vendedor: {numero_vendedor}\nSalario: {salario}')