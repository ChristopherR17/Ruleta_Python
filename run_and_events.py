import pygame
import math
import random

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

#Eventos
#RULETA
def e_ruleta(WIDTH, HEIGHT, animating, spin_velocity):
    button_x = WIDTH // 7 + 175 + 70
    button_y = HEIGHT // 4 - 25

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False, animating, spin_velocity
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if (button_x <= mouse_x <=  button_x + 150) and (button_y <= mouse_y <= button_y + 50):
                if not animating:
                    animating = True
                    spin_velocity = random.uniform(0.15, 0.2)
    return True, animating, spin_velocity
