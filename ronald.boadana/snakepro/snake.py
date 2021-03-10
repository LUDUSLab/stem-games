from fruit import *
from config import *
from game import *

eating_fruit_sound = pygame.mixer.Sound('../snake/assets/eating-apple-sound.wav')
snake = [(320, 320), (352, 320), (384, 320)]
snake_head = pygame.image.load('../snakepro/assets/ronald.boadana_snakehead-right.png')
snake_body = pygame.image.load('../snakepro/assets/ronald.boadana_snakebody.png')

UP = 32
RIGHT = 33
DOWN = 34
LEFT = 35
direction = LEFT


def body_snake_move():
    global snake, snake_head, snake_body, direction, snake_head_pos, apple_pos, player_score, grape_pos, strawberry_pos, eating_fruit_sound
    if direction == UP:
        snake_head_pos = (snake[0][0], snake[0][1] - 32)
        snake_head = pygame.image.load('../snakepro/assets/ronald.boadana_snakehead-up.png')
        screen.blit(snake_head, snake_head_pos)

    if direction == DOWN:
        snake_head_pos = (snake[0][0], snake[0][1] + 32)
        snake_head = pygame.image.load('../snakepro/assets/ronald.boadana_snakehead-down.png')

    if direction == RIGHT:
        snake_head_pos = (snake[0][0] + 32, snake[0][1])
        snake_head = pygame.image.load('../snakepro/assets/ronald.boadana_snakehead-right.png')

    if direction == LEFT:
        snake_head_pos = (snake[0][0] - 32, snake[0][1])
        snake_head = pygame.image.load('../snakepro/assets/ronald.boadana_snakehead-left.png')