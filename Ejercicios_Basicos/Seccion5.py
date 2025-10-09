"""SECCIÓN 5: Subsetting y slices con []
•	Crea una variable palabra = 'Python' y muestra: la primera letra, las tres primeras letras, las dos últimas letras.
•	Crea una variable frase = 'Aprender Python es divertido' y muestra la palabra 'Python' usando slicing.
•	Pide al usuario una palabra y muestra cuántas letras tiene.
•	Pide al usuario una palabra y muestra su primera y última letra.
•	Crea una variable codigo = 'ABC1234XYZ' y muestra solo la parte numérica usando slice.
•	Crea una variable nombre = 'Juan Pérez' y muestra el apellido usando slice (es decir, utilizando [])."""

palabra = "Python"
print (palabra[0:1], palabra[0:3], palabra[:-3:-1])

frase = "Aprender Python es divertido"
print (frase[9:16])

palabra1 = input ("Ingresa una palabra: ")
print (F"Tu palabra tiene {len(palabra1)} letras")

palabra2 = input ("Ingresa otra palabra: ")
print (f"La primera letra es {palabra2[0:1:1]}, la ultima letra es {palabra2[-1:-2:-1]}")

codigo = "ABC1234XYZ"
print (codigo[3:6:1])

nombre = "Juan Pérez"
print (nombre[5:10:1])


