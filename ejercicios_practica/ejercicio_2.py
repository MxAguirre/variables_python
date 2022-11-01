# Tipos de variables [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 3.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios de práctica numérica y consola

# Ahora los valores a operar deben ser ingresados por
# consola con la función "input" como se ve a continuación
from __future__ import division


numero_1 = int(input('Ingrese por consola el primer número entero a operar:'))

numero_2 = int(input('Ingrese por consola el segundo número entero a operar:'))

# Alumno: Imprima en pantalla los dos números enteros solicitados
# print(....)

print(numero_1)
print(numero_2)

# Objetivo:
# Calcular la suma, resta, división y multiplicación
# de los números ingresados numero_1, numero_2

# Alumno:
# Crear una variable llamada suma donde se 
# almacene el valor de la suma de las variable numero_1 y numero_2

suma = numero_1 + numero_2

# Crear una variable llamada resta donde se 
# almacene el valor de la resta de numero_1 menos numero_2
resta = numero_1 - numero_2
# Crear una variable llamada division donde se 
# almacene el valor de la division de numero_1 dividido numero_2
if numero_2 == 0 : 
    pass
else : 
    division = numero_1 / numero_2

# Crear una variable llamada multiplicacion donde se 
# almacene el valor de la multiplicacion de numero_1 por numero_2

multiplicacion = numero_1 * numero_2

# Imprima en pantalla todos los resultados
print('La suma de estos numeros es:', suma)
print('La resta de estos numeros es:', resta)
if numero_2 == 0 : print('No se puede dividir por cero')
else : print('La division de estos dos numeros es:', division)
print('La multiplicacion de estos numeros es:', multiplicacion)