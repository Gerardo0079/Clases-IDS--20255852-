alumnos  = 0
lista_alumnos  = [ ]
cantidad = int (input ("Cuantos alumnos vamos a ingresar? "))

for i in range (cantidad):
    alumnos = input ("Ingrese el nombre del alumno: ")
    lista_alumnos.append (alumnos)
print (lista_alumnos)