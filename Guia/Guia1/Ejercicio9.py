plato = int (input ())
complemento = int (input())

platos_principales = ["Hamburguesa", " Pizza", "Tacos", " Pupusas" , "Hotdog"]
complementos_disponibles = ["Papas fritas", "Alitas de pollo", "Ensalada", "Sopa", "Lasaña"]

print (f"El pedido de Alvin es: {platos_principales[plato-1]} con {complementos_disponibles[complemento-1]} ")