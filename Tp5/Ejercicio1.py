def multiplicar(numero1,numero2):
    resultado = 0
    for i in range(numero2):
        resultado += numero1
    return resultado

n = int(input('Ingrese un numero: '))

numero = 1
for i in range(n):
    numero = multiplicar(numero, (i+1))
    print(f'Numero: {numero}')