"""SECCIÓN 2: input() y conversión de tipos (casting)
•	Pide al usuario su nombre usando input() y muéstrale un saludo personalizado.
•	Pide al usuario su edad y muestra un mensaje con el doble de esa edad. 
•	Pide dos números enteros al usuario, súmalos y muestra el resultado.
•	Pide al usuario un número decimal y muestra su mitad.
•	Pide al usuario su año de nacimiento y calcula su edad (usando 2025 como año actual).
•	Pide al usuario el precio de un producto y el número de unidades. Muestra el total a pagar.
•	Pide al usuario un número entero y muestra el cuadrado de ese número.
•	Pide al usuario dos números y muestra su promedio.
•	Pide al usuario su nombre completo y su edad, y muestra un mensaje con formato f-string como: Hola, Juan Pérez. Tienes 20 años.
"""

Nombre = input ("Ingrese su nombre: ")
print (F"Bienvenido {Nombre}, un saludo ")

Edad = int (input ("Ingrese su edad: "))
print(F"El doble de su edad es: {Edad*2}")

Num1 = int (input ("Ingrese el primer numero: "))
Num2 = int (input ("Ingrese el segundo numero: "))
print (F"La suma de {Num1} y {Num2} es: {Num2 + Num1}")

num_decimal = float (input ("Ingrese un numero decimal: "))
print (F"La mitad de ese numero es: {num_decimal/2}")

anio_nacimiento = int(input ("Ingrese su año de nacimiento: "))
anio_actual = 2025
print (F"Su edad es de: {anio_actual - anio_nacimiento}")

precio_producto = float (input ("Ingrese el precio del producto: "))
cantidad_producto = int (input ("Ingrese la cantidad que va a llevar: "))
print (F" El precio es de {precio_producto}, lleva {cantidad_producto}, hace un total de ${precio_producto*cantidad_producto}")

num_cuadrado = float (input ("Ingrese un numero: "))
print(F"El cuadrado de {num_cuadrado} es de: {num_cuadrado*num_cuadrado}")

num_promedio1 = float (input ("ingresa el primer numero: "))
num_promedio2 = float (input ("ingresa el segundo numero: "))
print(F"El promedio entre {num_promedio1} y {num_promedio2} es de: {(num_promedio1+num_promedio2)/2}")

print (F"Hola {Nombre}. Tienes {Edad}")




