import math

# 1. Crear una función llamada imprimir_hola_mundo que imprima por
# pantalla el mensaje: “Hola Mundo!”.
def imprimir_hola_mundo():
    print("Hola Mundo!")

imprimir_hola_mundo()


# 2. Crear una función llamada saludar_usuario(nombre) que reciba
# como parámetro un nombre y devuelva un saludo personalizado.
def saludar_usuario(nombre):
    print(f"Hola {nombre}!")

nombre = input("Ingresa tu nombre por favor: ")
saludar_usuario(nombre)

# 3. Crear una función llamada informacion_personal(nombre, apellido,
# edad, residencia) que reciba cuatro parámetros e imprima: “Soy
# [nombre] [apellido], tengo [edad] años y vivo en [residencia]”.
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

nombre = input("Ingresa tu nombre por favor: ")
apellido = input("Ingresa tu apellido por favor: ")
edad = int(input("Ingresa tu edad por favor: "))
residencia = input("Ingresa donde vives por favor: ")
informacion_personal(nombre, apellido, edad,residencia.capitalize())

# 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro
# y devuelva el área del círculo. calcular_perimetro_circulo(radio)
# que reciba el radio como parámetro y devuelva el perímetro del círculo.
def calcular_area_circulo(radio):
    area = math.pi * (radio*radio)
    return area

def calcular_perimetro_circulo(radio):
    perimetro = 2 * math.pi * radio
    return perimetro

radio = float(input("Ingresa el radio de tu circulo: "))
area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)
print(f"El area de tu circulo es: {area} y el perimetro del mismo es: {perimetro}")




# 5. Crear una función llamada segundos_a_horas(segundos) que reciba
# una cantidad de segundos como parámetro y devuelva la cantidad
# de horas correspondientes. 
def segundos_a_horas(segundos):
    horas = segundos/3600
    return horas

segundos = int(input("Ingresa la cantidad de segundos: "))
horas = segundos_a_horas(segundos)
print(f"{segundos} segundos son {horas} horas")



# 6. Crear una función llamada tabla_multiplicar(numero) que reciba un
# número como parámetro y imprima la tabla de multiplicar de ese
# número del 1 al 10.
def tabla_multiplicar(numero):
    print(f"La tabla del {numero} es:")
    for i in range(1,11):
        print(f"{numero} x {i} = {numero*i}")

numero = int(input("Ingresa un número entero: "))
tabla_multiplicar(numero)


# 7. Crear una función llamada operaciones_basicas(a, b) que reciba
# dos números como parámetros y devuelva una tupla con el resultado de sumarlos,
# restarlos, multiplicarlos y dividirlos. 
def operaciones_basicas(a, b):
    suma = a+b
    resta = a-b
    multiplicacion = a*b
    division = a/b

    resultados = (suma,resta,multiplicacion,division)
    return resultados

num1 = int(input("Ingresa el primer número entero: "))
num2 = int(input("Ingresa el segundo número entero: "))
resultados = operaciones_basicas(num1,num2)
print("suma  resta  multiplicación  división")
print(f"suma = {resultados[0]} | resta = {resultados[1]} | multiplicación = {resultados[2]} | división = {resultados[3]}")




# 8. Crear una función llamada calcular_imc(peso, altura) que reciba el
# peso en kilogramos y la altura en metros, y devuelva el índice de
# masa corporal (IMC).
def calcular_imc(peso,altura):
    imc = peso/(altura*altura)
    return imc

peso = float(input("Ingresa tu peso corporal: "))
altura = float(input("Ingresa tu altura: "))
imc = calcular_imc(peso, altura)
print(f"Tu IMC según tu peso y altura ingresados es: {imc}")



# 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
# una temperatura en grados Celsius y devuelva su equivalente en
# Fahrenheit. 
def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius*1.8)+32
    return fahrenheit

grados_celsius = float(input("Ingresa la temperatura celsius: "))
grados_fahrenheit = celsius_a_fahrenheit(grados_celsius)
print(f"Los {grados_celsius}°C  son: {grados_fahrenheit}°F")




# 10. Crear una función llamada calcular_promedio(a, b, c) que reciba
# tres números como parámetros y devuelva el promedio de ellos.
def calcular_promedio(a,b,c):
    promedio = (a+b+c)/3
    return promedio

num3 = float(input("Ingresa el primero de tres números: "))
num4 = float(input("Ingresa el segundos de tres números: "))
num5 = float(input("Ingresa el tercero de tres números: "))
promedio = calcular_promedio(num3,num4,num5)
print(f"El promedio entre {num3}, {num4} y {num5} es: {promedio}")