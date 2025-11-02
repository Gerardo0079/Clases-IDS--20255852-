cantidad = int (input ())

Redistribuciones = []
for i in range (cantidad):
    SL = int (input ())
    if SL >= 3:
       Redistribuciones.append ("Ok")
    else: 
       Redistribuciones.append ("No")
print (*Redistribuciones, sep = "\n")
