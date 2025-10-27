"""Entrada
Recibirás 6 datos de tipo float, cada uno en una línea independiente.

Estos representan las notas de los estudiantes ya calificadas. Puedes usar una lista para almacenarlas.

Salida
Debes calcular y mostrar en líneas separadas lo siguiente, con formato de 2 decimales en todos los valores numéricos:

El máximo
El mínimo
La diferencia entre el máximo y el mínimo
La suma total de las 6 notas
El promedio de las 6 notas
Cada línea debe seguir estrictamente el formato indicado:

La palabra del campo (escríbela exactamente igual), seguida de dos puntos, un espacio y el número con dos decimales. Presta mucha atención a las mayúsculas, los acentos y los espacios, ya que cualquier diferencia hará que tu programa no produzca la salida correcta.

Nota: El orden de las líneas es obligatorio y el formato de dos decimales debe aplicarse incluso a los números enteros para mantener la coherencia."""

d1, d2, d3, d4, d5, d6 = float (input()), float (input()),float (input()),float (input()),float (input()),float (input())
notas = [d1, d2, d3, d4, d5, d6]
mx = max(notas)
mn = min(notas)
dif = mx - mn
total = sum(notas)
prom = total / 6

print(f"Maximo: {mx:.2f}")
print(f"Minimo: {mn:.2f}")
print(f"Diferencia: {dif:.2f}")
print(f"Suma: {total:.2f}")
print(f"Promedio: {prom:.2f}")
