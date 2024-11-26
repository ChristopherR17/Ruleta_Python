import pygame
import math
import random

mouse_x, mouse_y = pygame.mouse.get_pos()
mouse_pos = (mouse_x, mouse_y)

mouse_x, mouse_y = pygame.mouse.get_pos()
mouse_pos = (mouse_x, mouse_y)

#Global
animating = False
angle = 0    
spin_velocity = 0   
deceleration = 0.001    

start_angle = 0
target_angle = 0
animation_start_time = 0
spin_velocity = 0  

#Calculos
#RULETA
def r_ruleta(nums, angle, spin_velocity, animating):
    if not animating:
        return angle, spin_velocity, animating
    
    if spin_velocity > 0:
        angle += spin_velocity
        spin_velocity -= deceleration
    else:
        animating = False

        normalized_angle = -angle % (2 * math.pi) 
        slice_angle = 2 * math.pi / len(nums)
        result_index = int(normalized_angle // slice_angle)
        result_number = nums[result_index]
        print(f"Resultado de la ruleta: {result_number}")
    
    return angle, spin_velocity, animating

<<<<<<< HEAD
=======
#FICHAS
def r_fichas(WIDTH, HEIGHT, jugadores, fichas):
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

>>>>>>> parent of ae1f809 (Revert ".")
#Eventos
#RULETA
def e_ruleta(WIDTH, HEIGHT, animating, spin_velocity):
    button_x = WIDTH // 7 + 175 + 70
    button_y = HEIGHT // 4 - 25

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False, animating, spin_velocity
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if (button_x <= mouse_x <=  button_x + 150) and (button_y <= mouse_y <= button_y + 50):
                if not animating:
                    animating = True
                    spin_velocity = random.uniform(0.15, 0.2)
    return True, animating, spin_velocity
<<<<<<< HEAD
=======

#FICHAS
def e_fichas(fichas):
    global ficha_seleccionada

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:  # Detectar clic inicial
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
>>>>>>> parent of ae1f809 (Revert ".")
