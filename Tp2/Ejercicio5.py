''' Una editorial determina el precio de un libro según la cantidad de páginas que contiene. El 
costo básico del libro es de $500, más $20,20 por página con encuadernación rústica. Si el 
número de páginas supera las 300 la encuadernación debe ser en tela, lo que incrementa el 
costo en $200. Además, si el número de páginas sobrepasa las 600 se hace necesario un 
procedimiento especial de encuadernación que incrementa el costo en $336. Desarrollar un 
programa que calcule el costo de un libro dado el número de páginas.'''

numero_paginas = int(input('Ingrese el numero de paginas del libro: '))
costo_base = 500
costo_encuadernacion = 20.20
costo_encuadernacion_tela = 200
costo_encuadernacion_especial = 336

if numero_paginas <= 300:
    costo_libro = costo_base + numero_paginas * costo_encuadernacion
elif numero_paginas > 300:
    costo_libro = costo_base + numero_paginas * costo_encuadernacion + costo_encuadernacion_tela
else:
    costo_libro = costo_libro = costo_base + numero_paginas * costo_encuadernacion + costo_encuadernacion_tela + costo_encuadernacion_especial

print(f'El valor del libro es: {costo_libro}')