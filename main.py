<<<<<<< Updated upstream
import dibujo_ruleta as ruleta

ruleta.main()
=======
import pygame
import dibujos
import sys

# Inicializar Pygame
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((dibujos.WIDTH, dibujos.HEIGHT))
pygame.display.set_caption("Ruleta Completa")

# Función principal
def main():
    running = True
    while running:
        # Manejar eventos (de la ruleta)
        running = app_events()
        app_run()

        dibujos.app_draw()  # Dibujar la ruleta
        clock.tick(60) # Limitar a 60 FPS

    # Fora del bucle, tancar l'aplicació
    pygame.quit()
    sys.exit()

    pygame.quit()

def app_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True

def app_run():
    pass

if __name__ == "__main__":
    main()
>>>>>>> Stashed changes
