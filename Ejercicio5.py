#Una persona quiere invertir su capital en un banco y quiere saber cuánto dinero gana en un mes si el banco paga 2% mensual.
#¿Cuánto ganará en seis meses si deja su dinero invertido?
capital = int(input('Ingrese su capital: '))
meses = int(input('Ingrese la cantidad de meses que quiere invertir su dinero: '))
for i in range(meses):
    ganancia = capital * 2 / 100
    capital = capital + ganancia
print(f'Su ganancia en {meses} meses es: {round(capital,2)}')