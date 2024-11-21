import pygame
import sys

# Configuración inicial de las estadísticas
def inicializar_estadisticas():
    return {
        "tiradas": [],
        "scroll_offset": 0,
        "font": pygame.font.Font(None, 24),
        "width": 800,
        "height": 600,
        "row_height": 30,
        "column_widths": [100, 300, 350]  # Anchos de columnas: Resultado, Créditos, Apuestas
    }

def agregar_tirada(estadisticas, resultado, creditos_jugadores, apuestas_jugadores):
    tirada = {
        "resultado": resultado,
        "creditos": creditos_jugadores,
        "apuestas": apuestas_jugadores,
    }
    estadisticas["tiradas"].append(tirada)

def mostrar_estadisticas(estadisticas, pantalla):
    pantalla.fill((30, 30, 30))  # Fondo gris oscuro

    # Dibujar encabezados
    encabezados = ["Resultado", "Créditos", "Apuestas"]
    x_pos = 20
    for idx, titulo in enumerate(encabezados):
        texto = estadisticas["font"].render(titulo, True, (255, 255, 255))
        pantalla.blit(texto, (x_pos, 20))
        x_pos += estadisticas["column_widths"][idx]

    # Dibujar filas de estadísticas
    for i, tirada in enumerate(estadisticas["tiradas"]):
        y = 50 + i * estadisticas["row_height"] - estadisticas["scroll_offset"]
        if y < 50 or y > estadisticas["height"] - 50:
            continue  # No dibujar filas fuera de la pantalla

        x_pos = 20

        # Columna 1: Resultado
        resultado_texto = estadisticas["font"].render(str(tirada["resultado"]), True, (200, 200, 200))
        pantalla.blit(resultado_texto, (x_pos, y))
        x_pos += estadisticas["column_widths"][0]

        # Columna 2: Créditos (resumido)
        creditos_resumidos = ", ".join([f"{jugador}: {credito}" for jugador, credito in tirada["creditos"].items()])
        creditos_texto = estadisticas["font"].render(creditos_resumidos, True, (200, 200, 200))
        pantalla.blit(creditos_texto, (x_pos, y))
        x_pos += estadisticas["column_widths"][1]

        # Columna 3: Apuestas (resumido)
        apuestas_resumidas = ", ".join([f"{jugador}: {apuesta}" for jugador, apuesta in tirada["apuestas"].items()])
        apuestas_texto = estadisticas["font"].render(apuestas_resumidas, True, (200, 200, 200))
        pantalla.blit(apuestas_texto, (x_pos, y))

    # Dibujar la barra de scroll
    if len(estadisticas["tiradas"]) > 0:
        scrollbar_height = max(
            estadisticas["height"] * (estadisticas["height"] / (len(estadisticas["tiradas"]) * estadisticas["row_height"])),
            20,
        )
        scrollbar_y = (estadisticas["scroll_offset"] / max(len(estadisticas["tiradas"]) * estadisticas["row_height"] - estadisticas["height"], 1)) * (estadisticas["height"] - scrollbar_height)
        pygame.draw.rect(pantalla, (100, 100, 100), (estadisticas["width"] - 20, scrollbar_y, 10, scrollbar_height))

def manejar_eventos_estadisticas(estadisticas, evento):
    if evento.type == pygame.MOUSEBUTTONDOWN:
        if evento.button == 4:  # Scroll hacia arriba
            estadisticas["scroll_offset"] = max(estadisticas["scroll_offset"] - 30, 0)
        elif evento.button == 5:  # Scroll hacia abajo
            max_offset = max(len(estadisticas["tiradas"]) * estadisticas["row_height"] - estadisticas["height"], 0)
            estadisticas["scroll_offset"] = min(estadisticas["scroll_offset"] + 30, max_offset)

def reiniciar_estadisticas(estadisticas):
    estadisticas["tiradas"] = []
    estadisticas["scroll_offset"] = 0

# Programa principal
def main():
    pygame.init()

    # Configuración de la pantalla
    ancho, alto = 800, 600
    pantalla = pygame.display.set_mode((ancho, alto))
    pygame.display.set_caption("Estadísticas de la Ruleta")

    # Inicializar estadísticas
    estadisticas = inicializar_estadisticas()

    # Ejemplo: agregar tiradas ficticias
    for i in range(1, 29):
        resultado = i  # Resultado ficticio
        creditos = {"Taronja": 100 - i, "Lila": 90 + i, "Blau": 80 + i // 2}
        apuestas = {"Taronja": 10 + i, "Lila": 20 + i, "Blau": 30+ i}
        agregar_tirada(estadisticas, resultado, creditos, apuestas)

    # Bucle principal
    reloj = pygame.time.Clock()
    ejecutando = True
    while ejecutando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                ejecutando = False
            manejar_eventos_estadisticas(estadisticas, evento)

        # Dibujar las estadísticas
        mostrar_estadisticas(estadisticas, pantalla)

        # Actualizar pantalla
        pygame.display.flip()
        reloj.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
