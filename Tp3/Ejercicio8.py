'''Se desea analizar cuántos autos circulan con patente que tiene numeración par y cuántos con 
numeración impar en un día. Le solicitan escribir un algoritmo que permita ingresar la 
terminación de la patente (entre 0 y 9) hasta ingresar -1 e informar cuántas se ingresaron con
numeración par y cuántas con numeración impar.'''

patente = 0
contador_par = 0
contador_impar = 0

while patente != -1:
    patente = int(input('Ingrese la terminacion de la patente (entre 0 y 9): '))
    if patente > 9 or patente < 0:
        print('Error, se ingreso mas de un digito')
    else:
        if patente % 2 == 0:
            print('La patente es par')
            contador_par += 1
        else: 
            print('La patente es impar')
            contador_impar += 1

print(f'Patentes pares: {contador_par}')
print(f'Patentes impares: {contador_impar}')