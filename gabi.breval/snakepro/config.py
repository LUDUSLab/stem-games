import pygame
import random
import game
from snake import *

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


# Colors ------------------------------------------------------------------------------------------------------- #
light_grey = (200, 200, 200)
bg_color = pygame.Color('grey12')
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# score text --------------------------------------------------------------------------------------------------- #
font = address('gabi.brevalFont.otf', 'font')
score_font = pygame.font.Font(address('gabi.brevalFont.otf', 'font'), 35)
score_text = score_font.render(' 0', True, COLOR_WHITE, COLOR_BLACK)
score_text_rect = score_text.get_rect()
score_text_rect.center = (WIDTH / 2, 30)
score = 0

# Game over text ----------------------------------------------------------------------------------------------- #
lose_font = pygame.font.Font(address('gabi.brevalFont.otf', 'font'),
                             100)
lose_text = lose_font.render('Game over!', True, COLOR_WHITE, COLOR_BLACK)
lose_text_rect = score_text.get_rect()
lose_text_rect.center = (600, 350)
# -------------------------------------------------------------------------------------------------------------- #

# Sound ------------------------------------------------------------------------------------------------------ #
munch_sound_effect = pygame.mixer.Sound(address('gabi.breval.munch-sound.wav', 'sound'))
game_over_effect = pygame.mixer.Sound(address('batida_gabi.breval.wav', 'sound'))


# Grass -------------------------------------------------------------------------------------------------------- #
grass = pygame.image.load(address('gabi.breval.folha.png', 'skin'))

