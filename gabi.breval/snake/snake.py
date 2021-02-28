import pygame
import random
from pygame.locals import *
from tkinter.messagebox import showinfo

WIDTH = 600
HEIGHT = 600
grid_size = 20

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # width, height, we are matrices
pygame.display.set_caption('Snake')

# Colors
light_grey = (200, 200, 200)
bg_color = pygame.Color('grey12')
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# score text
score_font = pygame.font.Font('C:/Users/55929/Documents/STEM/stem-games/gabi.breval/snake/assets/gabi.brevalFont.otf',
                              35)
score_text = score_font.render(' 0', True, COLOR_WHITE, COLOR_BLACK)
score_text_rect = score_text.get_rect()
score_text_rect.center = (WIDTH / 2, 30)
score = 0


def on_grid_random():
    x = random.randint(0, 590)
    y = random.randint(55, 590)

    return x // 10 * 10, y // 10 * 10


'''
So that he is always in multiples of 10 and this will make the snake "eat", inside the grid
'''


def collision(c1, c2):
    return c1[0] == c2[0] and c1[1] == c2[1]


UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

'''
Games and screens are represented by matrices
Every sequence is a tuple
'''

# Snake
snake_head = pygame.image.load('C:/Users/55929/Documents/STEM/stem-games/gabi.breval/snake/assets/'
                               'snake_head_gabi.breval.png')
snake = [(200, 200), (220, 200), (240, 200)]  # every sequence is a tuple
snake_skin = pygame.Surface((grid_size, grid_size))
snake_skin.fill((255, 255, 255))  # color

# Apple
apple_1_score = pygame.image.load('C:/Users/55929/Documents/STEM/stem-games/gabi.breval/snake/assets/'
                                  'gabi.breval.maca.png')
apple_1_score = pygame.transform.scale(apple_1_score, [30, 30])
apple_1_score_y = 10
apple_food = pygame.image.load('C:/Users/55929/Documents/STEM/stem-games/gabi.breval/snake/assets/'
                               'gabi.breval.maca.png')
apple_food = pygame.transform.scale(apple_food, [20, 20])
apple_food_pos = on_grid_random()
'''
apple = pygame.Surface((grid_size, grid_size))
apple.fill((255, 0, 0))  # color

'''
my_direction = LEFT
clock = pygame.time.Clock()  # limit the fps

while True:

    clock.tick(10)

    for event in pygame.event.get():  # identifies what was clicked
        if event.type == QUIT:
            pygame.quit()
        if event.type == KEYDOWN:
            if event.key == K_UP:
                my_direction = UP
            if event.key == K_DOWN:
                my_direction = DOWN
            if event.key == K_LEFT:
                my_direction = LEFT
            if event.key == K_RIGHT:
                my_direction = RIGHT

    if my_direction == UP:  # shakes the snake´s head
        snake[0] = (snake[0][0], snake[0][1] - 10)

    if my_direction == DOWN:  # shakes the snake´s head
        snake[0] = (snake[0][0], snake[0][1] + 10)

    if my_direction == RIGHT:  # shakes the snake´s head
        snake[0] = (snake[0][0] + 10, snake[0][1])

    if my_direction == LEFT:  # shakes the snake´s head
        snake[0] = (snake[0][0] - 10, snake[0][1])

    if collision(snake[0], apple_food_pos):  # two tuples (first matrices´s line and apple food tuple)
        apple_food_pos = on_grid_random()  # when there´s a collision the apple changes its position
        score += 1
        snake.append((0, 0))  # the snake grows, that´s why we add another tuple on it

    if snake[0][0] > 580 or snake[0][1] < 50 or snake[0][1] > 580 or snake[0][0] < 0:  # exceptions
        showinfo(title="Game Over", message="GAME OVER!!!")
        exit()

    for i in range(len(snake) - 1, 0, -1):  # shakes the rest of snakes´s body
        snake[i] = (snake[i - 1][0], snake[i - 1][1])

    # update score hud
    score_text = score_font.render(str(score), True, COLOR_WHITE, COLOR_BLACK)
    screen.fill((0, 0, 0))  # cleaning the screen
    screen.blit(apple_food, apple_food_pos)
    screen.blit(score_text, score_text_rect)
    screen.blit(apple_1_score, ((WIDTH / 2) - 50, apple_1_score_y))
    pygame.draw.line(screen, COLOR_WHITE, [0, 50], [600, 50], 1)

    '''
    Sintaxe :

    aaline(surface, color, start_pos, end_pos, blend=1)
    pygame.draw.line(screen, COLOR_WHITE, [0, 55], [600, 55], 1) ->
    É uma reta, logo ela precisa de dois pontos para existir e esses foram os pontos colocados

    ...
    E diferentemente do plano cartesino normal o pygame muda as orientacoes do plano entao o [0,0] é no canto 
    esquerdo da tela
    ...

    '''
    for pos in snake:
        screen.blit(snake_skin, pos)

    pygame.display.update()
