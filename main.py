import pygame
import sys
import dibujos
import run_and_events

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

    while running:
        # Procesar eventos
        running, animating, spin_velocity = run_and_events.e_ruleta(WIDTH, HEIGHT, dibujos.nums, animating, spin_velocity)
        
        # Actualizar estado de la ruleta
        angle, spin_velocity, animating = run_and_events.r_ruleta(dibujos.nums, angle, spin_velocity, animating)

        # Dibujar la ruleta y la mesa con el ángulo actualizado
        dibujos.angle = angle  # Asegúrate de que `dibujos` use este ángulo
        dibujos.app_draw()

        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
