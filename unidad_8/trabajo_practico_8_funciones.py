# 1. Crear archivo inicial con productos: Crear un archivo de texto llamado productos.txt con tres productos. Cada línea debe tener: nombre,precio,cantidad
with open ("productos.txt","w") as archivo:
    archivo.write("Molida,4500,15\n")
    archivo.write("Avena,2350,10\n")
    archivo.write("Coca-Cola,3400,20\n")




# 2. Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada línea la procese con
# .strip() y .split(",") y muestre los productos en el siguiente formato:
def mostrar_productos():
    with open ("productos.txt","r") as archivo:
        for linea in archivo:
            nombre, precio, cantidad = linea.strip().split(",")
            print(f"Producto: {nombre} | Precio: {precio} | Cantidad: {cantidad}")
        



# 3. Agregar productos desde teclado: Modificar el programa para que luego de mostrar los productos le pida al usuario
# que ingrese un nuevo producto (nombre, precio, cantidad) y lo agregue al archivo sin borrar el contenido existente.
def agregar_productos():
    nombre = input("Ingrese el nombre del producto: ").capitalize().strip()
    precio = input("Ingrese el precio del producto: ").strip()
    cantidad = input("Ingrese la cantidad del producto: ").strip()
    producto_1 = f"{nombre},{precio},{cantidad}\n"

    with open("productos.txt", "a") as archivo:
        archivo.write(producto_1)
        
    with open ("productos.txt","r") as archivo:
        for linea in archivo:
            nombre, precio, cantidad = linea.strip().split(",")
            print(f"Producto: {nombre} | Precio: {precio} | Cantidad: {cantidad}")




# 4. Cargar productos en una lista de diccionarios: Al leer el archivo, cargar los datos en una lista llamada productos, donde
# cada elemento sea un diccionario con claves: nombre, precio, cantidad.
def cargar_productos():
    productos = []
    with open ("productos.txt","r") as archivo:
        for linea in archivo:
            nombre, precio, cantidad = linea.strip().split(",")
            producto = {
                "nombre": nombre,
                "precio": float(precio),
                "cantidad": int(cantidad)
            }
            productos.append(producto)
    return productos




# 5. Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un producto. Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. Si
# no existe, mostrar un mensaje de error.
def buscar_producto(productos):
    consultar = input("Por favor, ingrese el nombre del producto")
    for producto in productos:
        if consultar.capitalize() == producto["nombre"]:
            print(f"Producto encontrado: {producto["nombre"]} | Precio: {producto["precio"]} | Cantidad: {producto["cantidad"]}")
        else:
            print("No se encontró ningún producto")




# 6. Guardar los productos actualizados: Después de haber leído, buscado o agregado productos, sobrescribir el archivo productos.txt escribiendo nuevamente todos los
# productos actualizados desde la lista.
def guardar_productos(productos):
    with open("productos.txt", "w") as archivo:
        for producto in productos:
            linea = f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n"
            archivo.write(linea)
    print("¡Se ha actualizado el archivo de forma correcta!\n")