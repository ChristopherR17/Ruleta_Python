import math
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import sys
import random

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
YELLOW = (255, 255, 70)
BLACK2 = (50, 41, 41)
GREEN = (54, 157, 35)
RED = (237, 46, 46)
BLUE = (70, 130, 180)

pygame.init()
clock = pygame.time.Clock()

# Dimensiones de la ventana
WIDTH = 800
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Ruleta con Botón')

# Variables globales
nums = list(range(37))  # Números de la ruleta
angle = 0               # Ángulo actual de rotación
spin_speed = 0          # Velocidad angular de giro
spinning = False        # Si la ruleta está girando
target_angle = 0        # Ángulo objetivo donde se detendrá
button_rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT - 100, 200, 50)  # Posición y tamaño del botón

# Función principal
def main():
    global angle, spin_speed, spinning, target_angle
    is_looping = True

    while is_looping:
        is_looping = app_events()  # Gestionar eventos
        app_run()                  # Lógica de la ruleta
        app_draw()                 # Dibujar la ruleta y el botón

        clock.tick(60)             # Limitar a 60 FPS

    pygame.quit()
    sys.exit()

# Manejo de eventos
def app_events():
    global spinning, spin_speed, target_angle

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False  # Salir del programa
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if not spinning and button_rect.collidepoint(event.pos):  # Si el botón es presionado
                spinning = True
                spin_speed = random.uniform(0.1, 0.2)  # Velocidad inicial
                target_angle = random.randint(0, 36) * (2 * math.pi / len(nums))  # Casilla objetivo
    return True

# Lógica de la ruleta
def app_run():
    global angle, spin_speed, spinning, target_angle

    if spinning:
        spin_speed *= 0.99  # Desacelerar gradualmente
        angle += spin_speed  # Actualizar el ángulo

        # Calcula la diferencia entre el ángulo actual y el objetivo
        target_radians = target_angle % (2 * math.pi)
        angle_radians = angle % (2 * math.pi)
        diff = (target_radians - angle_radians) % (2 * math.pi)

        # Detener la ruleta cuando esté cerca del objetivo y con poca velocidad
        if spin_speed < 0.001 and abs(diff) < 0.01:
            angle = target_radians  # Ajustar el ángulo al objetivo
            spinning = False

# Dibujo de la ruleta y el botón
def app_draw():
    global angle
    screen.fill(WHITE)

    # Centro y radio de la ruleta
    center_x, center_y = WIDTH // 2, HEIGHT // 2
    radi = 300
    slice_angle = 2 * math.pi / len(nums)

    # Dibujar segmentos de la ruleta
    for i, num in enumerate(nums):
        start_angle = angle + i * slice_angle
        end_angle = start_angle + slice_angle

        point1 = (center_x, center_y)
        point2 = polar_to_cartesian((center_x, center_y), radi, start_angle)
        point3 = polar_to_cartesian((center_x, center_y), radi, end_angle)

        color = GREEN if num == 0 else (BLACK2 if num % 2 == 0 else RED)
        pygame.draw.polygon(screen, color, [point1, point2, point3])
        pygame.draw.line(screen, BLACK, point1, point2, 2)
        pygame.draw.line(screen, BLACK, point1, point3, 2)

        mid_angle = start_angle + slice_angle / 2
        text_x, text_y = polar_to_cartesian((center_x, center_y), radi * 0.7, mid_angle)
        font = pygame.font.SysFont(None, 24)
        text_surface = font.render(str(num), True, BLACK)
        text_rect = text_surface.get_rect(center=(text_x, text_y))
        screen.blit(text_surface, text_rect)

    # Dibujar flecha roja
    pygame.draw.polygon(screen, RED, [
        (center_x, center_y - radi - 10),
        (center_x + 20, center_y - radi - 40),
        (center_x - 20, center_y - radi - 40)
    ])
    pygame.draw.circle(screen, BLACK, (center_x, center_y), 30)

    # Dibujar botón
    pygame.draw.rect(screen, BLUE, button_rect)
    font = pygame.font.SysFont(None, 36)
    text_surface = font.render("GIRAR", True, WHITE)
    text_rect = text_surface.get_rect(center=button_rect.center)
    screen.blit(text_surface, text_rect)

    pygame.display.update()

# Conversión de coordenadas polares a cartesianas
def polar_to_cartesian(center, radius, angle_rad):
    x = center[0] + radius * math.cos(angle_rad)
    y = center[1] + radius * math.sin(angle_rad)
    return x, y

if __name__ == "__main__":
    main()
