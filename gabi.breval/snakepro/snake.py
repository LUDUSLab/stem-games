import pygame
import config

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3
my_direction = LEFT


# Snake ------------------------------------------------------------------------------------------------------- #
'''
Games and screens are represented by matrices
Every sequence is a tuple
'''

snake_head = pygame.image.load(config.address('snake_head_gabi.breval.png', 'skin'))
snake = [(200, 200), (220, 200), (240, 200)]  # every sequence is a tuple
snake_head_pos = (snake[0][0] - 20, snake[0][1])
snake_head = pygame.transform.scale(snake_head, [20, 20])
snake_skin = pygame.Surface((config.grid_size, config.grid_size))
snake_skin.fill((0, 255, 0))  # color

# Rotation  -------------------------------------------------------------------------------------------------- #
snake_copy = snake_head.copy()
snake_head_down = pygame.transform.rotate(snake_copy, 180)
snake_head_left = pygame.transform.rotate(snake_copy, 90)
snake_head_right = pygame.transform.rotate(snake_copy, 270)
snake_head_up = pygame.transform.rotate(snake_copy, 0)