#Ejemplo de ruleta funcional

import pygame
import math
import random
import sys

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ruleta")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
colors = [
    (255, 200, 200), (200, 255, 200), (200, 200, 255),
    (255, 255, 200), (200, 255, 255), (255, 200, 255)
]

# Configuración de la ruleta
names = ["Dog 🐶", "Cat 🐱", "Bear 🐻", "Unicorn 🦄", "Lion 🦁", "Cow 🐮", "Pig 🐷", "Hamster 🐹", "Penguin 🐧"]
counters = [0] * len(names)
angle = 0  # Ángulo actual de la ruleta
animating = False  # Estado de animación
FPS = 60
clock = pygame.time.Clock()


# Función para convertir coordenadas polares a cartesianas
def polar_to_cartesian(center, radius, angle_rad):
    x = center[0] + radius * math.cos(angle_rad)
    y = center[1] + radius * math.sin(angle_rad)
    return x, y


# Función para dibujar la ruleta manualmente
def draw_ruleta(angle):
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


# Función para animar el giro de la ruleta
def animate_spin(target_angle, duration, target_index):
    global angle, animating
    start_angle = angle
    step_count = int(duration * FPS)
    step_angle = (target_angle - start_angle) / step_count
    current_step = 0

    def step():
        nonlocal current_step
        if current_step >= step_count:
            return False
        global angle
        angle += step_angle
        draw_ruleta(angle)
        pygame.display.flip()
        clock.tick(FPS)
        current_step += 1
        return True

    while step():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    counters[target_index] += 1
    animating = False
    return target_index


# Función principal
def main():
    global animating, angle
    running = True
    while running:
        screen.fill(WHITE)
        draw_ruleta(angle)
        pygame.display.flip()
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and not animating:
                if event.key == pygame.K_SPACE:  # Girar la ruleta con la tecla Espacio
                    animating = True
                    total_spins = random.randint(2, 5)
                    duration = random.randint(5000, 7500) / 1000  # Duración en segundos
                    target_index = random.choices(
                        range(len(names)),
                        weights=[1 / (c + 1) for c in counters],
                        k=1
                    )[0]
                    target_angle = -2 * math.pi * total_spins - target_index * (2 * math.pi / len(names))
                    result = animate_spin(target_angle, duration, target_index)
                    print(f"¡Seleccionado: {names[result]}!")

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
