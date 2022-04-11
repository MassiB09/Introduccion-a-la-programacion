'''Escribir un algoritmo que permita ingresar los números de legajo de los alumnos de un curso 
y su nota de examen final. El fin de la carga se determina ingresando un -1 en el legajo. 
Informar para cada alumno si aprobó o no el examen considerando que se aprueba con nota 
mayor o igual a 4. Se debe validar que la nota ingresada sea entre 1 y 10. Terminada la carga 
de datos, informar:
• Cantidad de alumnos que aprobaron con nota mayor o igual a 4.
• Cantidad de alumnos que desaprobaron el examen. Nota menor a 4.
• Porcentaje de alumnos que están aplazados (tienen 1 en el examen).'''

legajo = 0
nota = 1
contador_desaprobados = 0
contador_aprobados = 0
aplazados = 0

while legajo != -1:
    if nota > 0 and nota < 11:
        legajo = int(input('Ingrese el legajo: '))
        nota = int(input('Ingrese la nota del examen final: '))
        if nota < 4:
            contador_desaprobados += 1
            if nota == 1:
                aplazados += 1
        else:
            contador_aprobados += 1
    else:
        print('La nota tiene que estar entre 1 y 10\n')
porcentaje_aplazados = (contador_aprobados + contador_desaprobados) * aplazados / 100

print(f'Los alumnos aprobados son: {contador_aprobados}')
print(f'Los alumnos desaprobados son: {contador_desaprobados}')
print(f'El porcentaje de aplazados es: {porcentaje_aplazados}')
