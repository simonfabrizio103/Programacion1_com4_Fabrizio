import trabajo_practico_8_funciones as arch
while True:
    print(f"""---Gestionar Productos---
            1. Mostrar productos
            2. Agregar productos
            3. Buscar productos
            4. Salir
            """)
    opcion = input("ingresa la opción: ")

    match opcion:
        case 1:
            arch.mostrar_productos()
        case 2:
            arch.agregar_productos()
        case 3:
            arch.buscar_producto()
        case 4:
            print("Gracias por usar nuestro programa, abandonando la sesión...")
        case _:
            print("Opción ingresada inválida, ingrese una opción nuevamente.")