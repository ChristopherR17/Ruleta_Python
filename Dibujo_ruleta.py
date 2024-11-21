import math
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import sys
import utils
import random
import time

#Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (70, 130, 180)
BROWN = (139, 69, 19)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
GOLD = (212, 175, 55)

pygame.init()
clock = pygame.time.Clock()

# Definir la finestra
WIDTH = 1000
HEIGHT = 1000
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Ruleta')

# Números negros de la ruleta europea
black_nums = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 29, 31, 33, 35]

#General
nums = list(range(37))  
angle = 0    
counters = [0] * len(nums)
#Centro de la ruleta
center_x, center_y = WIDTH // 2, HEIGHT // 2  
CENTRO = (WIDTH // 2, HEIGHT // 2)
RADIO = 250

# Variables de animación
animating = False  # Estado de animación
start_angle = 0
target_angle = 0
animation_start_time = 0
animation_duration = 5  
FPS = 60 
spin_velocity = 0    
deceleration = 0.001    


# Bucle de l'aplicació
def main():
    is_looping = True

    while is_looping:
        is_looping = app_events()
        app_run()
        app_draw()

        clock.tick(60) # Limitar a 60 FPS

    # Fora del bucle, tancar l'aplicació
    pygame.quit()
    sys.exit()

# Gestionar events
def app_events():
    global animating, animation_start_time, start_angle, target_angle, spin_velocity

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Detectar si el clic está dentro del área del botón
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if (WIDTH // 2 - 75 <= mouse_x <= WIDTH // 2 + 75) and (HEIGHT - 100 <= mouse_y <= HEIGHT - 50):
                if not animating:
                    animating = True
                    animation_start_time = time.time()
                    spin_velocity = random.uniform(0.1, 0.3)  # Velocidad inicial entre 0.1 y 0.3 rad/s
                    total_spins = random.randint(2, 5)
                    slice_angle = 2 * math.pi / len(nums)
                    target_index = random.randint(0, len(nums) - 1)
                    target_angle = -2 * math.pi * total_spins - target_index * slice_angle - slice_angle / 2
                    counters[target_index] += 1


    return True

# Fer càlculs
def app_run():
    global angle, animating, spin_velocity, result_index, slice_angle

    if not animating:
        return
    
    if spin_velocity > 0:
        # Actualizar el ángulo según la velocidad angular
        angle += spin_velocity
        spin_velocity -= deceleration  # Reducir la velocidad gradualmente
    else:
        # Finalizar la animación cuando la velocidad llegue a cero
        animating = False
        
        #Resultado
        normalized_angle = -angle % (2 * math.pi) 
        slice_angle = 2 * math.pi / len(nums)
        adjusted_angle = normalized_angle + slice_angle / 2
        result_index = int(adjusted_angle // slice_angle) % len(nums)
        result_number = nums[result_index]

        # Mostrar el resultado en la terminal
        print(f"Resultado de la ruleta: {result_number}")

# Dibuixar
def app_draw():
    # Pintar el fons de blanc
    screen.fill(WHITE)
    
    # Dibuixar la graella(Despues se quita o se comenta)
    utils.draw_grid(pygame, screen, 50)

    # Dibujar la base de madera
    pygame.draw.circle(screen, BROWN, CENTRO, RADIO + 50)

    # Dibujar el borde dorado
    pygame.draw.circle(screen, GOLD, CENTRO, RADIO + 10)

    # Dibujar el círculo principal
    pygame.draw.circle(screen, BLACK, CENTRO, RADIO)
    pygame.draw.circle(screen, WHITE, CENTRO, RADIO, 5)


    # Centro de la ruleta
    radi = 200
    slice_angle = 2 * math.pi / len(nums)

    for i, num in enumerate(nums):
        # Calcular ángulos del segmento
        start_angle = angle + i * slice_angle
        end_angle = start_angle + slice_angle

        # Coordenadas de los puntos
        point1 = (center_x, center_y)
        point2 = polar_to_cartesian((center_x, center_y), radi, start_angle)
        point3 = polar_to_cartesian((center_x, center_y), radi, end_angle)

        # Dibujar triángulos de la ruleta y aplicarle color
        if num == 0:
            color = GREEN
            pygame.draw.polygon(screen, color, [point1, point2, point3])
        elif num in black_nums:
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
        text_x, text_y = polar_to_cartesian((center_x, center_y), radi * 0.7, mid_angle)

        # Renderizar texto
        font = pygame.font.SysFont(None, 24)
        text = f"{num}"
        text_surface = font.render(text, True, WHITE)
        text_rect = text_surface.get_rect(center=(text_x, text_y))
        screen.blit(text_surface, text_rect)

    # Dibujar indicador
    # Dibujar indicador a la derecha
    pygame.draw.polygon(screen, RED, [
        (center_x + radi + 10, center_y),
        (center_x + radi + 40, center_y - 20),
        (center_x + radi + 40, center_y + 20)
    ])


    #Circulo central de la ruleta
    pygame.draw.circle(screen, GOLD, point1, 30)
    #Anillo exterior
    pygame.draw.circle(screen, GOLD, point1, radi+2, 5)

    # Dibujar botón de giro
    pygame.draw.rect(screen, BLUE, (WIDTH // 2 - 75, HEIGHT - 100, 150, 50))
    font = pygame.font.SysFont(None, 36)
    text_surface = font.render("GIRAR", True, WHITE)
    text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT - 75))
    screen.blit(text_surface, text_rect)

    # Actualitzar el dibuix a la finestra
    pygame.display.update()

# Función para convertir coordenadas polares a cartesianas
def polar_to_cartesian(center, radius, angle_rad):
    x = center[0] + radius * math.cos(angle_rad)
    y = center[1] + radius * math.sin(angle_rad)
    return x, y

if __name__ == "__main__":
    main()