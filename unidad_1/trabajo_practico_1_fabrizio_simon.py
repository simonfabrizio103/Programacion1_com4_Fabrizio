#1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”
print("Hola mundo")
print()


# 2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
# el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
# por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
# realizar la impresión por pantalla

nombre_del_usuario = input("Ingresa tu nombre porfavor ")
print()
print(f' ¡Hola {nombre_del_usuario}!')
print()


# 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
# imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
# “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
# años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
# la impresión por pantalla.

nombre_1 = input("Porfavor ingresa tu nombre ")
print()
apellido_1 = input("Porfavor ingresa tu apellido ")
print()
edad = int(input("porfavor ingresa tu edad "))
print()
residencia = input("Porfavor ingresa tu lugar de residencia ")
print()

print(f'Soy {nombre_1} {apellido_1}, tengo {edad} años y vivo en {residencia}')
print()


# 4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
# su perímetro.

radio = float(input("Porfavor ingresa el radio de un circulo "))
print()
area = 3.14 * (radio*radio)
perimetro = 2 * 3.14 * radio
print(f'El area del circulo con el radio que ingresaste es {area}cm y su perimetro es {perimetro}cm')
print()


# 5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
# cuántas horas equivale.

segundos = int(input("Porfavor ingresa la cantidad de segundos que desees "))
print()
horas = segundos / 3600
print(f'La cantidad de horas según los segundos que ingresaste equivale a: {horas} horas')
print()


# 6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
# multiplicar de dicho número.

numero_tabla = int(input("Porfavor ingresa un número y te diré su tabla de multiplicar "))

multiplicar_0 = numero_tabla*0
multiplicar_1 = numero_tabla*1
multiplicar_2 = numero_tabla*2
multiplicar_3 = numero_tabla*3
multiplicar_4 = numero_tabla*4
multiplicar_5 = numero_tabla*5
multiplicar_6 = numero_tabla*6
multiplicar_7 = numero_tabla*7
multiplicar_8 = numero_tabla*8
multiplicar_9 = numero_tabla*9
multiplicar_10 = numero_tabla*10

print(f'La tabla de multiplicar del número {numero_tabla} es: ')
print()
print(f'{numero_tabla}*0 = {multiplicar_0}')
print(f'{numero_tabla}*1 = {multiplicar_1}')
print(f'{numero_tabla}*2 = {multiplicar_2}')
print(f'{numero_tabla}*3 = {multiplicar_3}')
print(f'{numero_tabla}*4 = {multiplicar_4}')
print(f'{numero_tabla}*5 = {multiplicar_5}')
print(f'{numero_tabla}*6 = {multiplicar_6}')
print(f'{numero_tabla}*7 = {multiplicar_7}')
print(f'{numero_tabla}*8 = {multiplicar_8}')
print(f'{numero_tabla}*9 = {multiplicar_9}')
print(f'{numero_tabla}*10 = {multiplicar_10}')
print()



# 7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
# pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

numero_operaciones0 = int(input("Porfavor ingresa un número distinto de 0 "))
print()
numero_operaciones1 = int(input("Porfavor ingresa otro número distinto de 0 "))
print()

suma = numero_operaciones0 + numero_operaciones1
division = numero_operaciones0 / numero_operaciones1
multiplicacion = numero_operaciones0 * numero_operaciones1
resta = numero_operaciones0 - numero_operaciones1

print(f'La suma de {numero_operaciones0} y {numero_operaciones1} es: {suma}')
print()
print(f'La división de {numero_operaciones0} y {numero_operaciones1} es: {division}')
print()
print(f'La multiplicación de {numero_operaciones0} y {numero_operaciones1} es: {multiplicacion}')
print()
print(f'La resta de {numero_operaciones0} y {numero_operaciones1} es: {resta}')
print()



# 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
# de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente
# modo:

altura = float(input("Porfavor ingresa tu altura en metros "))
print()
peso = float(input("Porfavor ingresa tu peso "))
print()
indice_de_masa = peso/(altura*altura)

print(f'Tu índice de masa corporal es: {indice_de_masa}')
print()



# 9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
# pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:

temperatura_celsius = float(input("Ingresa porfavor una temperatura en grados Celsius "))
print()
temperatura_fahrenheit = 9/5 * temperatura_celsius + 32

print(f'{temperatura_celsius}° Celsius equivalen a {temperatura_fahrenheit}° Fahrenheit')
print()



# 10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
# dichos números.

numero_prome_1 = float(input("Porfavor ingresa el primer número "))
print()
numero_prome_2 = float(input("Porfavor ingresa el segundo número "))
print()
numero_prome_3 = float(input("Porfavor ingresa el tercer número "))
print()

promedio = (numero_prome_1 + numero_prome_2 + numero_prome_3) / 3
print(f'El promedio entre {numero_prome_1}, {numero_prome_2} y {numero_prome_3} es: {promedio}')
print()