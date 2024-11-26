import pygame
import math

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

def eventos(fichas):
    global ficha_seleccionada

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:  # Detectar clic inicial
            mouse_x, mouse_y = pygame.mouse.get_pos()
            mouse_pos = (mouse_x, mouse_y)
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