''' Diseñar una función para mostrar un título filas de asteriscos, la longitud de la fila de asteriscos 
y el texto del título se recibe como parámetro. Ejemplo: titulo(“Ejercicio 3”, 15) muestra:
***************
Ejercicio 3
***************
Desarrollar un programa principal para mostrar el título: “Aprendiendo Funciones”, del ejercicio 
4 al 8 agregar un título al iniciar el programa relacionado a lo que va a resolver el problema.'''

def titulo_asteriscos(titulo, cantidad_asteriscos):
    asteriscos = ''
    for i in range(cantidad_asteriscos):
        asteriscos += '*'
    mensaje = f'{asteriscos}\n{titulo}\n{asteriscos}'
    return mensaje

titulo = titulo_asteriscos('Aprendiendo Funciones', 25)
print(titulo)