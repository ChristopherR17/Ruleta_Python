#import pygame
#import math
#import sys
#
## Inicializamos Pygame
#pygame.init()
#
## Configuración inicial
#dimensions = (800, 600)
#screen = pygame.display.set_mode(dimensions)
#pygame.display.set_caption("Distribució de Fitxes")
#
## Colores
#TARONJA = (255, 165, 0)
#LILA = (128, 0, 128)
#BLAU = (0, 0, 255)
#BLANC = (255, 255, 255)
#NEGRE = (0, 0, 0)
#ROIG = (200, 0, 0)
#
## Fonts
#font = pygame.font.Font(None, 36)
#
## Jugadors inicials
#players = {
#    "Taronja": {"color": TARONJA, "saldo": 100, "fitxes": {100: 0, 50: 1, 20: 1, 10: 2, 5: 2}},
#    "Lila": {"color": LILA, "saldo": 100, "fitxes": {100: 0, 50: 1, 20: 1, 10: 2, 5: 2}},
#    "Blau": {"color": BLAU, "saldo": 100, "fitxes": {100: 0, 50: 1, 20: 1, 10: 2, 5: 2}},
#}
#
## Funció per distribuir les fitxes
#def redistribuir_fitxes(player):
#    saldo = player["saldo"]
#    denominacions = sorted(player["fitxes"].keys(), reverse=True)
#    distribucio = {den: 0 for den in denominacions}
#
#    for den in denominacions:
#        distribucio[den] = saldo // den
#        saldo %= den
#
#    player["fitxes"] = distribucio
#    player["saldo"] = sum(den * quantitat for den, quantitat in distribucio.items())
#
## Funció per dibuixar una fitxa de póker
#def dibuixar_fitxa(x, y, color, denominacio):
#    # Círculo exterior
#    pygame.draw.circle(screen, NEGRE, (x, y), 30)  # Borde negro
#    pygame.draw.circle(screen, color, (x, y), 28)  # Color principal
#
#    # Decoración de borde
#    for i in range(12):
#        angle = i * 30
#        rad = math.radians(angle)
#        dx = int(24 * math.cos(rad))
#        dy = int(24 * math.sin(rad))
#        pygame.draw.circle(screen, BLANC, (x + dx, y + dy), 4)
#
#    # Círculo interior
#    pygame.draw.circle(screen, BLANC, (x, y), 18)
#
#    # Número de denominación
#    den_text = font.render(str(denominacio), True, color)
#    screen.blit(den_text, (x - den_text.get_width() // 2, y - den_text.get_height() // 2))
#
## Funció per dibuixar les fitxes
#def dibuixar_fitxes():
#    screen.fill(BLANC)
#
#    y_offset = 50
#    for idx, (nom, data) in enumerate(players.items()):
#        color = data["color"]
#        saldo = data["saldo"]
#        fitxes = data["fitxes"]
#
#        # Dibuixa el nom del jugador
#        text = font.render(f"{nom} - Crèdit: {saldo}", True, NEGRE)
#        screen.blit(text, (50, y_offset))
#        y_offset += 40
#
#        # Dibuixa les fitxes
#        x_offset = 150
#        for den, quantitat in fitxes.items():
#            for _ in range(quantitat):
#                dibuixar_fitxa(x_offset, y_offset, color, den)
#                x_offset += 80
#
#        y_offset += 100  # Espai entre jugadors
#
## Redistribuir les fitxes per cada jugador
#for jugador in players.values():
#    redistribuir_fitxes(jugador)
#
## Loop principal
#running = True
#while running:
#    for event in pygame.event.get():
#        if event.type == pygame.QUIT:
#            running = False
#
#    # Dibuixa l'estat actual de les fitxes
#    dibuixar_fitxes()
#
#    # Actualitza la pantalla
#    pygame.display.flip()
#
## Sortim de Pygame
#pygame.quit()
#sys.exit()


#sujeto a cambios
# Diccionario global para almacenar la información de los jugadores
jugadores = {
    "taronja": {"saldo": 100, "fichas": {5: 2, 10: 2, 20: 1, 50: 1, 100: 0}},
    "lila": {"saldo": 100, "fichas": {5: 2, 10: 2, 20: 1, 50: 1, 100: 0}},
    "blau": {"saldo": 100, "fichas": {5: 2, 10: 2, 20: 1, 50: 1, 100: 0}},
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
