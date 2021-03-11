from fruit import *
from config import *
from game import *

# snake positions and sprites
snake = [(320, 320), (288, 320), (256, 320)]
snake_head = pygame.image.load('../snakepro/assets/ronald.boadana_snakehead-right.png')
snake_head_pos = (snake[0][0] + 32, snake[0][1])
snake_body = pygame.image.load('../snakepro/assets/ronald.boadana_snakebody.png')

# different snake's head positions
s_UP = pygame.image.load('../snakepro/assets/ronald.boadana_snakehead-up.png')
s_DOWN = pygame.image.load('../snakepro/assets/ronald.boadana_snakehead-down.png')
s_RIGHT = pygame.image.load('../snakepro/assets/ronald.boadana_snakehead-right.png')
s_LEFT = pygame.image.load('../snakepro/assets/ronald.boadana_snakehead-left.png')

# looping to make the key pressed move the snake
UP = 32
RIGHT = 33
DOWN = 34
LEFT = 35
direction = LEFT


def body_snake_move():
    global snake, snake_head, snake_body, direction, snake_head_pos
    snake_head_pos = (snake[0][0] + 32, snake[0][1])
    if direction == UP:
        snake_head_pos = (snake[0][0], snake[0][1] - 32)
        snake_head_pos = snake[0]
        snake_head = s_UP
        screen.blit(snake_head, snake_head_pos)

    elif direction == DOWN:
        snake_head_pos = (snake[0][0], snake[0][1] + 32)
        snake_head_pos = snake[0]
        snake_head = s_DOWN
        screen.blit(snake_head, snake_head_pos)

    elif direction == RIGHT:
        snake_head_pos = (snake[0][0] + 32, snake[0][1])
        snake_head_pos = snake[0]
        snake_head = s_RIGHT
        screen.blit(snake_head, snake_head_pos)

    elif direction == LEFT:
        snake_head_pos = (snake[0][0] - 32, snake[0][1])
        snake_head_pos = snake[0]
        snake_head = s_LEFT
        screen.blit(snake_head, snake_head_pos)
