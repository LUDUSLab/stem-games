from config import *
import pygame

# Apple ------------------------------------------------------------------------------------------------------ #
apple_1_score = pygame.image.load(address('gabi.breval.maca.png', 'skin'))
apple_1_score = pygame.transform.scale(apple_1_score, [32, 32])
apple_1_score_y = 10
apple_food = pygame.image.load(address('gabi.breval.maca.png', 'skin'))
apple_food = pygame.transform.scale(apple_food, [grid_size, grid_size])
apple_food_pos = on_grid_random()
