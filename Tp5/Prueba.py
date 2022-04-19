sumDigit, extNum = 0, 0
numEntero = int(input("Ingrese un numero entero: "))
while numEntero != 0:
    extNum = numEntero % 10
    numEntero //= 10
    sumDigit += extNum
print("La suma de los digitos es: {}".format(sumDigit))