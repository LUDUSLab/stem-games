import pygame
import random
from pygame.locals import *
from tkinter.messagebox import showinfo

WIDTH = 800
HEIGHT = 600
grid_size = 32

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # width, height, we are matrices
pygame.display.set_caption('Snake')

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3
my_direction = LEFT


def collision(c1, c2):
    return c1[0] == c2[0] and c1[1] == c2[1]


def on_grid_random():
    x = random.randint(25, 575)
    y = random.randint(50, 530)
    return x // 10 * 10, y // 10 * 10


def address(name, genre):
    #  skins = "/home/gabibreval/Documentos/stem-games/gabi.breval/snakepro/assets/skins/"
    #  sounds = "/home/gabibreval/Documentos/stem-games/gabi.breval/snakepro/assets/sounds/"
    #  fonts = "/home/gabibreval/Documentos/stem-games/gabi.breval/snakepro/assets/fonts/"

    skins = 'C:/Users/55929/Documents/stem-games/gabi.breval/snakepro/assets/font/'
    sounds = 'C:/Users/55929/Documents/stem-games/gabi.breval/snakepro/assets/sound/'
    fonts = 'C:/Users/55929/Documents/stem-games/gabi.breval/snakepro/assets/skin/'

    if genre == "skin":
        directory = skins + name
        return directory

    elif genre == "sound":
        directory = sounds + name
        return directory

    elif genre == "font":
        directory = fonts + name
        return directory


def after_collision():
    global score, apple_food_pos, snake
    apple_food_pos = on_grid_random()  # when there´s a collision the apple changes its position
    munch_sound_effect.play()  # sound
    score += 1
    snake.append((0, 0))
    return apple_food_pos


def restart():
    global score, snake, snake_head_pos, apple_food_pos, my_direction, died
    score = 0
    snake.clear()  # limpando a lista
    snake = [(200, 200), (220, 200), (240, 200)]  # desenhando ela dnv
    my_direction = LEFT
    snake_head_pos = (snake[0][0] - 20, snake[0][1])
    apple_food_pos = on_grid_random()
    died = False


# Colors ------------------------------------------------------------------------------------------------------- #
light_grey = (200, 200, 200)
bg_color = pygame.Color('grey12')
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# score text --------------------------------------------------------------------------------------------------- #
score_font = pygame.font.Font(
    'C:/Users/55929/Documents/stem-games/gabi.breval/snakepro/assets/font/gabi.brevalFont.otf', 35)
score_text = score_font.render(' 0', True, COLOR_WHITE, COLOR_BLACK)
score_text_rect = score_text.get_rect()
score_text_rect.center = (WIDTH / 2, 30)
score = 0

# Sound ------------------------------------------------------------------------------------------------------- #
munch_sound_effect = pygame.mixer.Sound(address('gabi.breval.munch-sound.wav', 'sound'))
game_over_effect = pygame.mixer.Sound(address('batida_gabi.breval.wav', 'sound'))

# Grass -------------------------------------------------------------------------------------------------------- #
grass = pygame.image.load('C:/Users/55929/Documents/stem-games/gabi.breval/snakepro/assets/skin/gabi.breval.folha.png')

# Apple ------------------------------------------------------------------------------------------------------ #
apple_1_score = pygame.image.load('C:/Users/55929/Documents/stem-games/gabi.breval/snakepro/assets/skin/'
                                  'gabi.breval.maca.png')
apple_1_score = pygame.transform.scale(apple_1_score, [20, 20])
apple_1_score_y = 10
apple_food = pygame.image.load('C:/Users/55929/Documents/stem-games/gabi.breval/snakepro/assets/skin/'
                               'gabi.breval.maca.png')
apple_food = pygame.transform.scale(apple_food, [grid_size, grid_size])
apple_food_pos = on_grid_random()

# Snake ------------------------------------------------------------------------------------------------------- #
'''
Games and screens are represented by matrices
Every sequence is a tuple
'''

snake_head = pygame.image.load('C:/Users/55929/Documents/stem-games/gabi.breval/snakepro/assets/skin/'
                               'snake_head_gabi.breval.png')
snake = [(200, 200), (220, 200), (240, 200)]  # every sequence is a tuple
snake_head_pos = (snake[0][0] - 20, snake[0][1])
snake_head = pygame.transform.scale(snake_head, [grid_size, grid_size])
snake_skin = pygame.Surface((grid_size, grid_size))
snake_skin.fill((0, 255, 0))  # color

# Rotation  -------------------------------------------------------------------------------------------------- #
snake_copy = snake_head.copy()
snake_head_down = pygame.transform.rotate(snake_copy, 180)
snake_head_left = pygame.transform.rotate(snake_copy, 90)
snake_head_right = pygame.transform.rotate(snake_copy, 270)
snake_head_up = pygame.transform.rotate(snake_copy, 0)

clock = pygame.time.Clock()  # limit the fps
died = False

while True:

    clock.tick(20)

    snake_head_pos = (snake[0])

    for event in pygame.event.get():  # identifies what was clicked
        if event.type == QUIT:
            pygame.quit()
        if event.type == KEYDOWN:

            if event.key == K_UP:
                if my_direction == DOWN:
                    pass
                else:
                    my_direction = UP

            if event.key == K_DOWN:
                if my_direction == UP:
                    pass
                else:
                    my_direction = DOWN

            if event.key == K_LEFT:
                if my_direction == RIGHT:
                    pass
                else:
                    my_direction = LEFT

            if event.key == K_RIGHT:
                if my_direction == LEFT:
                    pass
                else:
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
        after_collision()

    # Checking if there was a collision with herself ---------------------------------------------------------------- #
    if snake.count(snake_head_pos) > 1:
        font = pygame.font.SysFont('C:/Users/55929/Documents/stem-games/'
                                      'gabi.breval/snakepro/assets/font/gabi.brevalFont.otf', 35,
                                      True, True)
        message = "Press R to Start Again"
        formatted_text = font.render(message, True, COLOR_WHITE, COLOR_BLACK)
        ret_text = formatted_text.get_rect()

        died = True

        while died:
            screen.fill((0, 0, 0))
            for event in pygame.event.get():  # identifies what was clicked
                if event.type == QUIT:
                    pygame.quit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        restart()

            ret_text.center = ((WIDTH / 2), HEIGHT/ 2)
            screen.blit(formatted_text, ret_text)
            pygame.display.update()

    # Checking if the snake has reached the limits of the screen ---------------------------------------------------- #
    if snake[0][0] > 800:
        snake[0] = (0, snake[0][1])
    if snake[0][0] < 0:
        snake[0] = (800, snake[0][1])
    if snake[0][1] > 600:
        snake[0] = (snake[0][0], 0)
    if snake[0][1] < 55:
        snake[0] = (snake[0][0], 600)

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
    screen.blit(grass, ((770, 20), (550, 50)))
    screen.blit(grass, ((770, 0), (550, 50)))

    pygame.draw.line(screen, COLOR_WHITE, [5, 50], [800, 50], 1)

    screen.blit(apple_food, apple_food_pos)
    screen.blit(score_text, score_text_rect)
    screen.blit(apple_1_score, ((WIDTH / 2) - 50, apple_1_score_y))

    for pos in snake:
        screen.blit(snake_skin, pos)

    pygame.display.update()