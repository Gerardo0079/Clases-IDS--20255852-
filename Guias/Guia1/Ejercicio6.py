"""Entrada
Vas a recibir 10 numeros en total.

Los primeros 5 numeros enteros determinan la cantidad de puntos que otorga cada problema.

Los ultimos 5 numeros decimales detereminan el porcentaje que obtuvo cada equipo.

Salida
Un solo numero entero que indique la puntuacion total del equipo NESE."""

n1, n2, n3, n4, n5= int (input()), int (input()),int (input()),int (input()),int (input())
n6, n7, n8, n9, n10 = float (input ()), float (input ()), float (input ()), float (input ()), float (input ())

print (int (n1 * n6 + n2 * n7 + n3 *n8 + n4 * n9 + n5 * n10))