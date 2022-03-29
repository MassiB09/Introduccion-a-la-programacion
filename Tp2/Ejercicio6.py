'''Una remisería requiere un sistema que calcule el precio de un viaje a partir de la cantidad de 
km que desea recorrer el usuario. Tiene la siguiente tarifa: 
▪ Viaje mínimo $50
▪ Si recorre entre 0 y 10km: $20/km
▪ Si recorre 10km o más: $15/km'''

km = float(input('Ingrese la cantidad de kilometros: '))
minimo = 50
minimo_10km = 250

if km < 10:
    costo_viaje = minimo + 20 * km
else:
    costo_viaje = minimo_10km + 15 * (km -10)

print(f'El costo del viaje es: {costo_viaje}')