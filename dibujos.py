import math
import pygame
import utils

# Dimensiones de la ventana
WIDTH = 1800
HEIGHT = 950
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.init()

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BLUE = (70, 130, 180)
BROWN = (139, 69, 19)
GREEN = (0, 128, 0)(34, 139, 34)
RED = (200, 0, 0)
GOLD = (212, 175, 55)
V_TABLERO = (34, 139, 34)

#Variables globales
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 11, 14, 13, 16, 15, 18, 17, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 30, 29, 32, 31, 34, 33, 36, 35]
angle = 0
counters = [0] * len(nums)

#Posicion de la ruleta
CENTER_X, CENTER_Y = WIDTH // 7, HEIGHT // 4  
CENTRO = (CENTER_X, CENTER_Y)
RADIO = 175

#Tamaño de la mesa
CELL_WIDTH = 60
CELL_HEIGHT = 60
MARGIN = 10

# Números rojos y negros de la ruleta europea
black_numbers = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
red_numbers = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]

#Diccionario que recibe la informacion del archivo jugadores
jugadores = {}

#Lista para almacenar la posicion de cada ficha que se dibuja
fichas = []

#Resultat ruleta
#resultado = 0

def app_draw():
    screen.fill(V_TABLERO)

    utils.draw_grid(pygame, screen, 50)

    dibujar_ruleta()
    dibujar_mesa()
    dibujar_fichas()

    pygame.display.update()

############ RULETA ############
def dibujar_ruleta():
    # Dibujar la base de madera
    pygame.draw.circle(screen, BROWN, CENTRO, RADIO + 50)

    # Dibujar el borde dorado
    pygame.draw.circle(screen, GOLD, CENTRO, RADIO + 10)

    # Dibujar el círculo principal
    pygame.draw.circle(screen, BLACK, CENTRO, RADIO)
    pygame.draw.circle(screen, WHITE, CENTRO, RADIO, 5)

    # Dibujar los segmentos de la ruleta
    radi = 150
    slice_angle = 2 * math.pi / len(nums)

    for i, num in enumerate(nums):
        # Calcular ángulos del segmento
        start_angle = angle + i * slice_angle
        end_angle = start_angle + slice_angle

        # Coordenadas de los puntos
        point1 = CENTRO
        point2 = polar_to_cartesian(CENTRO, radi, start_angle)
        point3 = polar_to_cartesian(CENTRO, radi, end_angle)

        # Dibujar triángulos de la ruleta y aplicar color
        color = get_color(num)
        pygame.draw.polygon(screen, color, [point1, point2, point3])

        # Dibujar bordes
        pygame.draw.line(screen, BLACK, point1, point2, 3)
        pygame.draw.line(screen, BLACK, point1, point3, 3)

        # Calcular posición del texto
        mid_angle = start_angle + slice_angle / 2
        text_x, text_y = polar_to_cartesian(CENTRO, radi * 0.7, mid_angle)

        # Renderizar números de la ruleta
        font = pygame.font.SysFont(None, 20)
        text = f"{num}"
        text_surface = font.render(text, True, WHITE)
        text_rect = text_surface.get_rect(center=(text_x, text_y))
        screen.blit(text_surface, text_rect)

    #Circulo central de la ruleta
    pygame.draw.circle(screen, GOLD, point1, 30)
    #Anillo exterior
    pygame.draw.circle(screen, GOLD, point1, radi+2, 5)

    #Dibujar indicador
    pygame.draw.polygon(screen, RED, [
        (CENTER_X + radi - 15, CENTER_Y),
        (CENTER_X + radi + 40, CENTER_Y - 15),
        (CENTER_X + radi + 40, CENTER_Y + 15)
    ])
    #Contorno del indicador
    pygame.draw.polygon(screen, GOLD, [
        (CENTER_X + radi - 15, CENTER_Y),
        (CENTER_X + radi + 40, CENTER_Y - 15),
        (CENTER_X + radi + 40, CENTER_Y + 15)
    ], 3)

    #Boton de giro de la ruleta
    button_width = 150
    button_height = 50
    button_x = CENTER_X + RADIO + 70 
    button_y = CENTER_Y - button_height // 2
    pygame.draw.rect(screen, BLUE, (button_x, button_y, button_width, button_height))
    font = pygame.font.SysFont(None, 36)
    text_surface = font.render("GIRAR", True, WHITE)
    text_rect = text_surface.get_rect(center=(button_x + button_width // 2, button_y + button_height // 2))
    screen.blit(text_surface, text_rect)
"""
    font = pygame.font.SysFont(None, 20)
    text = font.render(resultado, True, (255, 255, 255))
    screen.blit(CENTER_X, CENTER_Y)
"""
def polar_to_cartesian(center, radius, angle_rad):
    x = center[0] + radius * math.cos(angle_rad)
    y = center[1] + radius * math.sin(angle_rad)
    return x, y

############ MESA ############
def dibujar_mesa():
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

    # Dibujar números de la tabla
    for row in range(3): 
        for col in range(12): 
            number = (2 - row) + col * 3 + 1
            if number > 36:
                break  
            rect = pygame.Rect(start_x + col * CELL_WIDTH, start_y + row * CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT)
            color = get_color(number)
            pygame.draw.rect(screen, color, rect)  
            pygame.draw.rect(screen, WHITE, rect, width=2)  
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
        draw_text_centered(f"Columna {3 - i}", rect, BLACK, screen)

    # Zona de banca
    banca_rect = pygame.Rect(WIDTH - 120, start_y - 70, 100, 50)
    pygame.draw.rect(screen, WHITE, banca_rect, width=2)
    draw_text_centered("Banca", banca_rect, WHITE, screen)

#Funcion para devolver el color segun el numero
def get_color(number):
    if number == 0:
        return GREEN
    elif number in red_numbers:
        return RED
    else:
        return BLACK

############ FICHAS ############
def dibujar_fichas():
    global fichas

    font2 = pygame.font.SysFont("Arial", 16)
    font3 = pygame.font.SysFont("Arial", 25)
    y_offset = HEIGHT - 200  
    x_offset_start = WIDTH - 400  

    for nom, data in jugadores.items():
        color = data["color"]
        saldo = data["saldo"]
        fitxes = data["fitxes"]

        box_x = x_offset_start - 50
        box_y = y_offset - 100
        box_width = 395
        box_height = 245
        pygame.draw.rect(screen, (200, 200, 200), (box_x, box_y, box_width, box_height)) 
        pygame.draw.rect(screen, color, (box_x, box_y, box_width, box_height), 2)

        text = font3.render(f"{nom} - Crèdit: {saldo}", True, BLACK)
        screen.blit(text, (box_x + 10, box_y + 10))

        y_text = box_y + 50
        for den, cantidad in sorted(fitxes.items(), reverse=True):  
            ficha_texto = font3.render(f"Fichas de {den} x {cantidad}", True, BLACK)
            screen.blit(ficha_texto, (box_x + 10, y_text))
            y_text += 30

        y_fichas = y_offset
        x_fichas_start = x_offset_start
        for den, cantidad in sorted(fitxes.items()): 
            x_fichas = x_fichas_start
            for _ in range(cantidad):
                ficha = dibuixar_fitxa(x_fichas, y_fichas, color, den, font2)
                fichas.append(ficha)
                x_fichas -= 0  
            y_fichas -= 50 

        x_offset_start -= 400  

def dibuixar_fitxa(x, y, color, denominacio, font2):
    
    Aug_x = 300
    Aug_y = 120

    # Círculo exterior
    pygame.draw.circle(screen, BLACK, (x + Aug_x, y + Aug_y), 25) 
    pygame.draw.circle(screen, color, (x + Aug_x, y + Aug_y), 23) 

    # Decoración de borde
    for i in range(12):
        angle = i * 30
        rad = math.radians(angle)
        dx = int(19 * math.cos(rad))
        dy = int(19 * math.sin(rad))
        pygame.draw.circle(screen, WHITE, (x + dx + Aug_x, y + dy + Aug_y), 3)

    # Círculo interior
    pygame.draw.circle(screen, WHITE, (x + Aug_x, y + Aug_y), 14)

    # Número de denominación
    den_text = font2.render(str(denominacio), True, color)
    screen.blit(den_text, (x - den_text.get_width() // 2 + Aug_x, y - den_text.get_height() // 2 + Aug_y))

############ ESTADISTICAS ############
def estadisticas():
    pass



