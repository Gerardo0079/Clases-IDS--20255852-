clientes = []
productos = []
pedido = []
j = 0
print ("Bienvenido al menu de la cafeteria ESEN")

menu_activo = True 
while menu_activo:
    
    print ("\nMenu principal: ")
    print ("\n 1. Mostrar productos \n 2.	Agregar producto \n 3.	Registrar nuevo cliente \n 4.	Mostrar clientes \n 5.	Registrar pedido \n 6.	Mostrar pedidos del día \n 7.	Mostrar categorías disponibles \n 8.	Salir")
    opcion = int (input ("Este es nuestro menu, selecciona un numero (1-8): "))
    
    if opcion == 1:
        if len(productos) != 0:
          print (productos)
        else:
            print ("Aun no hay productos registrados")
    
    elif opcion == 2:
     
        j += 1
        nombre_nuevo = input ("Ingrese el nombre del producto: ")
        categoria_nuevo = input ("Ingrese el categoria del producto; ")
        precio_nuevo = float (input ("Ingrese el precio del producto: "))
        usuario_id = "P" + str (j)
        producto = [{"nombre": nombre_nuevo, "categoria": categoria_nuevo, "precio": precio_nuevo}]
        productos.append(producto) 
        
    elif opcion == 3:
        n = 0
        n += 1
        nombre_nuevo = input ("Ingrese el nombre del cliente: ")
        correo_nuevo = input ("Ingrese el correo del cliente; ")
        telefono_nuevo = input ("Ingrese el telefono del cliente: ")
        usuario_id = "C" + str (n)
        cliente = [{"nombre": nombre_nuevo, "correo": correo_nuevo, "telefono": telefono_nuevo}]
        clientes.append(cliente) 
        
    elif opcion == 4:
        if len(clientes) != 0:
          print (clientes)
        else:
            print ("Aun no hay clientes registrados")
    
    elif opcion == 5:
        if len(productos) != 0:
          a = 0
          for a in productos:
              print(productos[a]["nombre"], + " $"+ productos[a]["precio"] )
              a += 1
        else:
            print ("Aun no hay productos registrados")
    

        