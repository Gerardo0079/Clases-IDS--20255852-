"""SECCIÓN 6: Operadores de string y métodos
•	Crea una variable frase = 'La programación es poderosa'. Muestra un mensaje si la palabra 'poderosa' está dentro de la frase. 
•	Usa el operador not in para verificar si 'Java' no aparece en la frase anterior.
•	Crea una variable palabra = 'hola' y muestra esa palabra repetida 5 veces usando *.
•	Crea una variable texto = 'banana' y muestra cuántas veces aparece la letra 'a'.
•	Crea una variable mensaje = 'El Salvador es un gran país' y muestra la posición donde aparece la palabra 'gran' usando .index().
"""

frase = "La programación es poderosa"
if "poderosa" in frase:
    print ("Poderosa esta en la frase")
else: 
    print ("Poderosa no esta en la frase")
    
if "Java" not in frase:
    print ("Java no esta en la frase")
else:
    print ("Java esta en la frase")

palabra = "Hola"
print (F"{palabra} "*5)

texto = "Banana"
print (texto.count("a"))

mensaje = "El Salvador es un gran país"
print (mensaje.index("gran"))


    

    


