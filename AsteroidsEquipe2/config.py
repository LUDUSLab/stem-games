import window
import pygame

pygame.font.init()

COLOR_BLACK = (0, 0, 0)
COLOR_LIGHT_GRAY = (154, 154, 154)

window = window.Window()

def font(size: int):
    path = "./assets/VectorBattle-e9XO.ttf"
    return pygame.font.Font(path, size)

def display_msg(surface: pygame.Surface, fnt: pygame.font, message: str, color: tuple, pos: tuple):
    text = fnt.render(message, True, color)
    surface.blit(text, pos)

def check_quit_event():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
