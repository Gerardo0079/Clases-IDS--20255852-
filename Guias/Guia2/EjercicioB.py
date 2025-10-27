"""Descripción
Leer un numero entero S y mostrar como salida el numero par posterior y el número impar anterior.

Entrada
Un número entero S.

Salida
El número par posterior y el número impar anterior al número entero leído.

Ejemplo"""

n1 = int (input())

n1_par = n1 +1 
n1_impar = n1-1

while n1_par % 2 != 0: 
    n1_par = n1_par + 1 
    
while n1_impar % 2 == 0: 
    n1_impar = n1_impar -1
    
print (n1_par)
print (n1_impar)
