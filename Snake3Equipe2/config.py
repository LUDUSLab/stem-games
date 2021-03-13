import pygame

pygame.init()

COLOR_BLACK = (0, 0, 0)
COLOR_LIGHT_GRAY = (200, 200, 200)
window_size = (1280, 720)
center = (window_size[0]//2, window_size[1]//2)
screen = pygame.display.set_mode(window_size)

pygame.display.set_caption("Snake 3: Mad Kobra")


def font(size:int):
    path = "./assets/PressStart2P.ttf"
    return pygame.font.Font(path, size)

def display_msg(surface, fnt, message:str, color:tuple, pos:tuple):
    text = fnt.render(message, True, color)
    surface.blit(text, pos)

def display_img(surface, path:str, pos:tuple):
    image = pygame.image.load(path)
    surface.blit(image, pos)

def set_obj_coordinates(obj, x, y):
    obj.x = x
    obj.y = y