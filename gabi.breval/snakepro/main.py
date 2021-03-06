import pygame
import random
from pygame.locals import *
from tkinter.messagebox import showinfo
import fruit
import game
import wall
import config
import snake

clock = pygame.time.Clock()  # limit the fps
c = config.after_collision()
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

    if collision(snake[0], fruit.apple_food_pos):  # two tuples (first matrices´s line and apple food tuple)
        config.after_collision()

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
        if config.collision(snake_head_pos, apple_food_pos):  # two tuples (first matrices´s line and apple food tuple)
            config.after_collision()

    if my_direction == DOWN:
        snake_head_pos = (snake[0][0], snake[0][1] + 20)
        screen.blit(snake_head_down, snake_head_pos)
        if config.collision(snake_head_pos, apple_food_pos):  # two tuples (first matrices´s line and apple food tuple)
            config.after_collision()  # the snake grows, that´s why we add another tuple on it

    if my_direction == LEFT:
        snake_head_pos = (snake[0][0] - 20, snake[0][1])
        screen.blit(snake_head_left, snake_head_pos)
        if config.collision(snake_head_pos, apple_food_pos):  # two tuples (first matrices´s line and apple food tuple)
            config.after_collision()

    if my_direction == RIGHT:
        snake_head_pos = (snake[0][0] + 20, snake[0][1])
        screen.blit(snake_head_right, snake_head_pos)
        if config.collision(snake_head_pos, apple_food_pos):  # two tuples (first matrices´s line and apple food tuple)
            config.after_collision()

    screen.blit(game.grass, ((5, 0), (5, 550)))
    screen.blit(game.grass, ((5, 20), (5, 550)))
    screen.blit(game.grass, ((565, 20), (550, 50)))
    screen.blit(game.grass, ((565, 0), (550, 50)))

    screen.blit(apple_food, apple_food_pos)
    screen.blit(score_text, score_text_rect)
    screen.blit(apple_1_score, ((WIDTH / 2) - 50, apple_1_score_y))

    '''
     # Lines ---------------------------------------------------------------------------------------------- #
    pygame.draw.line(screen, COLOR_WHITE, [5, 50], [595, 50], 1)
    pygame.draw.line(screen, COLOR_WHITE, [5, 50], [5, 550], 1)
    pygame.draw.line(screen, COLOR_WHITE, [595, 50], [595, 550], 1)
    pygame.draw.line(screen, COLOR_WHITE, [5, 550], [595, 550], 1)
    
    '''
    for pos in snake:
        screen.blit(snake_skin, pos)

    pygame.display.update()
