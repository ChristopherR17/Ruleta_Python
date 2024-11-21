import pygame
import math

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
ANCHO, ALTO = 800, 800
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Ruleta de Casino Decorada")

# Colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO = (200, 0, 0)
VERDE = (0, 200, 0)
MADERA = (139, 69, 19)
DORADO = (212, 175, 55)

# Números rojos y negros de la ruleta europea
red_nums = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27,28, 30, 32, 34, 36]
black_nums = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 29, 31, 33, 35]

# Configuración de la ruleta
CENTRO = (ANCHO // 2, ALTO // 2)
RADIO = 250
SECTORES = 37  # Cantidad de sectores (0 al 36)
SEPARADOR = 2  # Grosor de los separadores entre sectores

# Función para dibujar la ruleta
def dibujar_ruleta():
    # Dibujar la base de madera
    pygame.draw.circle(pantalla, MADERA, CENTRO, RADIO + 50)

    # Dibujar el borde dorado
    pygame.draw.circle(pantalla, DORADO, CENTRO, RADIO + 10)

    # Dibujar el círculo principal
    pygame.draw.circle(pantalla, NEGRO, CENTRO, RADIO)
    pygame.draw.circle(pantalla, BLANCO, CENTRO, RADIO, 5)

    # Dibujar sectores
    angulo_por_sector = 360 / SECTORES

    for i in range(SECTORES):
        # Calcular los ángulos inicial y final del sector
        angulo_inicio = math.radians(i * angulo_por_sector)
        angulo_final = math.radians((i + 1) * angulo_por_sector)

        # Calcular el color del sector
        if i == 0:
            color = VERDE 
        elif i in black_nums:
            color = NEGRO
        else:
            color = ROJO

        # Dibujar el sector como un polígono
        x1 = CENTRO[0] + RADIO * math.cos(angulo_inicio)
        y1 = CENTRO[1] - RADIO * math.sin(angulo_inicio)
        x2 = CENTRO[0] + RADIO * math.cos(angulo_final)
        y2 = CENTRO[1] - RADIO * math.sin(angulo_final)
        pygame.draw.polygon(pantalla, color, [CENTRO, (x1, y1), (x2, y2)])
        
        # Dibujar separadores
        pygame.draw.line(pantalla, BLANCO, (x1, y1), (x2, y2), SEPARADOR)

        # Agregar texto del número
        angulo_texto = math.radians((i + 0.5) * angulo_por_sector)
        x_texto = CENTRO[0] + (RADIO - 40) * math.cos(angulo_texto)
        y_texto = CENTRO[1] - (RADIO - 40) * math.sin(angulo_texto)

        font = pygame.font.Font(None, 24)
        texto = font.render(str(i), True, BLANCO)
        texto_rect = texto.get_rect(center=(x_texto, y_texto))
        pantalla.blit(texto, texto_rect)

    # Dibujar círculo central dorado
    pygame.draw.circle(pantalla, DORADO, CENTRO, 40)

    # Dibujar el "marcador" (flecha) en la parte superior
    pygame.draw.polygon(pantalla, ROJO, [
        (CENTRO[0], CENTRO[1] - RADIO - 20),
        (CENTRO[0] - 15, CENTRO[1] - RADIO - 50),
        (CENTRO[0] + 15, CENTRO[1] - RADIO - 50)
    ])
    pygame.draw.line(pantalla, BLANCO, 
                     (CENTRO[0], CENTRO[1] - RADIO), 
                     (CENTRO[0], CENTRO[1] - RADIO - 50), 3)

# Loop principal
corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    # Dibujar fondo
    pantalla.fill(VERDE)

    # Dibujar la ruleta
    dibujar_ruleta()

    # Actualizar pantalla
    pygame.display.flip()

# Salir de Pygame
pygame.quit()
