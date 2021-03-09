from fruit import *
from config import *
from snakebody import *
from game import *
from wall import wall_draw
import pygame

pygame.init()

snake_direction = 0

while game_loop:
    game_clock.tick(15)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake_direction = LEFT

            if event.key == pygame.K_UP:
                snake_direction = UP

            if event.key == pygame.K_RIGHT:
                snake_direction = RIGHT

            if event.key == pygame.K_DOWN:
                snake_direction = DOWN

    snake_move(snake_direction)

    screen.fill(color_black)

    wall_draw()
    snake_draw()
    fruit_draw()

    scoring(snake_position[0], fruit_pos)

    pygame.display.update()
