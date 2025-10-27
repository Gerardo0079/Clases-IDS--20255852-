combos  = int (input ())
Pa, Pb, Pc = int(input ( )), int(input ( )), int(input ( ))
i = 0 
tipos = []
tipos_damage = []
while i != combos: 
    tipos.append(input ())
    tipos_damage[i] =  (tipos[i].count("A") * Pa) + (tipos.count[i]("B") * Pb) + (tipos.count[i]("C") * Pc)
    i = i +1
print (tipos_damage)
    
