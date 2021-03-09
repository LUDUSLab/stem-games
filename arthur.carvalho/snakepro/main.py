from fruit import fruit_draw
from config import *
from snakebody import *
import pygame

pygame.init()

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

    snake_move()

    print(snake_direction)

    screen.fill(color_black)

    snake_draw()
    fruit_draw()

    pygame.display.update()
