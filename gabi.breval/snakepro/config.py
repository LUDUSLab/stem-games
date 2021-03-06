import pygame
import random
import game
import snake

from pygame.locals import *


WIDTH = 800
HEIGHT = 600
grid_size = 20

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # width, height, we are matrices
pygame.display.set_caption('Snake')


def on_grid_random():
    x = random.randint(25, 575)
    y = random.randint(50, 530)
    return x // 10 * 10, y // 10 * 10


def address(name, genre):
    skins = "/home/gabibreval/Documentos/stem-games/gabi.breval/snakepro/assets/skins/"
    sounds = "/home/gabibreval/Documentos/stem-games/gabi.breval/snakepro/assets/sounds/"
    fonts = "/home/gabibreval/Documentos/stem-games/gabi.breval/snakepro/assets/fonts/"

    if genre == "skin":
        directory = skins + name
        return directory
    elif genre == "sound":
        directory = sounds + name
        return directory

    elif genre == "font":
        directory = fonts + name
        return directory

def after_collision():
    global score, apple_food_pos
    apple_food_pos = on_grid_random()  # when there´s a collision the apple changes its position
    game.munch_sound_effect.play()  # sound
    score += 1
    snake.append((0, 0))
    return apple_food_pos