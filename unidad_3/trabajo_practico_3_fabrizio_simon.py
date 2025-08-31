from statistics import mode, median, mean
import random


print()
edad_1 = int(input("Por favor, ingresa tu edad "))
print()

if(edad_1>=18):
    print("Usted es mayor de edad")
else:
    print("Usted es menor de edad")

print()

nota = int(input("Por favor, ingresa tu nota final "))
print()

if(nota>=6):
    print("Usted ha aprobado")
else:
    print("Usted ha desaprobado")

print()



num = int(input("Porfavor ingresa un número par "))
print()

if(num%2==0):
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

print()



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


contraseña = input("Por favor, ingresa una contraseña de entre 8 y 14 carácteres ")
print()

if(len(contraseña)>=8 and len(contraseña)<=14):
    print("Usted ha ingresado una contreña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 carácteres")

print()

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

frase = input("Por favor, ingresa una palabra o una frase ")
vocales = ["A","E","I","O","U"]
ultima_letra = frase[(len(frase))-1]
ultima_letra = ultima_letra.upper()

if(vocales.count(ultima_letra)>0):
    print("La última letra de tu frase es una vocal")
    print(frase,"!")
else:
    print("La última letra de tu frase no es una vocal")
    print(frase)

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


hemisferio = input("Por favor, ingresa el hermisferio en el que te encuentras (N/S) ")
mes_año = input("Por faovr, ingresa el mes del año en el que te encuentras ")
dia = input("Por favor, ingresa el día en el que te encuentras (números)")
meses = ["ENERO","FEBRERO","MARZO","ABRIL","MAYO","JUNIO","JULIO","AGOSTO","SEPTIEMBRE","OCTUBRE","NOVIEMBRE","DICIEMBRE"]

if((mes_año==meses[11]and dia>=21)or mes_año==meses[0]or mes_año==meses[1]or (mes_año==meses[2]and dia<=20)):
        if(hemisferio=="N"):
            print("Invierno")
        else:
            print("Verano")

if((mes_año==meses[2]and dia>=21)or mes_año==meses[3]or mes_año==meses[4]or (mes_año==meses[5]and dia<=20)):
        if(hemisferio=="N"):
            print("Primavera")
        else:
            print("Otoño")

if((mes_año==meses[5]and dia>=21)or mes_año==meses[6]or mes_año==meses[7]or (mes_año==meses[8]and dia<=20)):
        if(hemisferio=="N"):
            print("Verano")
        else:
            print("Invierno")
            
if((mes_año==meses[8]and dia>=21)or mes_año==meses[9]or mes_año==meses[10]or (mes_año==meses[11]and dia<=20)):
        if(hemisferio=="N"):
            print("Otoño")
        else:
            print("Primavera")

