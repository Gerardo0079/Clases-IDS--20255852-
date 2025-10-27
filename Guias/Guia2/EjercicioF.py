n1 = int (input ())
nombres =[]
longitud = []
i = 0 

while i != n1:
    nombres.append (input())
    longitud.append (len(nombres[i]))
    i = i + 1
i = 0
while i != n1:
    if longitud [i] <= 6:
        print ("Dios no creo aguantar esta vez")
    elif 6 >=longitud[i] < 8:
        print ("Dios no creo aguantar esta vez")
    else: 
        print("Si aguanto otro desarrollo de personaje")
    i = i + 1
        
        

