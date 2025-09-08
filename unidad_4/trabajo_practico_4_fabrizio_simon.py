import random

# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for i in range (101):
    print(i)
print()


# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.



num = int(input("Por favor, ingresa un número entero "))
print()
num_digitos = len(str(num))
print(num_digitos)
print()



# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores 
# dados por el usuario, excluyendo esos dos valores

val_1 = int(input("Por favor, ingresa el primer extremo "))
print()
val_2 = int(input("Por favor, ingresa el segundo extremo "))
print()

suma_1= 0
val_1 +=1

for i in range (val_1, val_2):
    suma_1 += i

print(suma_1)
print()



# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.

num_secuen = int(input("Por favor, ingresa números enteros para ser sumados, en caso de querer finalizar, ingrese 0 "))
print()
suma_2 = 0

while num_secuen != 0:
    suma_2 +=num_secuen
    num_secuen = int(input("Por favor, ingresa números enteros para ser sumados, en caso de querer finalizar, ingrese 0 "))
    print()

print(suma_2)
print()




# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

num_azar = int(input("Por favor, ingresa un número entre 0 y 9 para adivinar "))
print()
num_maquina = random.randint(0,9)
contador = 1

while num_azar!=num_maquina:
    contador+=1
    num_azar = int(input("Por favor, ingresa un número entre 0 y 9 para adivinar "))
    print()

print(f'Fueron necesarios {contador} intentos para adivinar el número aleatorio')
print()




# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos 
# entre 0 y 100, en orden decreciente.

for i in range (100, 0, -2):
    print(i)




# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un 
# número entero positivo indicado por el usuario.

val_3 = int(input("Por favor, ingresa un número entero positivo "))
print()
suma_3 = 0
for i in range (0,val_3):
    suma_3 +=i

print(f'La suma de todos los números comprendidos entre 0 y {val_3} es: {suma_3}')
print()




# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).

cont_pares = 0
cont_impares = 0
cont_positivos = 0
cont_negativos = 0


for i in range (1):
    num_entero = int(input("Por favor, ingresa números hasta llegar a 100 números ingresados "))
    print()
    if num_entero >0:
        cont_positivos+=1
    else:
        cont_negativos+=1
    
    if num_entero % 2 == 0:
        cont_pares+=1
    elif num_entero % 2 == 1:
        cont_impares+=1


print(f'Números pares: {cont_pares}')
print(f'Números impares: {cont_impares}')
print(f'Números positivos: {cont_positivos}')
print(f'Números negativos: {cont_negativos}')




# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).

suma_4 = 0
media = 0

for i in range (1):
    num_entero = int(input("Por favor, ingresa números enteros hasta llegar a 100 números ingresados "))
    print()
    suma_4 +=num_entero

media = suma_4/100
print(f'La media de los 100 números ingresados es: {media}')
print()

# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el 
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

num_normal = input("Ingresa un número para revertir los digitos: ")
num_invertido = []

for i in range(len(num_normal)-1, -1, -1):
    num_invertido.append(num_normal[i])

print("".join(num_invertido))