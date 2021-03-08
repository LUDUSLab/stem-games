import pygame
import random
from pygame.locals import *
from itertools import cycle
from snake import *
from fruit import *


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
menu = True

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


def missiles_pos(position):
    x, y = position
    x -= 10
    if x < 0:
        x = 800
        y = random.randint(50, 530)
    return x, y


def on_grid_random():
    x = random.randint(25, 575)
    y = random.randint(50, 530)
    return x // 10 * 10, y // 10 * 10


def snake_moviment():
    global snake, my_direction
    if my_direction == UP:  # shakes the snake´s head
        snake[0] = (snake[0][0], snake[0][1] - 10)

    if my_direction == DOWN:  # shakes the snake´s head
        snake[0] = (snake[0][0], snake[0][1] + 10)

    if my_direction == RIGHT:  # shakes the snake´s head
        snake[0] = (snake[0][0] + 10, snake[0][1])

    if my_direction == LEFT:  # shakes the snake´s head
        snake[0] = (snake[0][0] - 10, snake[0][1])


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
    global score, apple_food_pos, snake
    apple_food_pos = on_grid_random()  # when there´s a collision the apple changes its position
    munch_sound_effect.play()  # sound
    score += 1
    snake.append((0, 0))
    return apple_food_pos


def restart():
    global score, snake, snake_head_pos, apple_food_pos, my_direction, died, obstacle_pos, \
        obstacle_pos2, obstacle_pos3, obstacle_pos4, obstacle_pos5
    score = 0
    snake.clear()  # cleaning the list
    snake = [(200, 200), (220, 200), (240, 200)]  # drawing it again
    my_direction = LEFT
    snake_head_pos = (snake[0][0] - 20, snake[0][1])
    apple_food_pos = on_grid_random()
    obstacle_pos = (750, 300)
    obstacle_pos2 = (750, 150)  # where does it start
    obstacle_pos3 = (750, 200)  # where does it start
    obstacle_pos4 = (750, 340)  # where does it start
    obstacle_pos5 = (750, 100)  # where does it start
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

# BLINK TEXT -------------------------------------------------------------------------------------------------------- #
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

# Grass -------------------------------------------------------------------------------------------------------- #
grass = pygame.image.load(address('gabi.breval.folha.png', 'skin'))