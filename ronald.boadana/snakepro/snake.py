from fruit import *
from config import *
from game import *


snake = [(200, 200), (220, 200), (240, 200)]
snake_head = pygame.image.load('../snakepro/assets/ronald.boadana_snakehead-right.png')
snake_body = pygame.image.load('../snakepro/assets/ronald.boadana_snakebody.png')

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3
direction = LEFT


def body_snake_move():
    global snake, snake_head, snake_body, direction
    if direction == UP:
        snake_head_pos = (snake[0][0], snake[0][1] - 20)
        snake_head = pygame.image.load('../snakepro/assets/ronald.boadana_snakehead-up.png')
        screen.blit(snake_head, snake_head_pos)
        if snake_head_pos == apple_pos:
            score_points_apple()
        elif snake_head_pos == grape_pos:
            score_points_grape()
        elif snake_head_pos == strawberry_pos:
            score_points_strawberry()

    if direction == DOWN:
        snake_head_pos = (snake[0][0], snake[0][1] + 20)
        snake_head = pygame.image.load('../snakepro/assets/ronald.boadana_snakehead-down.png')
        screen.blit(snake_head, snake_head_pos)
        if snake_head_pos == apple_pos:
            score_points_apple()
        elif snake_head_pos == grape_pos:
            score_points_grape()
        elif snake_head_pos == strawberry_pos:
            score_points_strawberry()

    if direction == RIGHT:
        snake_head_pos = (snake[0][0] + 20, snake[0][1])
        snake_head = pygame.image.load('../snakepro/assets/ronald.boadana_snakehead-right.png')
        screen.blit(snake_head, snake_head_pos)
        if snake_head_pos == apple_pos:
            score_points_apple()
        elif snake_head_pos == grape_pos:
            score_points_grape()
        elif snake_head_pos == strawberry_pos:
            score_points_strawberry()

    if direction == LEFT:
        snake_head_pos = (snake[0][0] - 20, snake[0][1])
        snake_head = pygame.image.load('../snakepro/assets/ronald.boadana_snakehead-left.png')
        screen.blit(snake_head, snake_head_pos)
        if snake_head_pos == apple_pos:
            score_points_apple()
        elif snake_head_pos == grape_pos:
            score_points_grape()
        elif snake_head_pos == strawberry_pos:
            score_points_strawberry()
