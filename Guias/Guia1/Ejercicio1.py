"""Te han asignado la misión de crear este nuevo programa. Tu programa debe recibir un correo a validar e imprimir un mensaje que indique si es válido o inválido (True/False). Para que un correo se considere válido, debe cumplir las siguientes condiciones:

El correo contiene exactamente un @
Antes y después del @ debe haber al menos 3 caracteres
El correo debe contener al menos un punto
El correo no puede contener espacios
El correo no puede iniciar ni terminar con un punto

Restricciones
Todos los correos tendrán mínimo un arroba, aunque pueden tener varios.

Entrada
Una sola línea con un correo electrónico a validar."""

correo = input()

longitud = len(correo)

# exactamente un @
res1 = correo.count("@") == 1

# posición segura del @ (no lanza excepción)
pos = correo.find("@")

# ≥ 3 antes y ≥ 3 después del @ (solo tiene sentido si hay exactamente un @)
res2 = res1 and (pos >= 3) and (longitud - pos - 1 >= 3)

# al menos un punto en todo el correo
res3 = ("." in correo)

# no espacios
res5 = (" " not in correo)

# no inicia ni termina con punto 
res4 = (correo[:1] != ".") and (correo[-1:] != ".")

# todas las condiciones verdaderas
good = res1 and res2 and res3 and res4 and res5

print(good)


