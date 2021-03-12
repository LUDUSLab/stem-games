import pygame
from sys import exit

import config

import fruit

import snake

import wall

# create a game.py file and place the functions and variables related to the game as a whole

pygame.init()

#Tela
screen = pygame.display.set_mode(config.dimentions)
pygame.display.set_caption('Snake')
score_font = config.font_(size=20)


def pencil(text, color):
    message = score_font.render('%s' % text, True, color)
    return message


def write(text, color, surface, x, y):
    pen = pencil(text, color)
    surface.blit(pen, (x, y))


def game_loop():

    while True:
        screen.fill(config.royalblue)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake.direction_y != 1:
                    # turn image
                    if snake.direction_x >= 0 and snake.direction_y == 0:
                        snake.head = snake.turn_img(snake.head, 90)
                    elif snake.direction_x < 0 and snake.direction_y == 0:
                        snake.head = snake.turn_img(snake.head, -90)

                    snake.direction_x = 0
                    snake.direction_y = -1

                elif event.key == pygame.K_DOWN and snake.direction_y != -1:
                    #turn image
                    if snake.direction_x >= 0 and snake.direction_y == 0:
                        snake.head = snake.turn_img(snake.head, -90)
                    elif snake.direction_x < 0 and snake.direction_y == 0:
                        snake.head = snake.turn_img(snake.head, 90)

                    snake.direction_x = 0
                    snake.direction_y = 1

                elif event.key == pygame.K_LEFT and snake.direction_x != 1:
                    # turn image
                    if snake.direction_y >= 0 and snake.direction_x == 0:
                        snake.head = snake.turn_img(snake.head, -90)
                    elif snake.direction_y < 0 and snake.direction_x == 0:
                        snake.head = snake.turn_img(snake.head, 90)

                    snake.direction_x = -1
                    snake.direction_y = 0
                elif event.key == pygame.K_RIGHT and snake.direction_x != -1:
                    # turn image
                    if snake.direction_y >= 0 and snake.direction_x == 0:
                        snake.head = snake.turn_img(snake.head, 90)
                    elif snake.direction_y < 0 and snake.direction_x == 0:
                        snake.head = snake.turn_img(snake.head, -90)

                    snake.direction_x = 1
                    snake.direction_y = 0

        screen.blit(wall.grass, (wall.bg_x, wall.bg_y))
        screen.blit(wall.walls, (wall.bg_x, wall.bg_y))


        screen.blit(fruit.apple, fruit.apple_cord)
        screen.blit(snake.head, (snake.snake_pos[0]))

        snake.snake_pos[0][0] += snake.direction_x * config.block_size
        snake.snake_pos[0][1] += snake.direction_y * config.block_size

        if snake.head_pos[0] == fruit.apple_cord[0] and snake.head_pos[1] == fruit.apple_cord[1]:
            fruit.apple_cord = fruit.apple_pos(16, 784, 136, 584)

        pygame.display.flip()
        config.game_clock.tick(7)
