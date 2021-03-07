from __future__ import absolute_import, division, print_function
import pygame
import random
from pygame.locals import *
from itertools import cycle

WIDTH = 800
HEIGHT = 600
grid_size = 32
SCORE_MAX = 0

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # width, height, we are matrices
pygame.display.set_caption('Snake')

clock = pygame.time.Clock()  # limit the fps
BLINK_EVENT = pygame.USEREVENT + 0
died = False

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3
my_direction = LEFT


def verifying_score_max():
    global score, SCORE_MAX
    if score > SCORE_MAX:
        SCORE_MAX = score

    return SCORE_MAX


def game_over_screen():
    global highest_score, highest_score_txt, blink_surface, blink_rect
    screen.fill((0, 0, 0))
    for event_over in pygame.event.get():  # identifies what was clicked
        if event_over.type == QUIT:
            pygame.quit()
        if event_over.type == KEYDOWN:
            if event_over.key == K_r:
                restart()
        if event_over.type == BLINK_EVENT:
            blink_surface = next(blink_surfaces)

    highest_score = verifying_score_max()
    highest_score_txt = score_font.render('HIGHEST SCORE : ' + str(highest_score), True, COLOR_WHITE, COLOR_BLACK)
    screen.blit(highest_score_txt, highest_score_txt_rect)
    screen.blit(blink_surface, blink_rect)
    screen.blit(score_text, (WIDTH / 2, 330))
    screen.blit(apple_1_score, ((WIDTH / 2) - 50, 330))
    clock.tick(50)
    pygame.display.update()


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

    skins = 'C:/Users/55929/Documents/stem-games/gabi.breval/snakepro/assets/skin/'
    sounds = 'C:/Users/55929/Documents/stem-games/gabi.breval/snakepro/assets/sound/'
    fonts = 'C:/Users/55929/Documents/stem-games/gabi.breval/snakepro/assets/font/'

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
    global score, apple_food_pos, snake, obstacle_pos
    apple_food_pos = on_grid_random()  # when there´s a collision the apple changes its position
    obstacle_pos = on_grid_random()
    munch_sound_effect.play()  # sound
    score += 1
    snake.append((0, 0))
    return apple_food_pos, obstacle_pos


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
score_font = pygame.font.Font(address('gabi.brevalFont.otf', 'font'), 35)
score_text = score_font.render(' 0', True, COLOR_WHITE, COLOR_BLACK)
score_text_rect = score_text.get_rect()
score_text_rect.center = (WIDTH / 2, 30)
score = 0

highest_score_font = pygame.font.Font(address('gabi.brevalFont.otf', 'font'), 35)
highest_score = SCORE_MAX
highest_score_txt = score_font.render(str(highest_score), True, COLOR_WHITE, COLOR_BLACK)
highest_score_txt_rect = highest_score_txt.get_rect()
highest_score_txt_rect.center = (WIDTH / 2 - 95, 580)

# Sound ------------------------------------------------------------------------------------------------------- #
munch_sound_effect = pygame.mixer.Sound(address('gabi.breval.munch-sound.wav', 'sound'))
game_over_effect = pygame.mixer.Sound(address('batida_gabi.breval.wav', 'sound'))

# Grass -------------------------------------------------------------------------------------------------------- #
grass = pygame.image.load(address('gabi.breval.folha.png', 'skin'))

# Apple ------------------------------------------------------------------------------------------------------ #
apple_1_score = pygame.image.load(address('gabi.breval.maca.png', 'skin'))
apple_1_score = pygame.transform.scale(apple_1_score, [32, 32])
apple_1_score_y = 10
apple_food = pygame.image.load(address('gabi.breval.maca.png', 'skin'))
apple_food = pygame.transform.scale(apple_food, [grid_size, grid_size])
apple_food_pos = on_grid_random()

# Snake ------------------------------------------------------------------------------------------------------- #
'''
Games and screens are represented by matrices
Every sequence is a tuple
'''

snake_head = pygame.image.load(address('snake_head_gabi.breval.png', 'skin'))
snake = [(200, 200), (220, 200), (240, 200)]  # every sequence is a tuple
snake_head_pos = (snake[0][0] - 20, snake[0][1])
snake_head = pygame.transform.scale(snake_head, [grid_size, grid_size])
snake_skin = pygame.Surface((grid_size, grid_size))
snake_skin.fill((0, 255, 0))  # color

# Obstacles -------------------------------------------------------------------------------------------------- #
obstacle = pygame.image.load(address('gabi.breval.misseis.png', 'skin'))
obstacle = pygame.transform.scale(obstacle, [60, 60])
obstacle_pos = on_grid_random()

# Rotation  -------------------------------------------------------------------------------------------------- #
snake_copy = snake_head.copy()
snake_head_down = pygame.transform.rotate(snake_copy, 180)
snake_head_left = pygame.transform.rotate(snake_copy, 90)
snake_head_right = pygame.transform.rotate(snake_copy, 270)
snake_head_up = pygame.transform.rotate(snake_copy, 0)

# BLINK TEXT ------------------------------------------------------------------------------------------------- #
font = pygame.font.Font(address('gabi.brevalFont.otf', 'font'), 35)
message = "Press R to Start Again"
formatted_text = font.render(message, True, COLOR_WHITE, COLOR_BLACK)
ret_text = formatted_text.get_rect()
screen_rect = screen.get_rect()

blink_rect = formatted_text.get_rect()
blink_rect.center = screen_rect.center
off_text_surface = pygame.Surface(blink_rect.size)
blink_surfaces = cycle([formatted_text, off_text_surface])
blink_surface = next(blink_surfaces)
pygame.time.set_timer(BLINK_EVENT, 150)

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

    # Checking collision --------------------------------------------------------------------------------------------- #
    cobra = pygame.draw.rect(screen, (0, 255, 0), (snake[0][0], snake[0][1], 32, 32))
    fruit = pygame.draw.rect(screen, (255, 0, 0), (apple_food_pos[0], apple_food_pos[1], 32, 32))
    bomb = pygame.draw.rect(screen, (255, 0, 0), (obstacle_pos[0], obstacle_pos[1], 40, 40))

    if cobra.colliderect(fruit):
        after_collision()

    if cobra.colliderect(bomb):
        died = True
        while died:
            game_over_screen()

    # Checking if there was a collision with herself ---------------------------------------------------------------- #
    if snake.count(snake_head_pos) > 1:
        died = True
        while died:
            game_over_screen()

    # Checking if the snake has reached the limits of the screen ---------------------------------------------------- #
    if snake[0][0] > 800:
        snake[0] = (0, snake[0][1])
    if snake[0][0] < 0:
        snake[0] = (800, snake[0][1])
    if snake[0][1] > 600:
        snake[0] = (snake[0][0], 55)
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

    screen.blit(obstacle, obstacle_pos)
    screen.blit(apple_food, apple_food_pos)
    screen.blit(score_text, score_text_rect)
    screen.blit(apple_1_score, ((WIDTH / 2) - 50, apple_1_score_y))

    for pos in snake:
        screen.blit(snake_skin, pos)

    pygame.display.update()
