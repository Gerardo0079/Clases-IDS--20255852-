surnames = ["Rivest", "Shamir", "Adleman"]
for position, surname in enumerate(surnames, start = 1):  #La parte izquierda (Variable) es el iterador y el lado izquierdo el item. Se separa por coma, pueden ser distintos items
    print (position, surname)                #El start empieza en la posición 0, puede variar. Es para indicar desde donde empieza el contador, no afecta o es igual a un index
   
people = ["Nicol", "Rick ", "Rogelio", "Syd"]
ages = [23, 24, 23, 21]
instruments = ["Drums", "Keyboard", "Bass", "Guitar"]
                              #Se usa zip para juntar diversas listas o tuplas, en este caso que tienen relación
for person, age, instrument in zip (people,ages, instruments): #Se crean nuevas variables para iterar, pueden ser caulquiera 
    print (person, age, instrument)
    