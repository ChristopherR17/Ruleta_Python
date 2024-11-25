BLUE = (0, 0, 255)
ORANGE = (255,128,0)
PURPLE = (138, 43, 226)

jugadores = {
    "Taronja": {
        "color": ORANGE, 
        "saldo": 100,
        "fitxes": {
            5: 2,  
            10: 2, 
            20: 1, 
            50: 1,
            100: 0 
        }
    },
    "Lila": {
        "color": PURPLE, 
        "saldo": 100,
        "fitxes": {
            5: 2,  
            10: 2, 
            20: 1, 
            50: 1,
            100: 0 
        }
    },
    "Blau": {
        "color": BLUE,
        "saldo": 100,
        "fitxes": {
            5: 2,  
            10: 2, 
            20: 1, 
            50: 1,
            100: 0 
        }
    }
}

def apostar(jugador, valor_ficha, cantidad, espacio_apuesta):
    """
    Realiza una apuesta con el jugador indicado. 
    Si el jugador tiene suficientes fichas, las resta y asigna la apuesta al espacio indicado.
    """
    if jugadores[jugador]["fichas"].get(valor_ficha, 0) >= cantidad:
        jugadores[jugador]["fichas"][valor_ficha] -= cantidad
        # Aquí puedes agregar el código para realizar la apuesta en el espacio
        return True
    else:
        return False

def actualizar_saldo(jugador, ganancia):
    """
    Actualiza el saldo del jugador después de cada tirada.
    """
    jugadores[jugador]["saldo"] += ganancia

def reorganizar_fichas(jugador):
    """
    Reorganiza las fichas del jugador en función de su saldo disponible.
    """
    saldo = jugadores[jugador]["saldo"]
    jugadores[jugador]["fichas"] = {5: saldo // 5, 10: saldo // 10, 20: saldo // 20, 50: saldo // 50, 100: saldo // 100}

def mostrar_fichas(jugador):
    """
    Muestra el estado actual de las fichas del jugador.
    """
    return jugadores[jugador]["fichas"]
