BLUE = (0, 0, 255)
ORANGE = (255,128,0)
PURPLE = (138, 43, 226)

jugadores = {
    "Taronja": {
        "color": ORANGE, 
        "saldo": 100,
        "fitxes": {
            100: 0,  
            50: 1, 
            20: 1, 
            10: 2,
            5: 2 
        }
    },
    "Lila": {
        "color": PURPLE, 
        "saldo": 100,
        "fitxes": {
            100: 0,  
            50: 1, 
            20: 1, 
            10: 2,
            5: 2 
        }
    },
    "Blau": {
        "color": BLUE,
        "saldo": 100,
        "fitxes": {
            100: 0,  
            50: 1, 
            20: 1, 
            10: 2,
            5: 2 
        }
    }
}

def actualizar_saldo(jugadores):
    for jugador, datos in jugadores.items():
        saldo_calculado = sum(valor * cantidad for valor, cantidad in datos["fitxes"].items())
        datos["saldo"] = saldo_calculado
