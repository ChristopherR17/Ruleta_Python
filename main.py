import pygame
import sys
import dibujos 
import evento_ruleta as e_ruleta
import jugadores as players  

pygame.init()

clock = pygame.time.Clock()
WIDTH, HEIGHT = dibujos.WIDTH, dibujos.HEIGHT
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ruleta Completa")

def main():
    angle = 0
    spin_velocity = 0
    animating = False
    running = True

    dibujos.jugadores = players.jugadores 

    while running:
        running, animating, spin_velocity = e_ruleta.e_ruleta(WIDTH, HEIGHT, animating, spin_velocity)
        
        angle, spin_velocity, animating = e_ruleta.r_ruleta(dibujos.nums, angle, spin_velocity, animating)

        dibujos.angle = angle
        dibujos.app_draw() 

        clock.tick(60)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
