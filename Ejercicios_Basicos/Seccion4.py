"""SECCIÓN 4: f-strings y formato de salida
•	Crea tres variables (nombre, producto, precio) y muestra el mensaje: Hola Ana, el producto Laptop cuesta $1200.00 usando una f-string.
•	Pide el nombre y el país de un usuario y muestra: Hola, Carlos de El Salvador, ¡bienvenido!.
•	Crea un mini formulario que pida nombre, edad y ciudad, y luego muestre un resumen de la información en varias líneas usando f-strings.
•	Muestra el área de un rectángulo con base y altura dadas por el usuario. El resultado debe aparecer con dos decimales.
•	Muestra una tabla como esta: Producto: Pan, Precio: $1.50, Cantidad: 4, Total: $6.00 (Usa variables y f-strings).
"""
nombre, producto, precio = "Ana", "Laptop", 120
print (F"Hola, {nombre}, el producto {producto} cuesta {precio}")

usuario = input ("Ingresa tu nombre: ")
pais = input ("Ingresa el pais donde vives:")
print (f"Hola, {usuario} de {pais}, ¡bienvenido!")

nombre2, edad, ciudad = input ("Cual es tu nombre? "), input ("Cual es tu edad: "), input ("Cual es tu ciudad: ")
print (F"Hola {nombre2}, tienes {edad} años de edad y vives en {ciudad}")

base = float (input ("Ingresa la base del rectangulo: "))
altura = float (input ("Ingresa la altura del rectangulo: "))
print (F"El area del rectangulo es de: {(base*altura):.2f}")

Producto, precio, cantidad, total = "Pan" ,1.50,  4, 6.00 
print(F"El producto es: {Producto}, el precio es {precio}, la cantidad es: {cantidad } y el total es: {total:.2}")




