#Aqui estoy pensando en poner los eventos para que cuando se pulse un boton que ponga 'stats' se muestre el archivo stats.py.
import pygame

def evento():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            button_width = 150
            button_height = 50
            button_x = 200
            button_y = 750
            if (button_x <= mouse_x <= button_x + button_width) and (button_y <= mouse_y <= button_y + button_height):
                abrir_stats()  
    return True

def abrir_stats():
    import stats  
    stats.main()  

