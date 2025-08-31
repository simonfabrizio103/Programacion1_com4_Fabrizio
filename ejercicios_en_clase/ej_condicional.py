# Importo la libreria "sys" para poder finalizar el programa cuando haya un dato mal ingresado
import sys


# Creo la lista "semana" con el fin de en un futuro poder comparar el día ingresado por el usuario
semana = ["LUNES","MARTES","MIERCOLES","JUEVES","VIERNES"]
print()


# Le pido al usuario ingresar la fecha en el formato indicado
fecha_usuario = input("Porfavor ingresa la fecha en formato 'Día, DD/MS' ")


# Separo la fecha ingresada con una "," para ir desglosando los datos
datos_dia = fecha_usuario.split(",")


# Le asigno a la variable "datos_numeros" la posición [1] de la lista,
# que devuelve la parte del día y del mes (DD/MM), para seguir desglosando los datos
datos_numeros = datos_dia[1]


# Le asigno a la variable "dia" la posición [0] de la lista,
# que devuelve la parte en la que el usuario dice el día y lo paso a mayusculas para que no haya errores de tipeo
dia = str(datos_dia[0]).upper()


# Utilizo la variable "contador" para poder saber si el usuario ingresó un día válido
contador = semana.count(dia)


# Utilizo un condicional "if" para corroborar que el día ingresado por el usuario sea un día válido, si no, el programa termina
if(contador<1):
    print()
    print("Dia no válido, cerrando programa...")
    sys.exit()

print()


# Separo la fecha ingresada con una "/" para seguir desglosando los datos
datos_numeros = datos_numeros.split("/")


# Le asigno a la variable "dia_num" la posición [0] de la lista,
# que devuelve la parte del número del día
dia_num = int(datos_numeros[0])


# Compruebo con un condicional "if" si el número de día que ingresó el usuario es válido, si no, el programa termina
if(not(dia_num>0 and dia_num<=31)):
    print("Número de dia no válido, cerrando programa...")
    sys.exit()


# Le asigno a la variable "mes_num" la posición [1] de la lista,
# que devuelve la parte del número del mes
mes_num = int(datos_numeros[1])


# Compruebo con un condicional "if" si el número de mes que ingresó el usuario es válido, si no, el programa termina
if(not(mes_num>0 and mes_num<=12)):
    print("Número de mes no válido, cerrando programa...")
    sys.exit()


# Encasillo con un condicional "if" los días "LUNES, MARTES Y MIERCOLES" comparando justamente
# el día ingresado por el usuario con el indice del 0 al 2 de la lista "semana"
if(semana[0]==dia or semana[1]==dia or semana[2]==dia):
    if(semana[0]==dia):
        print("Usted ingresó el nivel inical")
        print()
    if(semana[1]==dia):
        print("Usted ingresó el nivel intermedio")
        print()
    if(semana[2]==dia):
        print("Usted ingresó el nivel avanzado")      
    print()
    aprobados = int(input("Porfavor ingrese la cantidad de alumnos aprobados "))
    print()
    desaprobados = int(input("Porfavor ingrese la cantidad de alumnos desaprobados "))
    total = aprobados + desaprobados
    porc_aprobados = (aprobados/total)*100
    print("El porcentaje de alumnos aprobados es: ",porc_aprobados)   


# Encasillo con un condicional "if" el día jueves para poder saber si asistió la mayoria o minoria comparando con un "if" anidado
elif(semana[3]==dia):
   asistencia = float(input("Porfavor ingresa el porcentaje de asistencia a clase "))
   print()
   if(asistencia>=50):
       print("Asistió la mayoria")
       print()
   else: 
        print("Asistió la minoria")
        print()


# Encasillo con un condicional "if" el día viernes, y en caso de que sea el día 1 del mes 1 o el día 1 del mes 7,
# se ingresa la cantidad de alumnos nuevos y el precio del arancel por alumno, sacando asi el total
elif(semana[4]==dia):
    if((dia_num==1 and mes_num==1)or(dia_num==1 and mes_num==7)):
        print("Comienzo del nuevo ciclo")
        print()
        cant_alumnos = int(input("Ingresa la cantidad de alumnos del nuevo ciclo"))
        arancel_por_alumno = int(input("Ingresa el arancel por alumno"))
        total_arancel = cant_alumnos*arancel_por_alumno
        print("El arancel total es: ",total_arancel)
