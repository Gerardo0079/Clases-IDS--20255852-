nombre = input ()
apellido = input()

part1 = nombre [:5] + apellido[0]
pin = (len(nombre) *1000 + len (apellido))% 10000

id = "C3-" + part1.lower() + "-" + str (pin)

print (f"Nick: {part1.lower()}")
print (f"Pin: {pin}")
print (f"ID: {id}")