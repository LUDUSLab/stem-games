import pygame
from fruit import *
from config import *
from game import *


snake = [(200, 200), (220, 200), (240, 200)]
snake_head = pygame.image.load('../snakepro/assets/ronald.boadana_snakehead-right.png')
snake_head = pygame.transform.scale(snake_head, [20, 20])
snake_head_pos = (snake[0][0] + 20, snake[0][1])
snake_body = pygame.image.load('../snakepro/assets/ronald.boadana_snake_body.png')
snake_body = pygame.transform.scale(snake_body, [20, 20])


def body_snake_move():
    global snake, snake_head, snake_head_pos, snake_body, apple_pos
    if direction == UP:
        snake_head_pos = (snake[0][0], snake[0][1] - 20)
        snake_head = pygame.image.load('../snakepro/assets/ronald.boadana_snakehead-up.png')
        screen.blit(snake_head, snake_head_pos)
        if snake_head_pos == apple_pos:
            score_points_apple()
        if snake_head_pos == grape_pos:
            score_points_grape()
        if snake_head_pos == strawberry_pos:
            score_points_strawberry()

    if direction == DOWN:
        snake_head_pos = (snake[0][0], snake[0][1] + 20)
        snake_head = pygame.image.load('../snakepro/assets/ronald.boadana_snakehead-down.png')
        screen.blit(snake_head, snake_head_pos)
        if snake_head_pos == apple_pos:
            score_points_apple()
        if snake_head_pos == grape_pos:
            score_points_grape()
        if snake_head_pos == strawberry_pos:
            score_points_strawberry()

    if direction == RIGHT:
        snake_head_pos = (snake[0][0] + 20, snake[0][1])
        snake_head = pygame.image.load('../snakepro/assets/ronald.boadana_snakehead-right.png')
        screen.blit(snake_head, snake_head_pos)
        if snake_head_pos == apple_pos:
            score_points_apple()
        if snake_head_pos == grape_pos:
            score_points_grape()
        if snake_head_pos == strawberry_pos:
            score_points_strawberry()

    if direction == LEFT:
        snake_head_pos = (snake[0][0] - 20, snake[0][1])
        snake_head = pygame.image.load('../snakepro/assets/ronald.boadana_snakehead-left.png')
        screen.blit(snake_head, snake_head_pos)
        if snake_head_pos == apple_pos:
            score_points_apple()
        if snake_head_pos == grape_pos:
            score_points_grape()
        if snake_head_pos == strawberry_pos:
            score_points_strawberry()

    return apple_pos
