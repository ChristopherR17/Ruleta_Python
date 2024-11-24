import pygame
import math
import random
import time

#Global
animating = False
angle = 0    
spin_velocity = 0   
deceleration = 0.001    

start_angle = 0
target_angle = 0
animation_start_time = 0
spin_velocity = 0  

def r_ruleta(nums, angle, spin_velocity, animating):
    if not animating:
        return angle, spin_velocity, animating
    
    # La desaceleración
    if spin_velocity > 0:
        angle += spin_velocity
        spin_velocity -= deceleration
    else:
        animating = False
        # Resultado
        normalized_angle = -angle % (2 * math.pi)  # Normalizar a un rango de [0, 2π]
        slice_angle = 2 * math.pi / len(nums)
        result_index = int(normalized_angle // slice_angle)
        result_number = nums[result_index]
        print(f"Resultado de la ruleta: {result_number}")
    
    return angle, spin_velocity, animating



# Gestionar events
def e_ruleta(WIDTH, HEIGHT, nums, animating, spin_velocity):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False, animating, spin_velocity
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if (WIDTH // 7 + 175 + 70 <= mouse_x <=  WIDTH // 7 + 175 + 70 + 150) and (HEIGHT // 4 - 25 <= mouse_y <= HEIGHT // 4 - 25 + 50):
                if not animating:
                    animating = True
                    spin_velocity = random.uniform(0.15, 0.2)
    return True, animating, spin_velocity
