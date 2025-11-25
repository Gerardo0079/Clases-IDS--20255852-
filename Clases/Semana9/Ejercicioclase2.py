def dui_validaciones(dui):
    condiciones = 0
    if len(dui) == 10:
        condiciones += 1
    if dui.count("-") == 1:
        condiciones += 1
    if dui[-1] != "-" and dui[-2] == "-":
       condiciones += 1
    print (f"Cumple {condiciones} condiciones")
    
dui_validaciones (
    input ("Ingrese el dui: ")
)