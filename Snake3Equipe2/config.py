import pygame
import window

pygame.init()

COLOR_BLACK = (0, 0, 0)
COLOR_LIGHT_GRAY = (200, 200, 200)


def font(size: int):
    path = "./assets/PressStart2P.ttf"
    return pygame.font.Font(path, size)


def display_msg(surface, fnt, message: str, color: tuple, pos: tuple):
    text = fnt.render(message, True, color)
    surface.blit(text, pos)


def display_img(surface, path: str, pos: tuple):
    image = pygame.image.load(path)
    surface.blit(image, pos)


def check_quit_event(event):
    if event.type == pygame.QUIT:
        pygame.quit()
        quit()


def exit_game():
    pygame.quit()
    quit()


window = window.Window()
