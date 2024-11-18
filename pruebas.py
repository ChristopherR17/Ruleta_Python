import pygame
import math
import random
import sys
import time

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
WIDTH, HEIGHT = 1000, 1000
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ruleta")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (238, 191, 28)
BLUE = (70, 130, 180)
BLACK2 = (50, 41, 41)
colors = [
    (255, 200, 200), (200, 255, 200), (200, 200, 255),
    (255, 255, 200), (200, 255, 255), (255, 200, 255)
]

# Configuración de la ruleta
names = ["Dog 🐶", "Cat 🐱", "Bear 🐻", "Unicorn 🦄", "Lion 🦁", "Cow 🐮", "Pig 🐷", "Hamster 🐹", "Penguin 🐧"]
counters = [0] * len(names)

# Variables para la animación
angle = 0  # Ángulo actual de la ruleta
animating = False  # Estado de animación
start_angle = 0
target_angle = 0
spin_speed = 0
animation_start_time = 0
animation_duration = 5  # Duración de la animación en segundos
FPS = 60
clock = pygame.time.Clock()

# Función para convertir coordenadas polares a cartesianas
def polar_to_cartesian(center, radius, angle_rad):
    x = center[0] + radius * math.cos(angle_rad)
    y = center[1] + radius * math.sin(angle_rad)
    return x, y

# Dibujar la ruleta
def draw_ruleta():
    global angle
    screen.fill(WHITE)
    cx, cy = WIDTH // 2, HEIGHT // 2  # Centro de la ruleta
    radius = 300
    slice_angle = 2 * math.pi / len(names)

    for i, name in enumerate(names):
        # Calcular ángulos del segmento
        start_angle = angle + i * slice_angle
        end_angle = start_angle + slice_angle

        # Coordenadas de los puntos
        point1 = (cx, cy)
        point2 = polar_to_cartesian((cx, cy), radius, start_angle)
        point3 = polar_to_cartesian((cx, cy), radius, end_angle)

        # Dibujar segmento como triángulo
        color = colors[i % len(colors)]
        pygame.draw.polygon(screen, color, [point1, point2, point3])

        # Dibujar bordes
        pygame.draw.line(screen, BLACK, point1, point2, 2)
        pygame.draw.line(screen, BLACK, point1, point3, 2)

        # Calcular posición del texto
        mid_angle = start_angle + slice_angle / 2
        text_x, text_y = polar_to_cartesian((cx, cy), radius * 0.7, mid_angle)

        # Renderizar texto
        font = pygame.font.SysFont(None, 24)
        text = f"{name} ({counters[i]})"
        text_surface = font.render(text, True, BLACK)
        text_rect = text_surface.get_rect(center=(text_x, text_y))
        screen.blit(text_surface, text_rect)

    # Dibujar indicador
    pygame.draw.polygon(screen, RED, [
        (cx, cy - radius - 10),
        (cx + 20, cy - radius - 40),
        (cx - 20, cy - radius - 40)
    ])

    # Dibujar botón de girar
    pygame.draw.rect(screen, BLUE, (WIDTH // 2 - 75, HEIGHT - 100, 150, 50))
    font = pygame.font.SysFont(None, 36)
    text_surface = font.render("GIRAR", True, WHITE)
    text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT - 75))
    screen.blit(text_surface, text_rect)

# Animar el giro de la ruleta
def animate_spin():
    global angle, animating, animation_start_time, start_angle, target_angle

    if not animating:
        return

    elapsed_time = time.time() - animation_start_time
    if elapsed_time < animation_duration:
        # Interpolar el ángulo en función del tiempo de la animación
        angle = start_angle + (target_angle - start_angle) * (elapsed_time / animation_duration)
    else:
        # Finalizar la animación
        angle = target_angle
        animating = False

# Gestionar los eventos
def app_events():
    global animating, animation_start_time, start_angle, target_angle

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Detectar si el clic está dentro del área del botón
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if (WIDTH // 2 - 75 <= mouse_x <= WIDTH // 2 + 75) and (HEIGHT - 100 <= mouse_y <= HEIGHT - 50):
                if not animating:
                    # Iniciar la animación de giro
                    animating = True
                    animation_start_time = time.time()
                    start_angle = angle
                    total_spins = random.randint(2, 5)
                    target_index = random.randint(0, len(names) - 1)
                    target_angle = -2 * math.pi * total_spins - target_index * (2 * math.pi / len(names))
                    counters[target_index] += 1

    return True

# Función principal
def main():
    global animating

    running = True
    while running:
        # Gestionar eventos
        running = app_events()

        # Actualizar el estado de la animación
        animate_spin()

        # Dibujar la ruleta
        draw_ruleta()

        # Actualizar pantalla
        pygame.display.flip()

        # Limitar a 60 FPS
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
