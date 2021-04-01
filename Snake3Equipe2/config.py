import pygame
import window

pygame.init()

COLOR_BLACK = (0, 0, 0)
COLOR_LIGHT_GRAY = (200, 200, 200)
menu_image = pygame.image.load('./assets/menu.png')
menu_sound = pygame.mixer.Sound('./assets/368068__furbyguy__rock-metal-guitar-riff-1.wav')
menu_sound.set_volume(0.1)
eat_sound = pygame.mixer.Sound('./assets/524607__clearwavsound__crunchy-bite.wav')
pygame.mixer.music.load('./assets/export_ofoct.com.mp3')
pygame.mixer.music.set_volume(0.2)

SQUARE_SIZE = 40


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
