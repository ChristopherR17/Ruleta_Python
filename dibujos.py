import math
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import sys
import random
import time

# Definir la finestra
WIDTH = 1800
HEIGHT = 950
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.init()
clock = pygame.time.Clock()

#Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BLUE = (70, 130, 180)
BROWN = (139, 69, 19)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
GOLD = (212, 175, 55)

#General
nums = [0,1,2,3,4,5,6,7,8,9,10,12,11,14,13,16,15,18,17,19,20,21,22,23,24,25,26,27,28,30,29,32,31,34,33,36,35]
angle = 0    
counters = [0] * len(nums)
center_x, center_y = WIDTH // 4, HEIGHT // 4  
CENTRO = (WIDTH // 4, HEIGHT // 4)
RADIO = 175

CELL_WIDTH = 60
CELL_HEIGHT = 60
MARGIN = 10  

# Números rojos y negros de la ruleta europea
black_numbers = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
red_numbers = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]

def app_draw():
    ############ RULETA ############
    # Pintar el fons de blanc
    screen.fill(GRAY)

    # Dibujar la base de madera
    pygame.draw.circle(screen, BROWN, CENTRO, RADIO + 50)

    # Dibujar el borde dorado
    pygame.draw.circle(screen, GOLD, CENTRO, RADIO + 10)

    # Dibujar el círculo principal
    pygame.draw.circle(screen, BLACK, CENTRO, RADIO)
    pygame.draw.circle(screen, WHITE, CENTRO, RADIO, 5)


    # Centro de la ruleta
    radi = 150
    slice_angle = 2 * math.pi / len(nums)

    for i, num in enumerate(nums):
        # Calcular ángulos del segmento
        start_angle = angle + i * slice_angle
        end_angle = start_angle + slice_angle

        # Coordenadas de los puntos
        point1 = (CENTRO)
        point2 = polar_to_cartesian(CENTRO, radi, start_angle)
        point3 = polar_to_cartesian(CENTRO, radi, end_angle)

        # Dibujar triángulos de la ruleta y aplicarle color
        if num == 0:
            color = GREEN
            pygame.draw.polygon(screen, color, [point1, point2, point3])
        elif num in black_numbers:
            color = BLACK
            pygame.draw.polygon(screen, color, [point1, point2, point3])
        else:
            color = RED
            pygame.draw.polygon(screen, color, [point1, point2, point3])

        # Dibujar bordes
        pygame.draw.line(screen, BLACK, point1, point2, 3)
        pygame.draw.line(screen, BLACK, point1, point3, 3)

        # Calcular posición del texto
        mid_angle = start_angle + slice_angle / 2
        text_x, text_y = polar_to_cartesian(CENTRO, radi * 0.7, mid_angle)

        # Renderizar numeros de la ruleta
        font = pygame.font.SysFont(None, 24)
        text = f"{num}"
        text_surface = font.render(text, True, WHITE)
        text_rect = text_surface.get_rect(center=(text_x, text_y))
        screen.blit(text_surface, text_rect)

    #Circulo central de la ruleta
    pygame.draw.circle(screen, GOLD, point1, 30)
    #Anillo exterior
    pygame.draw.circle(screen, GOLD, point1, radi+2, 5)

    # Dibujar indicador
    pygame.draw.polygon(screen, RED, [
        (center_x + radi - 15, center_y),
        (center_x + radi + 40, center_y - 15),
        (center_x + radi + 40, center_y + 15)
    ])
    #Contorno del indicador
    pygame.draw.polygon(screen, GOLD, [
        (center_x + radi - 15, center_y),
        (center_x + radi + 40, center_y - 15),
        (center_x + radi + 40, center_y + 15)
    ], 3)

    #Boton de giro
    pygame.draw.rect(screen, BLUE, (WIDTH // 2 - 75, HEIGHT - 100, 150, 50))
    font = pygame.font.SysFont(None, 36)
    text_surface = font.render("GIRAR", True, WHITE)
    text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT - 75))
    screen.blit(text_surface, text_rect)

    ############ MESA ############
    table_width = CELL_WIDTH * 12 + CELL_WIDTH + MARGIN * 3  
    start_x = WIDTH - table_width - 70  
    start_y = 100  

    # Fuente para los números
    font = pygame.font.SysFont("Arial", 20)

    # Dibujar un texto centrado en un rectángulo
    def draw_text_centered(text, rect, color, screen):
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(center=(rect.x + rect.width / 2, rect.y + rect.height / 2))
        screen.blit(text_surface, text_rect)

    def get_color(number):
        if number == 0:
            return GREEN
        elif number in red_numbers:
            return RED
        elif number in black_numbers:
            return BLACK

    # Dibujar números de la tabla
    for row in range(3):  # 3 filas
        for col in range(12):  # 12 columnas
            number = (2 - row) + col * 3 + 1
            if number > 36:
                break  # Evitar dibujar números mayores a 36
            rect = pygame.Rect(start_x + col * CELL_WIDTH, start_y + row * CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT)
            color = get_color(number)
            pygame.draw.rect(screen, color, rect)  # Fondo del color correspondiente
            pygame.draw.rect(screen, WHITE, rect, width=2)  # Bordes blancos
            draw_text_centered(str(number), rect, WHITE if color != WHITE else BLACK, screen)

    # Casilla del número 0
    zero_rect = pygame.Rect(start_x - CELL_WIDTH - MARGIN, start_y, CELL_WIDTH, CELL_HEIGHT * 3)
    pygame.draw.rect(screen, GREEN, zero_rect)
    pygame.draw.rect(screen, WHITE, zero_rect, width=2)
    draw_text_centered("0", zero_rect, WHITE, screen)

    # Zonas de apuestas adicionales
    apuesta_y = start_y + CELL_HEIGHT * 3 + MARGIN * 2
    apuestas = [("Rojo", RED), ("Negro", BLACK), ("Par", WHITE), ("Impar", WHITE)]
    for i, (label, color) in enumerate(apuestas):
        rect = pygame.Rect(start_x + i * (CELL_WIDTH * 3 + MARGIN), apuesta_y, CELL_WIDTH * 3, CELL_HEIGHT)
        pygame.draw.rect(screen, color, rect)
        pygame.draw.rect(screen, WHITE, rect, width=2)
        draw_text_centered(label, rect, BLUE, screen)

    # Zonas de columnas
    column_start_x = start_x + CELL_WIDTH * 12 + MARGIN * 2
    for i in range(3):
        rect = pygame.Rect(column_start_x, start_y + i * CELL_HEIGHT, CELL_WIDTH * 2, CELL_HEIGHT)
        pygame.draw.rect(screen, GRAY, rect)
        pygame.draw.rect(screen, WHITE, rect, width=2)
        draw_text_centered(f"Columna {i + 1}", rect, BLACK, screen)

    # Zona de banca
    banca_rect = pygame.Rect(WIDTH - 120, start_y - 70, 100, 50)
    pygame.draw.rect(screen, WHITE, banca_rect, width=2)
    draw_text_centered("Banca", banca_rect, WHITE, screen)

    pygame.display.update()

    # Función para convertir coordenadas polares a cartesianas
def polar_to_cartesian(center, radius, angle_rad):
    x = center[0] + radius * math.cos(angle_rad)
    y = center[1] + radius * math.sin(angle_rad)
    return x, y
