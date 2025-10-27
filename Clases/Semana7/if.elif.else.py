monto  = float (input ("Digite el monto: "))
tipo = input ("Tipo (local/internacional): ")
descuento = 0

if tipo.lower () == "local":
    if monto > 100: 
        impuesto = 0.07
    else: 
        if monto > 75: 
            impuesto = 0.05
        else: 
            impuesto = 0

elif tipo.lower()  == "internacional":
    if monto > 100: 
        impuesto = 0.12
    elif monto > 75: 
        impuesto = 0.09
    else: 
        impuesto = 0
        
else: 
    print ("Ese tipo no existe")
    
print (f"El tipo {tipo} con monto {monto:,.2f}")
print (f" paga un impuesto de {monto*impuesto:,.2f}")
    
    
    
"""
if tipo == "local":
    if monto >100:
        descuento = 0.07
    else:
        if monto > 75: 
            descuento = 0.05
        else: 
            descuento = 0
else: 
    if monto > 100: 
        descuento = 0.12
    else: 
        if monto > 75: 
            descuento = 0.9
        else: 
            descuento = 0
print (descuento)
    """