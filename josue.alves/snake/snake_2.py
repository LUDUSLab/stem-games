# eat sound: https://freesound.org/people/josepharaoh99/sounds/353067/
# game over sound: https://freesound.org/people/myfox14/sounds/382310/

import pygame
import random

pygame.init()

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 150, 150)
blue = (50, 153, 213)

width = 600
height = 600

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake - Pygame Edition')

clock = pygame.time.Clock()

snake_block = 20
snake_speed = 13

font_style = pygame.font.SysFont('assets/PressStart2P.ttf', 25)
score_font = pygame.font.SysFont('assets/PressStart2P.ttf', 35)

apple = pygame.image.load('assets/apple_jo.png')
grass = pygame.image.load('assets/grass.png')
eat_sound_effect = pygame.mixer.Sound('assets/353067__josepharaoh99__bite-cartoon-style.mp3')
game_over_sound_effect = pygame.mixer.Sound('assets/382310__myfox14__game-over-arcade.wav')


def score(scorep):
    value = score_font.render("Your Score: " + str(scorep), True, yellow)
    screen.blit(value, [0, 0])


def snake(block, lis):
    for x in lis:
        pygame.draw.rect(screen, red, [x[0], x[1], block, block])


def message(msg, color):
    text = font_style.render(msg, True, color)
    screen.blit(text, [width / 6, height / 3])


def game_loop():
    game_over = False
    game_close = False

    x1 = width / 2
    y1 = height / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    food_x = round(random.randrange(0, width - snake_block) / 20.0) * 20.0
    food_y = round(random.randrange(0, height - snake_block) / 20.0) * 20.0

    while not game_over:

        while game_close:
            screen.fill(blue)
            message("You lost :( Press P to play again or Q to quit", red)
            score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_p:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_over_sound_effect.play()
            game_close = True
        x1 += x1_change
        y1 += y1_change
        screen.blit(grass, (0, 0))
        fruit_rect = pygame.Rect(food_x, food_y, snake_block, snake_block)
        screen.blit(apple, fruit_rect)
        snake_head = [x1, y1]
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_over_sound_effect.play()
                game_close = True

        snake(snake_block, snake_list)
        score(length_of_snake - 1)

        pygame.display.update()

        if x1 == food_x and y1 == food_y:
            food_x = round(random.randrange(0, width - snake_block) / 20.0) * 20.0
            food_y = round(random.randrange(0, height - snake_block) / 20.0) * 20.0
            length_of_snake += 1
            eat_sound_effect.play()

        clock.tick(snake_speed)

    pygame.quit()
    quit()


game_loop()
