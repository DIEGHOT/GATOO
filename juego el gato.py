import random

def mostrar_tablero(tablero):
    print("\n   1  2  3")
    print("  -----------")
    for i in range(3):
        print(f"{i+1} | {' | '.join(tablero[i])} |")

def nueva_partida():
    tablero = [[" " for _ in range(3)] for _ in range(3)]
    jugadores = ["X", "O"]
    random.shuffle(jugadores)
    print(f"\n¡Nueva partida! El jugador 1 es '{jugadores[0]}' y la computadora es '{jugadores[1]}'\n")
    mostrar_tablero(tablero)
    turno = 0
    while True:
        if turno % 2 == 0:
            fila = int(input("\nJugador 1 (X), ingresa el número de fila (1-3): ")) - 1
            columna = int(input("Jugador 1 (X), ingresa el número de columna (1-3): ")) - 1
        else:
            fila, columna = movimiento_computadora(tablero)
            print(f"\nLa computadora (O) ha movido a la fila {fila + 1}, columna {columna + 1}")
        if tablero[fila][columna] == " ":
            tablero[fila][columna] = jugadores[turno % 2]
            mostrar_tablero(tablero)
            if verificar_ganador(tablero, jugadores[turno % 2]):
                print(f"\n¡El jugador {jugadores[turno % 2]} ha ganado!")
                break
            elif verificar_empate(tablero):
                print("\n¡Empate!")
                break
            turno += 1
        else:
            print("\n¡Esa casilla ya está ocupada! Inténtalo de nuevo.")

def movimiento_computadora(tablero):
    movimientos_disponibles = []
    for fila in range(3):
        for columna in range(3):
            if tablero[fila][columna] == " ":
                movimientos_disponibles.append((fila, columna))
    return random.choice(movimientos_disponibles)

def verificar_ganador(tablero, jugador):
    for i in range(3):
        if tablero[i][0] == tablero[i][1] == tablero[i][2] == jugador or \
           tablero[0][i] == tablero[1][i] == tablero[2][i] == jugador:
            return True
    if tablero[0][0] == tablero[1][1] == tablero[2][2] == jugador or \
       tablero[0][2] == tablero[1][1] == tablero[2][0] == jugador:
        return True
    return False

def verificar_empate(tablero):
    for fila in tablero:
        if " " in fila:
            return False
    return True

def versus():
    tablero = [[" " for _ in range(3)] for _ in range(3)]
    print("\n¡Modo versus activado!")
    mostrar_tablero(tablero)
    turno = 0
    while True:
        if turno % 2 == 0:
            jugador = "X"
        else:
            jugador = "O"
        fila = int(input(f"\nJugador {jugador}, ingresa el número de fila (1-3): ")) - 1
        columna = int(input(f"Jugador {jugador}, ingresa el número de columna (1-3): ")) - 1
        if tablero[fila][columna] == " ":
            tablero[fila][columna] = jugador
            mostrar_tablero(tablero)
            if verificar_ganador(tablero, jugador):
                print(f"\n¡El jugador {jugador} ha ganado!")
                break
            elif verificar_empate(tablero):
                print("\n¡Empate!")
                break
            turno += 1
        else:
            print("\n¡Esa casilla ya está ocupada! Inténtalo de nuevo.")

def menu():
    print("¡Bienvenido al juego de GATO!")
    while True:
        print("\nMenú:")
        print("1. Nueva partida (Player 1 VS COM)")
        print("2. Versus (P1 VS P2)")
        print("3. Salir")
        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            nueva_partida()
        elif opcion == "2":
            versus()
        elif opcion == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    menu()
