import pygame
import random
from pygame.locals import *
from tkinter.messagebox import showinfo
import fruit
import game
import wall
import config
import snake

WIDTH = 800
HEIGHT = 600
grid_size = 20

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # width, height, we are matrices
pygame.display.set_caption('Snake')


def on_grid_random():
    x = random.randint(25, 575)
    y = random.randint(50, 530)

    return x // 10 * 10, y // 10 * 10


'''
So that he is always in multiples of 10 and this will make the snake "eat", inside the grid
'''


def collision(c1, c2):
    return c1[0] == c2[0] and c1[1] == c2[1]




# Colors ------------------------------------------------------------------------------------------------------- #
light_grey = (200, 200, 200)
bg_color = pygame.Color('grey12')
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# score text --------------------------------------------------------------------------------------------------- #
score_font = pygame.font.Font('/home/gabibreval/Documentos/stem-games/gabi.breval/snake/assets/'
                              'gabi.brevalFont.otf',
                              35)
score_text = score_font.render(' 0', True, COLOR_WHITE, COLOR_BLACK)
score_text_rect = score_text.get_rect()
score_text_rect.center = (WIDTH / 2, 30)
score = 0

# Game over text ----------------------------------------------------------------------------------------------- #
lose_font = pygame.font.Font('/home/gabibreval/Documentos/stem-games/gabi.breval/snake/assets/'
                             'gabi.brevalFont.otf',
                             100)
lose_text = lose_font.render('Game over!', True, COLOR_WHITE, COLOR_BLACK)
lose_text_rect = score_text.get_rect()
lose_text_rect.center = (600, 350)
# -------------------------------------------------------------------------------------------------------------- #

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

# Snake ------------------------------------------------------------------------------------------------------- #
'''
Games and screens are represented by matrices
Every sequence is a tuple
'''
snake_head = pygame.image.load('/home/gabibreval/Documentos/stem-games/gabi.breval/snake/assets/skins/'
                               'snake_head_gabi.breval.png')
snake = [(200, 200), (220, 200), (240, 200)]  # every sequence is a tuple
snake_head_pos = (snake[0][0] - 20, snake[0][1])
snake_head = pygame.transform.scale(snake_head, [20, 20])
snake_skin = pygame.Surface((grid_size, grid_size))
snake_skin.fill((0, 255, 0))  # color

# Sound ------------------------------------------------------------------------------------------------------ #
munch_sound_effect = pygame.mixer.Sound('/home/gabibreval/Documentos/stem-games/gabi.breval/snake/assets/sounds/'
                                        'gabi.breval.munch-sound.wav')
game_over_effect = pygame.mixer.Sound('/home/gabibreval/Documentos/stem-games/'
                                      'gabi.breval/snake/assets/sounds/batida_gabi.breval.wav')

# Rotation  -------------------------------------------------------------------------------------------------- #
snake_copy = snake_head.copy()
snake_head_down = pygame.transform.rotate(snake_copy, 180)
snake_head_left = pygame.transform.rotate(snake_copy, 90)
snake_head_right = pygame.transform.rotate(snake_copy, 270)
snake_head_up = pygame.transform.rotate(snake_copy, 0)

# Apple ------------------------------------------------------------------------------------------------------ #
apple_1_score = pygame.image.load('/home/gabibreval/Documentos/stem-games/gabi.breval/snake/assets/skins/'
                                  'gabi.breval.maca.png')
apple_1_score = pygame.transform.scale(apple_1_score, [20, 20])
apple_1_score_y = 10
apple_food = pygame.image.load('/home/gabibreval/Documentos/stem-games/gabi.breval/snake/assets/skins/'
                               'gabi.breval.maca.png')
apple_food = pygame.transform.scale(apple_food, [20, 20])
apple_food_pos = on_grid_random()


def after_collision():
    global score, apple_food_pos
    apple_food_pos = on_grid_random()  # when there´s a collision the apple changes its position
    munch_sound_effect.play()  # sound
    score += 1
    snake.append((0, 0))
    return apple_food_pos

# Grass -------------------------------------------------------------------------------------------------------- #
grass = pygame.image.load('/home/gabibreval/Documentos/stem-games/gabi.breval/snake/assets/skins/'
                          'gabi.breval.folha.png')


my_direction = LEFT
clock = pygame.time.Clock()  # limit the fps

while True:

    clock.tick(10)

    snake_head_pos = (snake[0])

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
        munch_sound_effect.play()  # sound
        score += 1
        snake.append((0, 0))  # the snake grows, that´s why we add another tuple on it

    if snake[0][0] > 575 or snake[0][1] < 50 or snake[0][1] > 530 or snake[0][0] < 5:  # exceptions
        game_over_effect.play()
        showinfo(title="Game Over", message="GAME OVER!!!")
        exit()

    for i in range(len(snake) - 1, 0, -1):  # shakes the rest of snakes´s body
        snake[i] = (snake[i - 1][0], snake[i - 1][1])

    # Update score hud --------------------------------------------------------------------------------- #

    snake_head_pos = (snake[0][0] - 20, snake[0][1])
    score_text = score_font.render(str(score), True, COLOR_WHITE, COLOR_BLACK)
    screen.fill((0, 0, 0))  # cleaning the screen

    # Sprites ------------------------------------------------------------------------------------------ #

    if my_direction == UP:
        snake_head_pos = (snake[0][0], snake[0][1] - 20)
        screen.blit(snake_head_up, snake_head_pos)
        if collision(snake_head_pos, apple_food_pos):  # two tuples (first matrices´s line and apple food tuple)
            after_collision()

    if my_direction == DOWN:
        snake_head_pos = (snake[0][0], snake[0][1] + 20)
        screen.blit(snake_head_down, snake_head_pos)
        if collision(snake_head_pos, apple_food_pos):  # two tuples (first matrices´s line and apple food tuple)
            after_collision()  # the snake grows, that´s why we add another tuple on it

    if my_direction == LEFT:
        snake_head_pos = (snake[0][0] - 20, snake[0][1])
        screen.blit(snake_head_left, snake_head_pos)
        if collision(snake_head_pos, apple_food_pos):  # two tuples (first matrices´s line and apple food tuple)
            after_collision()

    if my_direction == RIGHT:
        snake_head_pos = (snake[0][0] + 20, snake[0][1])
        screen.blit(snake_head_right, snake_head_pos)
        if collision(snake_head_pos, apple_food_pos):  # two tuples (first matrices´s line and apple food tuple)
            after_collision()

    screen.blit(grass, ((5, 0), (5, 550)))
    screen.blit(grass, ((5, 20), (5, 550)))
    screen.blit(grass, ((565, 20), (550, 50)))
    screen.blit(grass, ((565, 0), (550, 50)))

    screen.blit(apple_food, apple_food_pos)
    screen.blit(score_text, score_text_rect)
    screen.blit(apple_1_score, ((WIDTH / 2) - 50, apple_1_score_y))

    # Lines ---------------------------------------------------------------------------------------------- #
    pygame.draw.line(screen, COLOR_WHITE, [5, 50], [595, 50], 1)
    pygame.draw.line(screen, COLOR_WHITE, [5, 50], [5, 550], 1)
    pygame.draw.line(screen, COLOR_WHITE, [595, 50], [595, 550], 1)
    pygame.draw.line(screen, COLOR_WHITE, [5, 550], [595, 550], 1)

    for pos in snake:
        screen.blit(snake_skin, pos)

    pygame.display.update()
