'''Leer números que representan edades de un grupo de personas, finalizando la lectura cuando 
se ingrese el número 999. Imprimir cuántos son menores de 18 años, cuántos tienen 18 años o 
más y el promedio de edad de ambos grupos. Descartar valores que no representan una edad 
válida. (Se considera válido una edad entre 0 y 100).'''

edad = 1
flag = True
lista_menores = []
lista_mayores = []

while flag:
    edad = int(input('Ingrese una edad: '))
    if edad == 999:
        flag = False
    elif (edad > 0 and edad < 19):
        lista_menores.append(edad)
    elif (edad > 18 and edad < 101):
        lista_mayores.append(edad)
    else:
        print('La edad es invalida')
print(f'Los menores de edad son: {len(lista_menores)}\nEl promedio de edad es: {sum(lista_menores)/len(lista_menores)} ')
print(f'Los menores de edad son: {len(lista_mayores)}\nEl promedio de edad es: {sum(lista_mayores)/len(lista_mayores)} ')

