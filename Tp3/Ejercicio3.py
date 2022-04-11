'''Mostrar las tablas de multiplicar (entre 1 y 10) del número 4. ¿Cómo cambiaría el algoritmo 
para que el usuario pueda decidir la tabla de multiplicar a mostrar?'''

tabla = int(input('Ingrese el numero de la tabla que desa conocer: '))

for i in range(10):
    print(f'Numero {i+1}: {tabla * (i+1)}')