import os
import random
import keyboard
from time import sleep

def juego():
    #8x8 matrix
    jugador = 0
    tablero = [
        ["⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜"],
        ["⬜", "⬜", "⬜", "⬛", "⬛", "⬛", "⬜", "⬜"],
        ["⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬛", "⬜"],
        ["⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬛", "⬜"],
        ["⬜", "⬜", "⬜", "⬜", "⬜", "⬛", "⬜", "⬜"],
        ["⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬛", "⬜"],
        ["⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬛", "⬜"],
        ["⬜", "⬜", "⬜", "⬛", "⬛", "⬛", "⬜", "⬜"]
    ]

    os.system('cls' if os.name == 'nt' else 'clear')
    for fila in tablero:
        print("".join(fila))
    sleep(1)

    tablero = [
        ["⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜"],
        ["⬜", "⬜", "⬜", "⬛", "⬛", "⬛", "⬜", "⬜"],
        ["⬜", "⬜", "⬛", "⬜", "⬜", "⬜", "⬛", "⬜"],
        ["⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬛", "⬜"],
        ["⬜", "⬜", "⬜", "⬜", "⬜", "⬛", "⬜", "⬜"],
        ["⬜", "⬜", "⬜", "⬜", "⬛", "⬜", "⬜", "⬜"],
        ["⬜", "⬜", "⬜", "⬛", "⬜", "⬜", "⬜", "⬜"],
        ["⬜", "⬜", "⬛", "⬛", "⬛", "⬛", "⬛", "⬜"]
    ]

    os.system('cls' if os.name == 'nt' else 'clear')
    for fila in tablero:
        print("".join(fila))
    sleep(1)

    tablero = [
        ["⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜"],
        ["⬜", "⬜", "⬜", "⬜", "⬛", "⬜", "⬜", "⬜"],
        ["⬜", "⬜", "⬜", "⬛", "⬛", "⬜", "⬜", "⬜"],
        ["⬜", "⬜", "⬜", "⬜", "⬛", "⬜", "⬜", "⬜"],
        ["⬜", "⬜", "⬜", "⬜", "⬛", "⬜", "⬜", "⬜"],
        ["⬜", "⬜", "⬜", "⬜", "⬛", "⬜", "⬜", "⬜"],
        ["⬜", "⬜", "⬜", "⬜", "⬛", "⬜", "⬜", "⬜"],
        ["⬜", "⬜", "⬛", "⬛", "⬛", "⬛", "⬜", "⬜"]
    ]

    os.system('cls' if os.name == 'nt' else 'clear')
    for fila in tablero:
        print("".join(fila))
    sleep(1)

    tablero = [
        ["⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜"],
        ["⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜"],
        ["⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜"],
        ["⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜"],
        ["⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜"],
        ["⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜"],
        ["⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜"],
        ["⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜"]
    ]

    playing = True
    while playing:
        new_car = random.randint(0,7)
        tablero[0][new_car] = "🚙"
        tablero[7][jugador] = "🚗"
        os.system('cls' if os.name == 'nt' else 'clear')
        for fila in tablero:
            print("".join(fila))

        #input
        key = keyboard.read_key()

        if key == "q":
            playing = False
            break
        elif key == "a" and jugador > 0:
            tablero[7][jugador] = "⬜"
            jugador -= 1
        elif key == "d" and jugador < 7:
            tablero[7][jugador] = "⬜"
            jugador += 1
        
        if tablero[7][jugador] == "🚙" or tablero[6][jugador] == "🚙":
            playing = False
            print("Perdiste!")

        #move cars down
        for i in range(7):
            tablero[7-i] = tablero[6-i]
        
        tablero[0] = ["⬜" for x in range(8)]

def main():
    juego()

if __name__ == "__main__":
    main()