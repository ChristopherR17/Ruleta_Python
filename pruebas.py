import pygame
import math

# Variable para rastrear el estado de arrastre
dragging = False
dragged_chip = None
offset_x, offset_y = 0, 0

def dibujar_fichas():
    global dragging, dragged_chip, offset_x, offset_y
    
    font2 = pygame.font.SysFont("Arial", 16)
    font3 = pygame.font.SysFont("Arial", 25)
    y_offset = HEIGHT - 200  
    x_offset_start = WIDTH - 400  

    # Lista de las fichas (coordenadas iniciales para cada ficha)
    fichas = []

    for nom, data in jugadores.items():
        color = data["color"]
        saldo = data["saldo"]
        fitxes = data["fitxes"]

        # Dibujar la caja para el jugador
        box_x = x_offset_start - 50
        box_y = y_offset - 100
        box_width = 395
        box_height = 245
        pygame.draw.rect(screen, (200, 200, 200), (box_x, box_y, box_width, box_height)) 
        pygame.draw.rect(screen, color, (box_x, box_y, box_width, box_height), 2)

        # Dibujar el nombre del jugador y el saldo
        text = font3.render(f"{nom} - Crèdit: {saldo}", True, BLACK)
        screen.blit(text, (box_x + 10, box_y + 10))

        # Dibujar la lista de fichas
        y_text = box_y + 50
        for den, cantidad in sorted(fitxes.items(), reverse=True):  
            ficha_texto = font3.render(f"Fichas de {den} x {cantidad}", True, BLACK)
            screen.blit(ficha_texto, (box_x + 10, y_text))
            y_text += 30

        # Dibujar las fichas en filas organizadas
        y_fichas = y_offset
        x_fichas_start = x_offset_start
        for den, cantidad in sorted(fitxes.items()): 
            x_fichas = x_fichas_start
            for i in range(cantidad):
                ficha = dibuixar_fitxa(screen, x_fichas, y_fichas, color, den, font2)
                fichas.append(ficha)  # Guardar información sobre la ficha
                x_fichas -= 0  
            y_fichas -= 50 

        x_offset_start -= 400  

    return fichas  # Devolvemos la lista de fichas

# Función para dibujar una ficha de póker y devolver sus coordenadas
def dibuixar_fitxa(screen, x, y, color, denominacio, font2):
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

    # Devolvemos las coordenadas de la ficha para su posterior uso en el arrastre
    return {'x': x, 'y': y, 'denominacio': denominacio, 'color': color, 'radius': 25}

# Función para manejar los eventos de arrastre de fichas
def manejar_arrastre_fichas(event, fichas):
    global dragging, dragged_chip, offset_x, offset_y
    
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

dibujar_fichas()
manejar_arrastre_fichas(event, fichas)

#Codigo de prueba para que la ficha se arrastre(LO HACE)
"""import pygame
import math

# Inicialización de Pygame
pygame.init()

# Colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Tamaño de la ventana
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Fuente para la denominación
font2 = pygame.font.Font(None, 36)

# Variables de posición inicial de la ficha
x, y = 100, 100  # Coordenadas iniciales
denominacion = 10  # Ejemplo de denominación de la ficha

# Variables de estado del arrastre
dragging = False
offset_x = 0
offset_y = 0

def dibuixar_fitxa(screen, x, y, color, denominacio, font2):
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

# Bucle principal
running = True
while running:
    screen.fill((0, 0, 0))  # Fondo de pantalla negro

    # Eventos
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

    # Dibujar la ficha
    dibuixar_fitxa(screen, x, y, RED, denominacion, font2)

    pygame.display.flip()  # Actualizar pantalla

# Salir de Pygame
pygame.quit()
"""
########## CODIGO DE RULETA FUNCIONAL(CON EVENTOS Y CALCULOS) ##########
"""
import math
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import sys
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

# Números rojos y negros de la ruleta europea
black_nums = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
red_numbers = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]

#General
nums = [0,1,2,3,4,5,6,7,8,9,10,12,11,14,13,16,15,18,17,19,20,21,22,23,24,25,26,27,28,30,29,32,31,34,33,36,35]
angle = 0    
counters = [0] * len(nums)
#Centro de la ruleta
center_x, center_y = WIDTH // 4, HEIGHT // 4  
CENTRO = (WIDTH // 4, HEIGHT // 4)
RADIO = 175

# Variables de animación
animating = False  # Estado de animación
start_angle = 0
target_angle = 0
animation_start_time = 0
animation_duration = 5  
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
                #Aqui es donde empieza la animacion de giro
                if not animating:
                    animating = True
                    animation_start_time = time.time()
                    spin_velocity = random.uniform(0.15, 0.2)
                    total_spins = random.randint(2, 5)
                    slice_angle = 2 * math.pi / len(nums)
                    target_index = random.randint(0, len(nums) - 1)
                    target_angle = -2 * math.pi * total_spins - target_index * slice_angle - slice_angle / 2
                    counters[target_index] += 1
    return True

# Fer càlculs
def app_run():
    global angle, animating, spin_velocity

    if not animating:
        return
    
    #La desaceleracion
    if spin_velocity > 0:
        angle += spin_velocity
        spin_velocity -= deceleration 

    else:
        animating = False
        
        #Resultado
        normalized_angle = -angle % (2 * math.pi)  # Normalizar a un rango de [0, 2π]
        slice_angle = 2 * math.pi / len(nums)
        result_index = int(normalized_angle // slice_angle)
        result_number = nums[result_index]

        # Mostrar el resultado en la terminal
        print(f"Resultado de la ruleta: {result_number}")


# Dibuixar
def app_draw():
    ############ RULETA ############
    # Pintar el fons de blanc
    screen.fill(WHITE)

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
        elif num in black_nums:
            color = BLACK
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

    # Actualitzar el dibuix a la finestra
    pygame.display.update()

# Función para convertir coordenadas polares a cartesianas
def polar_to_cartesian(center, radius, angle_rad):
    x = center[0] + radius * math.cos(angle_rad)
    y = center[1] + radius * math.sin(angle_rad)
    return x, y

if __name__ == "__main__":
    main()
"""

#OTRA RULETA#
"""
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

# Números rojos y negros de la ruleta europea
black_nums = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
red_numbers = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]

#General
nums = [0,1,2,3,4,5,6,7,8,9,10,12,11,14,13,16,15,18,17,19,20,21,22,23,24,25,26,27,28,30,29,32,31,34,33,36,35]
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
                #Aqui es donde empieza la animacion de giro
                if not animating:
                    animating = True
                    animation_start_time = time.time()
                    spin_velocity = random.uniform(0.15, 0.2)
                    total_spins = random.randint(2, 5)
                    slice_angle = 2 * math.pi / len(nums)
                    target_index = random.randint(0, len(nums) - 1)
                    target_angle = -2 * math.pi * total_spins - target_index * slice_angle - slice_angle / 2
                    counters[target_index] += 1
    return True

# Fer càlculs
def app_run():
    global angle, animating, spin_velocity

    if not animating:
        return
    
    #La desaceleracion
    if spin_velocity > 0:
        angle += spin_velocity
        spin_velocity -= deceleration 

    else:
        animating = False
        
        #Resultado
        normalized_angle = -angle % (2 * math.pi)  # Normalizar a un rango de [0, 2π]
        slice_angle = 2 * math.pi / len(nums)
        result_index = int(normalized_angle // slice_angle)
        result_number = nums[result_index]

        # Mostrar el resultado en la terminal
        print(f"Resultado de la ruleta: {result_number}")


# Dibuixar
def app_draw():
    # Pintar el fons de blanc
    screen.fill(WHITE)
    
    # Dibuixar la graella(Despues se quita o se comenta)
    #utils.draw_grid(pygame, screen, 50)

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

        # Renderizar numeros de la ruleta
        font = pygame.font.SysFont(None, 24)
        text = f"{num}"
        text_surface = font.render(text, True, WHITE)
        text_rect = text_surface.get_rect(center=(text_x, text_y))
        screen.blit(text_surface, text_rect)

    # Dibujar indicador
    pygame.draw.polygon(screen, RED, [
        (center_x + radi + 10, center_y),
        (center_x + radi + 40, center_y - 20),
        (center_x + radi + 40, center_y + 20)
    ])

    #Circulo central de la ruleta
    pygame.draw.circle(screen, GOLD, point1, 30)
    #Anillo exterior
    pygame.draw.circle(screen, GOLD, point1, radi+2, 5)

    #Boton de giro
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
"""

##### CODIGO MESA #####
"""
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

# Números rojos y negros de la ruleta europea
black_numbers = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
red_numbers =  [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]


# Función para obtener el color de un número
def get_color(number):
    if number == 0:
        return GREEN
    elif number in red_numbers:
        return RED
    elif number in black_numbers:
        return BLACK
    else:
        return WHITE  # En caso de un error (aunque no debería ocurrir)

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
            draw_text_centered(str(number), rect, WHITE if color != WHITE else BLACK, surface)


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
"""