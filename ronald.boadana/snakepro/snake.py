from fruit import *
from config import *
from game import *

# snake positions and sprites
snake = [(320, 320), (288, 320), (256, 320), (224, 320)]
snake_head = pygame.image.load('../snakepro/assets/ronald.boadana_snakehead2.png')
snake_head_pos = snake[0]
snake_body = pygame.image.load('../snakepro/assets/ronald.boadana_snakebody.png')

# looping to make the key pressed move the snake
UP = 32
RIGHT = 33
DOWN = 34
LEFT = 35
direction = LEFT


def body_snake_move():
    global snake, snake_head, snake_body, direction, snake_head_pos
    if direction == UP:
        snake_head_pos = (snake[0][0], snake[0][1] - 32)

    if direction == DOWN:
        snake_head_pos = (snake[0][0], snake[0][1] + 32)

    if direction == RIGHT:
        snake_head_pos = (snake[0][0] + 32, snake[0][1])

    if direction == LEFT:
        snake_head_pos = (snake[0][0] - 32, snake[0][1])


def drawing_snake():
    for i in range(1, len(snake)):
        screen.blit(snake_body, snake[i])
    screen.blit(snake_head, snake[0])
