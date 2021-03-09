import config
import pygame


# Apple ------------------------------------------------------------------------------------------------------ #
apple_1_score = pygame.image.load(config.address('gabi.breval.maca.png', 'skin'))
apple_1_score = pygame.transform.scale(apple_1_score, [32, 32])
apple_1_score_y = 10
apple_food = pygame.image.load(config.address('gabi.breval.maca.png', 'skin'))
apple_food = pygame.transform.scale(apple_food, [config.grid_size, config.grid_size])
apple_food_pos = config.on_grid_random()

'''
apple_1_score
apple_food
apple_1_score_y
apple_food_pos


'''