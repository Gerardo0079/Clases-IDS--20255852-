#Cuando una función depende un objeto es un métdodo 

"""    | --- Argumentos 
 print( )
       | --- Pueden ser: Ninguno, Uno o Muchos
"""
#Una función se crea con def, el input o output es opcional 
""" def my_function (input): 
    ... 
    ...
    return output
"""
#El archivo por completo de py es un modulo, se pueden tener distintos modulos para un proyecto
def saludar():
    #Se puede crear un docstring dentro de una función para dar el contexto de la función
    """  Es una función que va a saludar """ 
    nombre = input ("Digite el nombre:")
    apellido = input("Digite el apellido ")
    nombre_completo = f"{nombre.title() } {apellido.title()}"
    print(f"Hola {nombre_completo}")


def saludar_con_parametros():
    """Es una función que va a saludar con un parametro"""
    nombre = input ("Digite el nombre:")
    apellido = input("Digite el apellido ")
    nombre_completo = f"{nombre.title() } {apellido.title()}"
    print(f"Hola {nombre_completo}")
    
#Las funciones se describen con minúsculas y las clases con mayúsculas 

def describir_mascota (animal, nombre_mascota):
    """Vamos a describir mascotas. """
    print (f"Tengo un {animal}, y su nombre es {nombre_mascota.title() }")
 
describir_mascota(nombre_mascota = "firulais", animal = "perro" )
describir_mascota ("gato", "mishito")
describir_mascota (
    input("Digite el tipo de animal: "),
    input ("Digite el nombre de la mascota")
)


        
    
