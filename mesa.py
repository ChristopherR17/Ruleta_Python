import pygame

# Colores básicos
GREEN = (0, 128, 0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
BLUE = (0, 0, 255)

# Dimensiones
SCREEN_WIDTH = 1100
SCREEN_HEIGHT = 600
CELL_WIDTH = 60
CELL_HEIGHT = 60
MARGIN = 10  # Espaciado entre elementos

# Inicializa Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Mesa de la Ruleta")

# Fuente para los números
font = pygame.font.SysFont("Arial", 20)

# Dibujar un texto centrado en un rectángulo
def draw_text_centered(text, rect, color, surface):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(rect.x + rect.width / 2, rect.y + rect.height / 2))
    surface.blit(text_surface, text_rect)

# Secuencia de números en la ruleta (con colores)
def get_color(number):
    if number == 0:
        return GREEN
    elif number % 2 == 0:
        return BLACK
    else:
        return RED

def draw_table_horizontal(surface):
    surface.fill(GRAY)  # Fondo gris para destacar la mesa

    # Zona de números horizontales
    start_x = 50
    start_y = 100

    for row in range(3):  # 3 filas
        for col in range(12):  # 12 columnas
            number = (2 - row) + col * 3 + 1
            if number > 36:
                break  # Evitar dibujar números mayores a 36
            rect = pygame.Rect(start_x + col * CELL_WIDTH, start_y + row * CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT)
            color = get_color(number)
            pygame.draw.rect(surface, color, rect)  # Fondo del color correspondiente
            pygame.draw.rect(surface, WHITE, rect, width=2)  # Bordes blancos
            draw_text_centered(str(number), rect, WHITE, surface if color != WHITE else BLACK)

    # Casilla del número 0
    zero_rect = pygame.Rect(start_x - CELL_WIDTH - MARGIN, start_y, CELL_WIDTH, CELL_HEIGHT * 3)
    pygame.draw.rect(surface, GREEN, zero_rect)
    pygame.draw.rect(surface, WHITE, zero_rect, width=2)
    draw_text_centered("0", zero_rect, WHITE, surface)

    # Zonas de apuestas adicionales
    apuesta_y = start_y + CELL_HEIGHT * 3 + MARGIN * 2
    apuestas = [("Rojo", RED), ("Negro", BLACK), ("Par", WHITE), ("Impar", WHITE)]
    for i, (label, color) in enumerate(apuestas):
        rect = pygame.Rect(start_x + i * (CELL_WIDTH * 3 + MARGIN), apuesta_y, CELL_WIDTH * 3, CELL_HEIGHT)
        pygame.draw.rect(surface, color, rect)
        pygame.draw.rect(surface, WHITE, rect, width=2)
        draw_text_centered(label, rect, BLUE, surface)

    # Zonas de columnas
    columnas_y = start_y + CELL_HEIGHT * 3 + CELL_HEIGHT + MARGIN * 3
    for i in range(3):
        rect = pygame.Rect(start_x + i * CELL_WIDTH * 4, columnas_y, CELL_WIDTH * 4, CELL_HEIGHT)
        pygame.draw.rect(surface, GRAY, rect)
        pygame.draw.rect(surface, WHITE, rect, width=2)
        draw_text_centered(f"Col{i+1}", rect, BLACK, surface)

    # Zona de banca
    banca_rect = pygame.Rect(SCREEN_WIDTH - 120, start_y - 40, 100, 50)
    pygame.draw.rect(surface, WHITE, banca_rect, width=2)
    draw_text_centered("Banca", banca_rect, WHITE, surface)

# Bucle principal de Pygame
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    draw_table_horizontal(screen)
    pygame.display.flip()

pygame.quit()
