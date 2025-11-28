#Modulo para describir la logica de las funciones 

#Importamos el modulo de datos
import modulo_datos as dat 

def registrar_estudiantes (): 
    """Funcion para validar y registrar estudiantes"""
    while True: 
        carnet_i = input ("Digite el numero de carnet: ")
        n_c = len(carnet_i)
        valido = True
        for a in dat.alumnos: 
            if a["carnet"] == carnet_i:
                valido = False
        if n_c >= 6 and n_c <= 10 and valido: 
            break 
        else: 
            print ("El numero de digitos debe de ser entre 6 y 10, y unico")
    while True:        
        nombre_i = input ("Digite el nombre: ")
        if len(nombre_i) >=2: 
            break
        else: 
             print ("El numero de caracteres deben de ser mas de 2")
    while True: 
        apellido_i = input ("Digite el apellido: ")
        if len (apellido_i) >= 2: 
            break
        else: 
             print ("El numero de caracteres deben de ser mas de 2")
             
    alumno = {"carnet":carnet_i, "nombre": nombre_i, "apellido": apellido_i}
    dat.alumnos.append(alumno)
    
def inscribir_en_curso():
    """Inscribir un estudiante en un curso"""
    while True:
        carnet_i = input ("Digite el carnet a inscribir (Puede escribir  \"salir\"):")
        if carnet_i.lower () == "salir":
            break
        existe = False
        for alumnito in dat.alumnos:
            if alumnito["carnet"] == carnet_i:
                existe = True
        if existe == True: 
            print ("El carnet existe")
            for cod, nombre in dat.cursos.items():
                print (f"{cod} - {nombre}")
            
            while True: 
                curso_i = input ("Puede elegir el codigo de inscripcion:")
                curso_existe = False
                for curso in dat.cursos.keys():
                    if curso == curso_i:
                        curso_existe = True 
                        break
                if curso_existe:
                    print("El curso existe.")
                    
           
            break 
        else: 
            print ("El carnet no exste")
            
        
        
    

    
    