# Creación de variables "numero1" como entero y "numero2" como decimal.
numero1 = 600
numero2 = 98.5

print()
print("número 1: ",numero1)
print()
print("número 2: ",numero2)
print()
print("___________________________________________")
print()



# Creación de las operaciones "suma", "resta", "multiplicación" y "división".
suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2

print("suma: ",suma)
print()
print("resta: ",resta)
print()
print("multiplicación: ",multiplicacion)
print()
print("división: ",division)
print()
print("___________________________________________")
print()



# Creación de la variable "nombre"
nombre = "Juancito"

print("nombre: ",nombre)
print()
print("___________________________________________")
print()



# Creación de la variable "precio" y "descuento", luego multiplicamos la variable "descuento" a la variable "precio"
# y asi obtenemos el descuento, el cual guardamos en la variable "precio_final".
precio = 200.0
descuento = 0.25

print("precio: ",precio)
print()
print("descuento: ",descuento)
print()


precio_final = precio - (precio * descuento)
print("precio final: ",precio_final)
print()
print("___________________________________________")
print()



# Creación de la variable "cadena" y "longitud", la cual almacena la longitud de la variable cadena.
cadena = "me gusta la música"
longitud = len(cadena)
print("cadena: ",cadena)
print()
print("longitud de la variable cadena: ",longitud)
print()
print("___________________________________________")
print()



# Cración de la variable "precio" y parseo de "float" a "int".
precio = int(555.5)
print("precio: ",precio)
print()
print("___________________________________________")
print()



# Concatenación de las variables "nombre" y "apellido", arroja un string que almacenamos en la variable "nombre_completo".
nombre = "Roberto"
apellido = "Ramirez"
print("nombre: ",nombre)
print()
print("apellido: ",apellido)

nombre_completo = nombre +" "+ apellido
print()
print("nombre completo: ",nombre_completo)
print("___________________________________________")
print()


# Cración de la variable "edad" y sus respectivas operaciones.
edad = 21 + 5 - 10
print("edad: ",edad)
print()




# Creación de la variable "altura" y sus respectivas operaciones.
altura = 1.73 * 4 / 3
print("altura: ",altura)
print("___________________________________________")
print()



# Creación de la variable "mi_nombre" en mayusculas y transformación de la misma a minusculas.
mi_nombre = "FABRIZIO"
print("mi nombre en mayusculas: ",mi_nombre)
mi_nombre_minusculas = mi_nombre.lower()
print()
print("mi nombre en minusculas: ",mi_nombre_minusculas)



# Tranformamos a minusculas la variable "mi_nombre" exceptuando la primera letra.
mi_nombre_final = mi_nombre_minusculas.capitalize()
print()
print("mi nombre en minusculas excepto la primera letra: ",mi_nombre_final)
print()
print("___________________________________________")
print()