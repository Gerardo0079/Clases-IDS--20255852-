"""SECCIÓN 3: Operadores matemáticos y lógicos
•	Crea tres variables: a = 10, b = 3, c = 5. Calcula y muestra: la suma de a y b, el resultado de a dividido entre b, el residuo de dividir a entre c.
•	Crea una variable numero con valor 7 y muestra True si es mayor que 5, False en caso contrario.
•	Crea dos variables x = 10, y = 10. Usa los operadores is e is not para verificar si apuntan al mismo objeto en memoria.
•	Pide un número al usuario y muestra True si es par, False si es impar (usa el operador %).
•	Crea una variable booleana registrado = True. Usa operadores lógicos (and, or, not) para mostrar combinaciones posibles.
•	Pide al usuario dos números y muestra si el primero es mayor o igual que el segundo.
•	Pide al usuario su edad y muestra si tiene edad suficiente para votar (mayor o igual que 18).
•	Crea un ejemplo que combine operadores relacionales y lógicos, como: edad = 22; estudiante = True; print(edad >= 18 and estudiante).
"""
a, b, c = 10, 3, 5

print (F"La suma de los tres números es: {a+b+c}, a entre b es: {a/b} y el residuo de a entre c es: {a%c}")

num = 7 
com_num = 7 > 5
print ("Siete es mayor que 5? ", com_num)

x, y = 10, -10 
print(f"x es y? {x is y}")
print(f"x no es y? {x is not y}")

num_input = int (input ("Ingrese un numero entero: "))
print (num_input%2 is 0)

booleano = True 






