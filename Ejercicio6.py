# Leer una medida en metros e imprimir esta medida expresada en centímetros, pulgadas, pies y yardas. \
# Los factores de conversión son:
#1 pie = 12 pulgadas
#1 yarda = 3 pies
#1 pulgada = 2,54 cm.
#1 metro = 100 cm.
metros = float(input('Ingrese una medida en metros: '))
centimetros = metros * 100
pulgadas = centimetros / 2.54
pies = pulgadas / 12
yardas = pies / 3
print(f'Medida en centimetros: {centimetros}')
print(f'Medida en pulgadas: {pulgadas}')
print(f'Medida en pies: {pies}')
print(f'Medida en yardas: {yardas}')