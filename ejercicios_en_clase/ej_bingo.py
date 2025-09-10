# Importamos la libreria "random" la cual vamos a utilizar mas adelante para generar números aleatorios y también para que no se repitan números
import random

print()

# Pedimos al usuario que ingrese las dimensiones de su cartón de bingo (es un código un poco mas dinámico que al hacerlo solo de 5x5)
columnas = int(input("Por favor, ingrese la cantidad de columnas de su cartón "))
filas = int(input("Por favor, ingrese la cantidad de filas de su cartón "))


# Creamos la variable "numeros" a la cual le asignamos números aleatorios únicos para llenar el cartón
# Usamos del doble de rango (filas*columnas*2) para que haya más números para sortear
numeros = random.sample(range(1, filas*columnas*2), filas*columnas)


# Creamos una variable "sorteados" que es una lista con todos los posibles números que pueden salir en el sorteo
sorteados = list(range(1, filas*columnas*2))


# Con shuffle mezclamos los números para simular el sorteo aleatorio
random.shuffle(sorteados)


# Creamos la variable "matriz_bingo" y le asignamos la lista de números del cartón en una matriz de tamaño filas x columnas
matriz_bingo = [numeros[i*columnas:(i+1)*columnas] for i in range(filas)]
print()


# Mostramos el cartón inicial al usuario
for fila in matriz_bingo:
    print(fila)
print()


# Utilizamos un bucle "while" que sigue hasta que se complete el bingo
while True:
    print()


    # Sacamos un número aleatorio de la lista de sorteados
    # pop() lo elimina de la lista para que no se repita
    numero_azar = sorteados.pop()
    

    # Creamos la variable "num_ganador" para saber si el número salió en nuestro cartón
    num_ganador = False


    # Recorremos la matriz para buscar si el número está en el cartón
    for i in range(columnas):
        for j in range(filas):
            if numero_azar == matriz_bingo[i][j]:


                # Tachamos el número encontrado en el cartón
                matriz_bingo[i][j] = 0
                num_ganador = True

    # Utilizamos un condicional "if" para saber si el número estaba en el cartón o no
    if num_ganador:

        print(f"Ha salido sorteado el número {numero_azar} y está en tu cartón!")


        # Comprobamos si alguna fila completa está marcada (LINEA)
        if any(all(n == 0 for n in fila) for fila in matriz_bingo):
            print("Usted ha conseguido completar una LINEA!!")
    else:
        print(f"Ha salido sorteado el número {numero_azar} y no está en tu cartón!")


    # Mostramos cómo queda el cartón después de cada sorteo
    for fila in matriz_bingo:
        print(fila)       


    # Comprobamos si todas las casillas del cartón están marcadas (BINGO)
    if all(all(n == 0 for n in fila) for fila in matriz_bingo):


        print("Usted ha conseguido completar el BINGO!!")
        break  # Salimos del bucle "while" y el juego termina
