from screen import *
import pygame
import apple

head_direction = 'RIGHT'
apple_coordinate = apple.apple_coord
sprite = pygame.image.load('assets/matheus.nielsen_snake.png')


# sets snake direction
def set_direction(direction):
    global head_direction
    head_direction = direction


# exports snake's direction
def get_direction():
    return head_direction


# controls snake movement
def movement():

    global apple_coordinate
    apple_coordinate = apple.get_coord()
    global snake

    # checks the snake's direction and moves it accordingly
    if head_direction == 'LEFT':
        snake[0] = (snake[0][0] - grid_square, snake[0][1])

    elif head_direction == 'RIGHT':
        snake[0] = (snake[0][0] + grid_square, snake[0][1])

    elif head_direction == 'UP':
        snake[0] = (snake[0][0], snake[0][1] - grid_square)

    elif head_direction == 'DOWN':
        snake[0] = (snake[0][0], snake[0][1] + grid_square)

    # moves the rest of the snake's body
    for i in range(len(snake) - 1, 0, -1):
        snake[i] = (snake[i - 1][0], snake[i - 1][1])
    for j in range(0, len(snake) - 4):
        snake_hitbox[j] = (snake[j + 3][0], snake[j + 3][1])


# snake render
def blit():

    for pos in snake:
        screen.blit(sprite, pos)


# Checks if the snake eats the apple
def on_apple_collision():
    if snake[0] == apple_coordinate:
        print('score')
        apple.score()
        snake.append(screen_size)
        snake_hitbox.append(screen_size)
        print(snake_hitbox)


# high score file
high_score_read = open('high_scores.md', 'r')


# checks if the snake hit the wall
def on_wall_collision():
    if not screen_size[0] - grid_square > snake[0][0] > 0 or not screen_size[1] - grid_square > snake[0][1] > hud_y:
        print(apple.get_points())
        game_over_sfx.play()
        return True


# checks if the snake hit itself
def on_player_collision():
    on_wall_collision()
    if snake[0] in snake_hitbox or on_wall_collision() == True:
        if apple.get_points() > int(high_score_read.read()):
            high_score_write = open('high_scores.md', 'w')
            high_score_write.write(str(apple.get_points()))
            high_score_write.close()
        game_over_sfx.play()
        return True


# player setup
snake = [(320, 320), (352, 320), (384, 320), (406, 320)]
snake_hitbox = [(406, 320)]
head_coord = (snake[0][0], snake[0][1])
