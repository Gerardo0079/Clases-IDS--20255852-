Valores  = [[1, 3, 6], [2, 7, 4], [6 ,5 ,9], [1, 10, 20 ]]
numero = int (input ())
suma = 0
condicion = True
i = 0 


while condicion == True and i < len(Valores): 
    j = 0
    while condicion == True and j < len (Valores [i]): 
        suma += Valores[i][j]
        if suma > numero:
            condicion = False
            suma = suma - Valores [i][j]
        j += 1
    i += 1
print (suma)

    