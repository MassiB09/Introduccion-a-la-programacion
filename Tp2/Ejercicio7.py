'''Leer un número correspondiente a un año e imprimir un mensaje indicando si es bisiesto o no. 
Se recuerda que un año es bisiesto cuando es divisible por 4. Sin embargo, aquellos años que 
sean divisibles por 4 y también por 100 no son bisiestos, a menos que también sean divisibles 
por 400. Por ejemplo, 1900 no fue bisiesto, pero sí el 2000.'''

anio = int(input('Ingrese el año: '))

if anio % 4 == 0 and anio % 100 == 0 and anio % 400 == 0:
    print('Es año bisiesto!!')
elif anio % 4 == 0 and not(anio % 100 == 0):
    print('Es bisiesto!!')
else:
    print('No es bisiesto!!')