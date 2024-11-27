import pygame
import sys
import dibujos 
import evento_ruleta as e_ruleta
import jugadores as players  
import evento_fichas as e_fichas
import evento_estadisticas as e_stats

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

    fichas = dibujos.fichas
    dibujos.jugadores = players.jugadores 

    while running:
        running, animating, spin_velocity = e_ruleta.eventos(WIDTH, HEIGHT, animating, spin_velocity)
        angle, spin_velocity, animating = e_ruleta.calculos(dibujos.nums, angle, spin_velocity, animating)
        e_stats.evento()

        e_fichas.fichas = fichas
        e_fichas.manejar_arrastre_fichas()

        dibujos.animating = animating
        dibujos.resultado = e_ruleta.result_number
        dibujos.angle = angle
        dibujos.app_draw() 

        clock.tick(60)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
