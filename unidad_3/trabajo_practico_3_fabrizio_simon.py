from statistics import mode, median, mean
import random

# 1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
# deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.
print()
edad_1 = int(input("Por favor, ingresa tu edad "))
print()

if(edad_1>=18):
    print("Usted es mayor de edad")
else:
    print("Usted es menor de edad")

print()



# 2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
# mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
# mensaje “Desaprobado”.
nota = int(input("Por favor, ingresa tu nota final "))
print()

if(nota>=6):
    print("Usted ha aprobado")
else:
    print("Usted ha desaprobado")

print()




# 3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
# número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
# contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
# operador de módulo (%) en Python para evaluar si un número es par o impar
num = int(input("Porfavor ingresa un número par "))
print()

if(num%2==0):
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

print()



# 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
# siguientes categorías pertenece:
# ● Niño/a: menor de 12 años.
# ● Adolescente: mayor o igual que 12 años y menor que 18 años.
# ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
# ● Adulto/a: mayor o igual que 30 años
edad_2 = int(input("Por favor, ingresa tu edad "))
print()
if(edad_2<12):
    print("Usted es un niño/a")
elif(edad_2>=12 and edad_2<18):
    print("Usted es un adolescente")
elif(edad_2>=18 and edad_2<30):
    print("Usted es un adulto/a jóven")
elif(edad_2>=30):
    print("Usted es un adulto/a")

print()




# 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
# (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
# pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
# pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
# de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
# como una lista o un string.
contraseña = input("Por favor, ingresa una contraseña de entre 8 y 14 carácteres ")
print()

if(len(contraseña)>=8 and len(contraseña)<=14):
    print("Usted ha ingresado una contreña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 carácteres")

print()


# 6) Escribir un programa que tome la lista
# numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
# hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

if(media>mediana and mediana>moda):
    print("Existe sesgo positivo")
elif(media<mediana and mediana<moda):
    print("Existe sesgo negativo")
elif(media==mediana and mediana==moda):
    print("No existe sesgo")

print()



# 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
# termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
# pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
# pantalla.
frase = input("Por favor, ingresa una palabra o una frase ")
vocales = ["A","E","I","O","U"]
ultima_letra = frase[(len(frase))-1]
ultima_letra = ultima_letra.upper()

if(vocales.count(ultima_letra)>0):
    print("La última letra de tu frase es una vocal")
    frase = frase+"!"
    print(frase)
else:
    print("La última letra de tu frase no es una vocal")
    print(frase)



# 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
# dependiendo de la opción que desee:
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
nombre = input("Por favor, ingrese su nombre ")

print("Ingrese la opción 1 si desea su nombre en Mayusculas")
print("Ingrese la opción 2 si desea su nombre en Minusculas")
opcion = int(input("ingrese la opción 3 si desea la primera letra de su nombre en Mayusculas y el resto en minusculas "))

if(opcion == 1):
    print(nombre.upper())
elif(opcion == 2):
    print(nombre.lower())
elif(opcion == 3):
    print(nombre.capitalize())



#9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
# magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
# por pantalla
magnitud = int(input("Por favor, ingresa la magnitud de un terremoto "))

if(magnitud<3):
    print("Categoria: *MUY LEVE* (imperceptible)")
elif(magnitud>=3 and magnitud<4):
    print("Categoria: *LEVE* (ligeramente perceptible)")
elif(magnitud>=4 and magnitud<5):
    print("Categoria: *MODERADO* (sentido por personas, pero generalmente no causa daños)")
elif(magnitud>=5 and magnitud<6):
    print("Categoria: *FUERTE* (puede causar daños en estructuras débiles)")
elif(magnitud>=6 and magnitud<7):
    print("Categoria: *MUY FUERTE* (puede causar daños significativos)")
elif(magnitud>=7):
    print("Categoria: *EXTREMO* (puede causar graves daños a gran escala)")



# 10) Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
# del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
# si el usuario se encuentra en otoño, invierno, primavera o verano.
hemisferio = input("Por favor, ingresa el hermisferio en el que te encuentras (N/S) ")
hemisferio = hemisferio.upper()
print()

mes_año = input("Por favor, ingresa el mes del año en el que te encuentras ")
mes_año = mes_año.upper()
print()

dia = input("Por favor, ingresa el día en el que te encuentras (números) ")
print()

meses = ["ENERO","FEBRERO","MARZO","ABRIL","MAYO","JUNIO","JULIO","AGOSTO","SEPTIEMBRE","OCTUBRE","NOVIEMBRE","DICIEMBRE"]


if((mes_año==meses[11]and dia>=21)or mes_año==meses[0]or mes_año==meses[1]or (mes_año==meses[2]and dia<=20)):
        if(hemisferio=="N"):
            print("Te encuentras en la estación de Invierno")
        else:
            print("Te encuentras en la estación de Verano")

if((mes_año==meses[2]and dia>=21)or mes_año==meses[3]or mes_año==meses[4]or (mes_año==meses[5]and dia<=20)):
        if(hemisferio=="N"):
            print("Te encuentras en la estación de Primavera")
        else:
            print("Te encuentras en la estación de Otoño")

if((mes_año==meses[5]and dia>=21)or mes_año==meses[6]or mes_año==meses[7]or (mes_año==meses[8]and dia<=20)):
        if(hemisferio=="N"):
            print("Te encuentras en la estación de Verano")
        else:
            print("Te encuentras en la estación de Invierno")
            
if((mes_año==meses[8]and dia>=21)or mes_año==meses[9]or mes_año==meses[10]or (mes_año==meses[11]and dia<=20)):
        if(hemisferio=="N"):
            print("Te encuentras en la estación de Otoño")
        else:
            print("Te encuentras en la estación de Primavera")

