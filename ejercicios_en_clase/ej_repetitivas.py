# Importo la libreria "random" con el fin de poder generar numeros aleatorios
import random


# Le pido al usuario que ingrese la cantidad de lugares que se van a correr las letras
lugares = int(input("Por favor, ingresa la cantidad de lugares que se correrán las letras "))
print()
# Creo una lista del abecedario para poder correr las letras
abc = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z"]


# Creo un bucle "for" con el fin de pedir los 5 mensajes
for i in range(5):

    # Le pido al usuario ingresar el mensaje y lo paso a mayusculas para que no haya error al encontras la letra en el abecedario
    mensaje = list(input(f'Por favor, ingrese su mensaje número {i+1} ').upper())
    print()

    # Creo una variable que va almacenar el mensaje completo ya que vamos a ir corriendo las letras y necesito una variable que almacene la palabra con las letras corridas
    mensaje_cesar = ""
    
    # Creo un bucle "for" para recorrer cada letra del mensaje y poder ir corriendo letra por letra
    for i in range((len(mensaje))):

        

        # Creo un condicional "if" con el fin de corroborar que cada caracter del mensaje ingresado por el usuario exista dentro del abecedario
        if mensaje[i] in abc:

            # Creo una variable "pos" que almacena el índice donde se encuentra el carácter en la posición "i" del mensaje teniendo en cuenta el abecedario
            pos = abc.index(mensaje[i])

            # Creo una variable "nueva_pos" que almacena el índice de cada carácter ya con los lugares corridos
            nueva_pos = (pos + lugares) %len(abc)

            # Le asigno a "mensaje[i]" la posición con los lugares corridos
            mensaje[i] = abc[nueva_pos]
            
            # Le asigno a "mensaje_cesar" cada uno de los cáracteres ya corridos para tener el mensaje completo en una palabra
            mensaje_cesar = mensaje_cesar + mensaje[i]

    print("Sú mensaje cifrado es:",mensaje_cesar)
    print()




# Creo una lista "Jugadas" con los diferentes movimientos que puede hacer la máquina
jugadas = ["Piedra", "Papel", "Tijera"]

# Creo una variable "cont_maquina" para contabilizar las victorias de la máquina
cont_maquina = 0

# Creo una variable "cont_perso" para contabilizar las victorias de la persona
cont_perso = 0

# Creo un bucle "while" para que el juego continua infinitamente hasta que el usuario ingrese "salir"
while jugada !="Salir":

    # Le doy al usuario las opciones a elegir
    print("Elija una de las siguientes opciones")
    print()
    print()
    print("° Piedra")
    print("_________")
    print()
    print("° Papel")
    print("_________")
    print()
    print("° Tijera")
    print()

    # Creo una variable "num_jugada" que almacena un número aleatorio entre 0 y 2 para que la elección de la máquina sea al azar
    num_jugada = random.randint(0,2)

    print()
    # Le pido al usuario ingresar su opción
    jugada = input().capitalize()
    print()

    # Le asigno a "jugada_maquina" algún indice aleatorio de la lista "jugadas" para que la jugada seleccionada sea al azar
    jugada_maquina = jugadas[num_jugada]

    # Creo un condicional "if" para que cuando el usuario ingrese "salir" para finalizar el programa, no se impriman las jugadas seleccionadas por la persona  y la máquina
    if(jugada != "Salir"):
        print(f'(tu) {jugada} vs (máquina) {jugada_maquina}')

    # Creo un condicional "if" y varios  "elif" anidados para comparar la jugada de la máquina con la jugada de la persona y muestro el resultado
    # por pantalla, además le sumo 1 al conteo de la máquina o al conteo del jugador dependiendo de quien haya ganado la ronda   
    if(jugada_maquina=="Piedra" and jugada == "Tijera"):
        print("¡Perdiste!")
        print()
        cont_maquina += 1
        continue    
    elif(jugada=="Piedra" and jugada_maquina == "Tijera"):
        print("¡Ganaste!")
        print()
        cont_perso += 1
        continue
    elif(jugada_maquina=="Tijera" and jugada == "Papel"):
        print("¡Perdiste!")
        print()
        cont_maquina += 1
        continue
    elif(jugada=="Tijera" and jugada_maquina == "Papel"):
        print("¡Ganaste!")
        print()
        cont_perso += 1
        continue
    elif(jugada_maquina=="Papel" and jugada == "Piedra"):
        print("¡Perdiste!")
        print()
        cont_maquina += 1
        continue 
    elif(jugada=="Papel" and jugada_maquina == "Piedra"):
        print("¡Ganaste!")
        print()
        cont_perso += 1
        continue
    elif(jugada_maquina == jugada):
        print("¡Empate!")
        print()
        continue

# Muestro una tabla del resultado general con el total de victorias de cada jugador
print("                          Tabla general")
print("____________________________________________________________________")
print()
print(f'   puntuación máquina: {cont_maquina}          |          puntuación persona: {cont_perso}')
print() 
