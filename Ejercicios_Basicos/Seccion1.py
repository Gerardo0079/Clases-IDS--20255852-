"""SECCIÓN 1: Variables, comentarios y print()
•	Crea una variable llamada nombre y asígnale tu propio nombre. Muestra su valor usando print().
•	Crea tres variables: edad, ciudad y profesion, asígnales valores y muestra un mensaje combinándolos en una sola línea. 
•	Escribe un comentario que explique para qué sirve una variable en un programa.
•	Crea una variable mensaje que contenga el texto 'Bienvenido al curso de Python' y muéstralo.
•	Crea una variable anio_actual con el valor 2025 y una variable anio_nacimiento. Calcula y muestra tu edad restando ambos valores.
•	Declara una variable llamada pi con el valor 3.14159265359. Muestra un mensaje que diga “El valor aproximado de pi es 3.1416”.
•	Explica mediante un comentario qué diferencia hay entre una variable de tipo entero y una de tipo cadena.
"""

Nombre = "Gerardo"
print(Nombre)
edad = 18
ciudad = "Zaragoza"
profesion = "Estudiante"
print (f"Mi nombre es {Nombre}, tengo {edad} y soy un {profesion}")
#Una variable es como una caja que permite contener datos (pueden ser diversos)
Mensaje = "Bienvenido al curso de Python"
anio_actual = 2025 
anio_nacimiento = 2007
print(F"Naci en el año {anio_nacimiento} y hoy es el año {anio_actual}, por ende tengo {anio_actual - anio_nacimiento} años")
pi = 3.14159265359
print (f"El valor aproximado de pi es: {pi:.4}")
#La diferencia entre estos tipos de valores es que entero son solo numeros y cadena es para textos