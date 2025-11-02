alumnos = 0
lista_alumnos= []

print("Bienvenido a nuestro sistema de control de alumnos")
menu_activo= True



while menu_activo:
    opcion= input("Elija la opción (1: Ingresar alumnos, 2: Consultar, 3: Modificar, 5: Salir):")
    if opcion ==  "5":
        menu_activo= False
    elif opcion == "1":
        alumnos = input("Nombre de alumno a agregar: ")
        lista_alumnos.append(alumnos)
    elif opcion == "2":
        print(lista_alumnos)
    elif opcion == "3":
        i= int(input("Ingrese la posición del alumno a modificar (1-4): "))
        n = input("Ingrese el nuevo nombre del alumno: ")
        lista_alumnos[i-1] = n
    elif opcion == "4":
        borrado= lista_alumnos.pop(int(input("Ingrese el número del alumno a popear (1-4):")-1)) #Pierdo la info de haber borrado el icono si no lo pongo en variable
        print(f"Usted a popeado a {borrado}.")
        
    else: 
        print ("La opcion elegida no es valida ")



print("Gracias por utilizar nuestro sistema")