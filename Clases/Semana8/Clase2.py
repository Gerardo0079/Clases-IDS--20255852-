ejecucion = True 

while ejecucion: 
    opcion = input ("Continuamos ejecutando el menu? Y/N: ")
    if opcion.lower( ) == "n":
       ejecucion = False
    elif opcion.lower() == "y":
        print ("Ok, continuemos.")
    else:
        print ("La opcion elegida no es valida. ")
print ("Gracias por usar nuestro programa")