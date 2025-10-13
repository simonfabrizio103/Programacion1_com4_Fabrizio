# 1) Dado el diccionario precios_frutas
# Añadir las siguientes frutas con sus respectivos precios

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
1450}

precios_frutas["Naranja"]=1200
precios_frutas["Manzana"]=1500
precios_frutas["Pera"]=2300

print()
print(f"El diccionario con las nuevas frutas es:\n {precios_frutas}")
print()



# 2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, actualizar los precios de las siguientes frutas

precios_frutas["Banana"]=1330
precios_frutas["Manzana"]=1700
precios_frutas["Melón"]=2800

print(f"El diccionario con los precios actualizados es:\n{precios_frutas}")
print()




# 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los
# precios.

frutas = precios_frutas.keys()
frutas = list(frutas)
print(f"Estas son las frutas sin sus respectivos precios:\n{frutas}")
print()




# 4) Escribí un programa que permita almacenar y consultar números telefónicos.
contactos = {}
for i in range(5):
    nombre = input(f"Ingresa el nombre de tu contacto: ")
    numero = input(f"Ingresa el número para el contacto {nombre}: ")
    contactos[nombre]=numero
print()
consultar = input(f"Por favor, ingresa el nombre del contacto del que quieres saber su número: ")
print()

if consultar in contactos:
    print(f"El número del contacto {consultar} es: {contactos[consultar]}")
else:
    print(f"No existe nadie en tus contactos con el nombre {consultar}")
print()

# 5) Solicita al usuario una frase e imprime:
# • Las palabras únicas (usando un set).
# • Un diccionario con la cantidad de veces que aparece cada palabra.

frase = input("Ingresa la frase que desees: ")
print()

palabras = frase.split()
palabras_unicas = set(palabras)
print("Las palabras únicas son las siguientes:\n", palabras_unicas)
print()

repetidas = {}
for palabra in palabras:
    if palabra in repetidas:
        repetidas[palabra] += 1
    else:
        repetidas[palabra] = 1

print("La cantidad de veces que aparece cada palabra es la siguiente:\n", repetidas)
print()



# 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
# Luego, mostrá el promedio de cada alumno.

alumnos = {}
for i in range(3):
    nombre_alumno = input(f"Ingresa el nombre del {i+1}° alumno: ")
    notas_alumno = []
    for j in range (3):
        nota = float(input(f"Ingresa la {j+1}° nota del alumno {nombre_alumno}: "))
        notas_alumno.append(nota)
    alumnos[nombre_alumno]=tuple(notas_alumno)
    print(

    )
for alumno, notas in alumnos.items():
    promedio = (notas[0] + notas[1] + notas[2])/len(notas)
    print(f"El promedio de {alumno} es de: {promedio}")
    print()



# 7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1
# y Parcial 2:
# • Mostrá los que aprobaron ambos parciales.
# • Mostrá los que aprobaron solo uno de los dos.
# • Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).

parcial_1 = {5,6,7,8,9}
parcial_2 = {7,8,9,10,11}

aprobaron_ambos = parcial_1 & parcial_2
aprobaron_uno = parcial_1 ^ parcial_2
aprobaron_al_menos_uno = parcial_2 | parcial_1

print(f"Los que aprobaron ambos parciales son: {aprobaron_ambos}")
print(f"Los que aprobaron solo uno de los dos parciales son: {aprobaron_uno}")
print(f"Los que aprobaron al menos un parcial son: {aprobaron_al_menos_uno}")




# 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
# Permití al usuario:
# • Consultar el stock de un producto ingresado.
# • Agregar unidades al stock si el producto ya existe.
# • Agregar un nuevo producto si no existe.

productos = {
    "Sandias": 20,
    "Frutillas": 50,
    "Pomelos": 37,
    "Ananás":62
}

producto = input("Por favor, ingresa el nombre del producto: ")

if producto in productos:
    nuevo_stock = int(input(f"Ingresa la cantidad de {producto} que deseas añadir al stock: "))
    productos[producto] =+ nuevo_stock
    print(f"Se ha ingresado un nuevo stock para {producto}, su stock actual es: {productos[producto]}")
else:
    stock = int(input(f"Este es un producto nuevo, por favor, indica su stock inicial: "))
    productos[producto] = stock
    print(f"El nuevo producto {producto} cuenta con un stock inicial de: {stock}")





# 9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
calendario = {
    ("Lunes", "22:00"): "Gimnasio",
    ("Martes", "10:00"): "Parcial de Matemáticas",
    ("Miércoles", "16:00"): "Torneo de Fortnite"
}
for actividad in calendario:
    print(f"Estas son las 3 actividades previstas: {actividad} {calendario[actividad]}")

consultar_dia = input("Ingresa el día en el que la actividad sucede: ").capitalize()
consultar_hora = input("Ingresa la hora en el que la actividad sucede (por ejemplo: 18:00): ")

clave = (consultar_dia,consultar_hora)

if clave in calendario:
    print(f"La actividad esperada para el día {consultar_dia} con horario {consultar_hora} es: {calendario[clave]}")
else:
    print(f"No existe una actividad para el día y horas indicados")




# 10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo
# diccionario donde:
# • Las capitales sean las claves.
# • Los países sean los valores.

paises = {
    "Estados Unidos": "Washington DC",
    "Ecuador": "Quito",
    "El Salvador": "San Salvador",
    "Argentina": "Buenos Aires"
}
invertido = {}
for pais in paises:
    invertido[paises[pais]] = pais

print("Diccionario con los paises y capitales original:", paises)
print("Diccionario con los paises y capitales invertido:", invertido)
