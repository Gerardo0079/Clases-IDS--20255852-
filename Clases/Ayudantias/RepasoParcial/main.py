#Este modulo sera el inicio del program 

#importamos las funcioens de modulo_funciones.py 
import modulo_funciones as fn


while True: 
    print("---- Menu principal -----")
    print ("\t1. Registrar estudiantes \n\t2. Inscribir en curso\n\t3.Generar reportes\n\t4.salir")
    opcion = input ("Indique su opcion [1 - 4]: ")

    if opcion ==  "1":
        fn.registrar_estudiantes ()
    elif opcion == "2": 
        fn.inscribir_en_curso()
    elif opcion == "3": 
        print ("Eligio la opcion 3")
    elif opcion == "4":
        print ("Gracias por utilizar nuestro sistema")
        break
    else:
        print ("La opcion elegida no es valida")
        
