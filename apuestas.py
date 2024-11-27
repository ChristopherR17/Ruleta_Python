# apuestas registrarlas comprobarlas y dar los resultados

def hacer_apuesta(jugador, tipo_apuesta, valor_apuesta, cantidad_apostada):
    
    if jugadores[jugador]["saldo"] < cantidad_apostada:
        return "No tienes saldo suficiente para esta apuesta."
    
    if cantidad_apostada % 5 != 0:  # Asegurarse de que las apuestas sean múltiplos de 5
        return "Las apuestas deben ser múltiplos de 5."
    
    # Verificar que el jugador tiene la ficha necesaria
    if cantidad_apostada in jugadores[jugador]["fitxes"] and jugadores[jugador]["fitxes"][cantidad_apostada] > 0:
        jugadores[jugador]["fitxes"][cantidad_apostada] -= 1  # Restar la ficha apostada
        jugadores[jugador]["saldo"] -= cantidad_apostada
        if "apuestas" not in jugadores[jugador]:
            jugadores[jugador]["apuestas"] = []
        jugadores[jugador]["apuestas"].append((tipo_apuesta, valor_apuesta, cantidad_apostada))
        return "Apuesta realizada correctamente."
    else:
        return "No tienes suficientes fichas de ese valor."


def calcular_premio(jugador, tipo_apuesta, valor_apuesta, cantidad_apostada, resultado):
    
    if tipo_apuesta == "numero":
        if valor_apuesta == resultado:
            return cantidad_apostada * 35  # Pago por número acertado
        else:
            return 0
    
    elif tipo_apuesta == "color":
        if colores[resultado] == valor_apuesta:
            return cantidad_apostada  # Pago por color acertado
        else:
            return 0
    
    elif tipo_apuesta == "par_impar":
        if (valor_apuesta == "par" and resultado % 2 == 0) or (valor_apuesta == "impar" and resultado % 2 != 0):
            return cantidad_apostada  # Pago por par o impar
        else:
            return 0
    
    elif tipo_apuesta == "columna":
        # Las columnas contienen los números 1-3, 4-6, 7-9, etc.
        if resultado in valor_apuesta:
            return cantidad_apostada * 2  # Pago por columna
        else:
            return 0
    
    return 0

def resolver_apuestas(resultado):
    
    resultados = {}

    for jugador in jugadores:
        total_ganado = 0
        for tipo_apuesta, valor_apuesta, cantidad_apostada in jugadores[jugador].get("apuestas", []):
            total_ganado += calcular_premio(jugador, tipo_apuesta, valor_apuesta, cantidad_apostada, resultado)
        
        jugadores[jugador]["saldo"] += total_ganado
        jugadores[jugador]["apuestas"] = []  # Limpiar apuestas del jugador
        resultados[jugador] = {
            "resultado_ruleta": resultado,
            "saldo_jugador": jugadores[jugador]["saldo"],
            "premio_obtenido": total_ganado
        }

    return resultados


def guardar_stats():
    pass

def end():
    pass