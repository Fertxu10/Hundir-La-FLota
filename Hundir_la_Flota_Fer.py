from funciones import *
from variables import *
#from clases import *
import os
import pprint
import time

mensaje_bienvenida()
time.sleep(3)
tablero_mio = crear_tablero(tamano)
tablero_mio_visualizar = crear_tablero(tamano)
tablero_computer = crear_tablero(tamano)
tablero_computer_visualizar = crear_tablero(tamano)
posicionar_barcos_fijos_mio(tablero_mio)
posicionar_barcos_fijos_ordenador(tablero_computer)
print()
pprint.pprint(tablero_mio_visualizar)
print()
pprint.pprint(tablero_mio)
print()
time.sleep(4)
print("Tablero de la computadora con barcos fijos. Te doy 10 segundos para que los memorices...")
print()
time.sleep(5)
visualizar(tablero_computer)
time.sleep(5)
os.system("cls")
print()
while True:
    print ("Tus disparos")
    pprint.pprint(tablero_mio_visualizar)
    print()
    turno_jugador(tablero_computer, tablero_mio_visualizar)
    turno_computer(tablero_mio,tablero_computer_visualizar)
    vidas_jugador=calcular_vidas(tablero_mio)
    if vidas_jugador == 0:
        break
    vidas_computer=calcular_vidas(tablero_computer)
    if vidas_computer == 0:
        break





