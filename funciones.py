# Aca van a ir todas las funciones necesarias para el juego. Despues se van a importar al main.py

import pprint
from variables import *
import time
import random

# Funcion para crear los tableros. La variable "tamano" esta en el fichero de variable y desde ahi puedes elegir el tamaño de tu tablero.
def crear_tablero(tamano):
    tablero = [[" " for i in range(tamano)] for j in range(tamano)]

    return tablero


# Funcion para elegir la posicion de tus barcos.

def posicionar_barcos_fijos_mio(tablero):
     tablero[3][3] = 'B'
     tablero[4][3] = 'B'
     tablero[5][3] = 'B'
     tablero[6][3] = 'B'

     tablero[1][0] = 'B'
     tablero[1][1] = 'B'
     tablero[1][2] = 'B'
    
    
     tablero[4][5] = 'B'
     tablero[4][6] = 'B'
     tablero[4][7] = 'B'
    
     tablero[7][2] = 'B'
     tablero[8][2] = 'B'
    
     tablero[9][0] = 'B'
     tablero[9][1] = 'B'

     tablero[0][9] = 'B'

     tablero[2][8] = 'B'

     tablero[7][8] = 'B'

     tablero[9][6] = 'B'


# Funcion para elegir los barcos del ordenador. (Se mejorara haciendo que sea aleatorio en un futuro.)

def posicionar_barcos_fijos_ordenador(tablero):
     tablero[3][6] = 'B'
     tablero[4][6] = 'B'
     tablero[5][6] = 'B'
     tablero[6][6] = 'B'

     tablero[8][0] = 'B'
     tablero[8][1] = 'B'
     tablero[8][2] = 'B'
    
    
     tablero[1][5] = 'B'
     tablero[1][6] = 'B'
     tablero[1][7] = 'B'
    
     tablero[5][2] = 'B'
     tablero[6][2] = 'B'
    
     tablero[0][0] = 'B'
     tablero[0][1] = 'B'

     tablero[3][3] = 'B'

     tablero[5][9] = 'B'

     tablero[7][7] = 'B'

     tablero[9][9] = 'B'



# Funcion para calcular las vidas que le quedan a ambos jugadores, con ella contamos las "B" que haya en el tablero y asi va en funcion de la cantidad de barcos que hayas decidido poner.
def calcular_vidas(tablero):
    """Cuenta cuántas casillas con 'B' hay en el tablero (vidas)"""
    return sum(fila.count('B') for fila in tablero)    



# Funcion para ejecutar el turno del jugador.
def turno_jugador(tablero_computer, tablero_mio_visualizar):
    acierto = True
    while acierto:
        time.sleep(0.5)
        vidas_computer = calcular_vidas(tablero_computer)
        time.sleep(1)
        print("Vidas del ordenador")
        print(vidas_computer)
        if vidas_computer== 0:
            print("Felicidades! Has ganado!")
            break
        i = int(input("Por favor introduzca la coordenada (de 0 a 9) para la fila"))
        j = int(input("Por favor introduzca la coordenada (de 0 a 9) para la columna"))
        print (i,j)
        time.sleep(1.5)
        if i >= 10 or j >= 10:
            print("tus coordenadas, se salen del tablero, vuelve a probar")
        elif i >= 0 and i <= 9 and j >= 0 and j <= 9:
            acierto = disparo(tablero_computer,tablero_mio_visualizar,i,j)
            print()
            pprint.pprint(tablero_mio_visualizar)
            print()
        else:
            print("Tus coordenadas son negativas")
            acierto = False
            


# Funcion para ejecutar los disparos

def disparo(tablero_computer,tablero_mio_visualizar,i,j):
    if tablero_computer[i][j] == 'B':
        print("Tocado")
        time.sleep(1.5)
        tablero_computer[i][j] = "X"
        tablero_mio_visualizar[i][j] = "X"
        return True
    elif tablero_computer[i][j] == " ":
        print("Agua")
        time.sleep(1.5)
        tablero_computer[i][j] = "O"
        tablero_mio_visualizar[i][j] = "O"
        return False
    else:
        print("Ya habías disparado allí, no has visto bien")
        return False



# Funcion para ejecutar el turno del ordenador.

def turno_computer(tablero_mio, tablero_computer_visualizar):
    acierto = True
    while acierto:
        time.sleep(0.5)
        vidas_jugador=calcular_vidas(tablero_mio)
        time.sleep(1)
        print("Vidas del jugador")
        print(vidas_jugador)
        if vidas_jugador== 0:
            print("Que malo eres... Has perdido!")
            break
        i =random.randrange(0,10)
        j =random.randrange(0,10)
        time.sleep(2)
        print (i,j)
        time.sleep(1.5)
        if i >= 10 or j >= 10:
            print("tus coordenadas, se salen del tablero, vuelve a probar")
        elif i >= 0 and i <= 9 and j >= 0 and j <= 9:
            acierto = disparo(tablero_mio, tablero_computer_visualizar,i,j)
            print()
            pprint.pprint(tablero_mio)
            print()
        else:
            print("Tus coordenadas son negativas")
            acierto = False   
    
    
def visualizar(tablero):
    pprint.pprint(tablero)
    
    
# Funcion para mostrar un pequeño mensaje de bienvenida   
def mensaje_bienvenida():
    print("Bienvenido al juego de HLF")
    print()
    
    
    
    
    
    
    
