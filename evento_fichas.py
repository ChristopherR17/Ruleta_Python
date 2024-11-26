import pygame
import math

# Variable para rastrear el estado de arrastre
dragging = False
dragged_chip = None
offset_x, offset_y = 0, 0
fichas = []

def manejar_arrastre_fichas():
    global dragging, dragged_chip, offset_x, offset_y, fichas
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            # Verificar si el ratón está sobre alguna ficha
            for ficha in fichas:
                distance = math.sqrt((mouse_x - (ficha['x'] + 300)) ** 2 + (mouse_y - (ficha['y'] + 120)) ** 2)
                if distance <= ficha['radius']:  # Si está dentro del radio de la ficha
                    dragging = True
                    dragged_chip = ficha
                    offset_x = ficha['x'] - mouse_x
                    offset_y = ficha['y'] - mouse_y
                    break  # Solo arrastramos una ficha a la vez
        elif event.type == pygame.MOUSEMOTION:
            # Si estamos arrastrando una ficha, actualizar su posición
            if dragging and dragged_chip:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                dragged_chip['x'] = mouse_x + offset_x
                dragged_chip['y'] = mouse_y + offset_y
        elif event.type == pygame.MOUSEBUTTONUP:
            # Dejar de arrastrar cuando se suelta el botón del ratón
            dragging = False
            dragged_chip = None
    return True
"""
#FICHAS
def calculos(WIDTH, HEIGHT, jugadores, fichas):
    x_offset_start = WIDTH - 400
    y_offset = HEIGHT - 200

    for nom, data in jugadores.items():
        color = data["color"]
        fitxes = data["fitxes"]
        x_fichas_start = x_offset_start
        y_fichas = y_offset

        for den, cantidad in sorted(fitxes.items()):
            x_fichas = x_fichas_start
            for _ in range(cantidad):
                fichas.append({'x': x_fichas + 300, 'y': y_fichas + 120, 'denominacion': den, 'color': color})
                x_fichas -= 40
            y_fichas -= 50

        x_offset_start -= 400

#FICHAS
def eventos(fichas):
    global ficha_seleccionada

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:  # Detectar clic inicial
            mouse_pos = pygame.mouse.get_pos()
            for ficha in reversed(fichas):  # Revisar fichas en orden inverso para priorizar las superiores
                distancia = math.sqrt((ficha['x'] - mouse_pos[0])**2 + (ficha['y'] - mouse_pos[1])**2)
                if distancia < 25:  # Si el clic está dentro del radio de la ficha
                    ficha_seleccionada = ficha
                    break
                elif event.type == pygame.MOUSEMOTION:  # Detectar movimiento del ratón
                    if ficha_seleccionada:
                        ficha_seleccionada['x'], ficha_seleccionada['y'] = mouse_pos
                elif event.type == pygame.MOUSEBUTTONUP:  # Soltar la ficha
                    ficha_seleccionada = None
"""
"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Verificar si el ratón está sobre la ficha
            mouse_x, mouse_y = pygame.mouse.get_pos()
            distance = math.sqrt((mouse_x - (x + 300)) ** 2 + (mouse_y - (y + 120)) ** 2)
            if distance <= 25:  # Si está dentro del radio de la ficha
                dragging = True
                offset_x = x - mouse_x
                offset_y = y - mouse_y
        elif event.type == pygame.MOUSEMOTION:
            # Si estamos arrastrando la ficha, actualizar su posición
            if dragging:
                x = event.pos[0] + offset_x
                y = event.pos[1] + offset_y
        elif event.type == pygame.MOUSEBUTTONUP:
            # Dejar de arrastrar cuando se suelta el botón del ratón
            dragging = False
"""