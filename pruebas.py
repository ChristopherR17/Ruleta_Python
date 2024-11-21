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
        adjusted_angle = (normalized_angle + slice_angle / 2) % (2 * math.pi)
        result_index = (int(adjusted_angle // slice_angle) % len(nums)) % len(nums)
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



























#RULETA BONITA DE EJEMPLO#

#import pygame
#import math
#
## Inicializar Pygame
#pygame.init()
#
## Configuración de la pantalla
#ANCHO, ALTO = 800, 800
#pantalla = pygame.display.set_mode((ANCHO, ALTO))
#pygame.display.set_caption("Ruleta de Casino Decorada")
#
## Colores
#NEGRO = (0, 0, 0)
#BLANCO = (255, 255, 255)
#ROJO = (200, 0, 0)
#VERDE = (0, 200, 0)
#MADERA = (139, 69, 19)
#DORADO = (212, 175, 55)
#
## Números rojos y negros de la ruleta europea
#red_nums = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27,28, 30, 32, 34, 36]
#black_nums = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 29, 31, 33, 35]
#
## Configuración de la ruleta
#CENTRO = (ANCHO // 2, ALTO // 2)
#RADIO = 250
#SECTORES = 37  # Cantidad de sectores (0 al 36)
#SEPARADOR = 2  # Grosor de los separadores entre sectores
#
## Función para dibujar la ruleta
#def dibujar_ruleta():
#    # Dibujar la base de madera
#    pygame.draw.circle(pantalla, MADERA, CENTRO, RADIO + 50)
#
#    # Dibujar el borde dorado
#    pygame.draw.circle(pantalla, DORADO, CENTRO, RADIO + 10)
#
#    # Dibujar el círculo principal
#    pygame.draw.circle(pantalla, NEGRO, CENTRO, RADIO)
#    pygame.draw.circle(pantalla, BLANCO, CENTRO, RADIO, 5)
#
#    # Dibujar sectores
#    angulo_por_sector = 360 / SECTORES
#
#    for i in range(SECTORES):
#        # Calcular los ángulos inicial y final del sector
#        angulo_inicio = math.radians(i * angulo_por_sector)
#        angulo_final = math.radians((i + 1) * angulo_por_sector)
#
#        # Calcular el color del sector
#        if i == 0:
#            color = VERDE 
#        elif i in black_nums:
#            color = NEGRO
#        else:
#            color = ROJO
#
#        # Dibujar el sector como un polígono
#        x1 = CENTRO[0] + RADIO * math.cos(angulo_inicio)
#        y1 = CENTRO[1] - RADIO * math.sin(angulo_inicio)
#        x2 = CENTRO[0] + RADIO * math.cos(angulo_final)
#        y2 = CENTRO[1] - RADIO * math.sin(angulo_final)
#        pygame.draw.polygon(pantalla, color, [CENTRO, (x1, y1), (x2, y2)])
#        
#        # Dibujar separadores
#        pygame.draw.line(pantalla, BLANCO, (x1, y1), (x2, y2), SEPARADOR)
#
#        # Agregar texto del número
#        angulo_texto = math.radians((i + 0.5) * angulo_por_sector)
#        x_texto = CENTRO[0] + (RADIO - 40) * math.cos(angulo_texto)
#        y_texto = CENTRO[1] - (RADIO - 40) * math.sin(angulo_texto)
#
#        font = pygame.font.Font(None, 24)
#        texto = font.render(str(i), True, BLANCO)
#        texto_rect = texto.get_rect(center=(x_texto, y_texto))
#        pantalla.blit(texto, texto_rect)
#
#    # Dibujar círculo central dorado
#    pygame.draw.circle(pantalla, DORADO, CENTRO, 40)
#
#    # Dibujar el "marcador" (flecha) en la parte superior
#    pygame.draw.polygon(pantalla, ROJO, [
#        (CENTRO[0], CENTRO[1] - RADIO - 20),
#        (CENTRO[0] - 15, CENTRO[1] - RADIO - 50),
#        (CENTRO[0] + 15, CENTRO[1] - RADIO - 50)
#    ])
#    pygame.draw.line(pantalla, BLANCO, 
#                     (CENTRO[0], CENTRO[1] - RADIO), 
#                     (CENTRO[0], CENTRO[1] - RADIO - 50), 3)
#
## Loop principal
#corriendo = True
#while corriendo:
#    for evento in pygame.event.get():
#        if evento.type == pygame.QUIT:
#            corriendo = False
#
#    # Dibujar fondo
#    pantalla.fill(VERDE)
#
#    # Dibujar la ruleta
#    dibujar_ruleta()
#
#    # Actualizar pantalla
#    pygame.display.flip()
#
## Salir de Pygame
#pygame.quit()
