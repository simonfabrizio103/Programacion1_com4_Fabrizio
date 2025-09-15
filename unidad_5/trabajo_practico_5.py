
# 1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función range.


lista_num = []
for i in range (1,101):
    if i % 4 == 0:
        lista_num.append(i)
print(lista_num)
print()




# 2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el penúltimo. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el
# indexing con números negativos!

lista_elemt = ["Ryzen", "Nvidia", "Intel","Logitech","Razer"]
print(lista_elemt[len(lista_elemt)-2])
print()





# 3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por
# pantalla. Pista: para crear una lista vacía debes colocar los corchetes sin nada en su interior.

lista_1 = []
for i in range (3):
    palabra = input("Por favor ingresa una palabra hasta llenar la lista ")
    lista_1.append(palabra)
print(lista_1)
print()





# 4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”, 
# respectivamente. Imprimir la lista resultante por pantalla.

animales = ["perro", "gato", "conejo", "pez"]
for i in range(len(animales)):
    if i == 1:
        animales [i] = "loro"

    if i == len(animales)-1:
        animales [i] = "oso"

print(animales)
print()    




# 5) Analizar el programa y explicar con tus palabras qué es lo que realiza.

# El programa crea una variable "numeros", la cual es una lista con diferentes números,
# lo que hace el programa es remover o quitar el número mas grande con la función "max" y después lo imprime





# 6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por
# pantalla los dos primeros.

lista = list(range(10, 31, 5))

print(lista[0])
print(lista[1])
print()




# 7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores
# cualesquiera.

autos = ["sedan", "polo", "suran", "gol"]
print(autos)
print()

autos[1:3] = ["audi","ferrari"]
print(autos)
print()




# 8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append
# directamente. Imprimir la lista resultante por pantalla

dobles = []

for i in range (5,20,5):
    dobles.append(i*2)

print(dobles)
print()




# 9) Dada la lista “compras”, cuyos elementos representan los productos comprados por
# diferentes clientes:

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

compras[2].append("jugo")

compras[1][1] = compras[1][1].replace("fideos", "tallarines", 1)

compras[0][0] = compras[0][0].removesuffix("pan")

print(compras)




# 10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:

# lista_anidada[0]: 15
# lista_anidada[1]: True
# lista_anidada[2][0]: 25.5
# lista_anidada[2][1]: 57.9
# lista_anidada[2][2]: 30.6
# lista_anidada[3]: False

# Imprimir la lista resultante por pantalla.


lista_anidada = [[15],[True],[25.5,57.9,30.6],[False]]
print(lista_anidada)