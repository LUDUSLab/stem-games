import pygame
import random
from pygame.locals import *
import config

# Apple ------------------------------------------------------------------------------------------------------ #
apple_1_score = pygame.image.load(config.address('gabi.breval.maca.png', 'skin'))
apple_1_score = pygame.transform.scale(apple_1_score, [20, 20])
apple_1_score_y = 10
apple_food = pygame.image.load(config.address('gabi.breval.maca.png', 'skin'))
apple_food = pygame.transform.scale(apple_food, [20, 20])
apple_food_pos = config.on_grid_random()