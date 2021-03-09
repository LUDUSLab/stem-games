import pygame
from snake import *
from fruit import *
from config import *

playing_sound = 0
player_score = 0

# sounds
game_over_sound = pygame.mixer.Sound('../snake/assets/game-over-sound.wav')
victory_sound = pygame.mixer.Sound('../snake/assets/victory-sound.wav')
eating_fruit_sound = pygame.mixer.Sound('../snake/assets/eating-apple-sound.wav')


def game_over():
    global playing_sound
    screen.fill(color_black)
    screen.blit(defeat_text, defeat_text_rect)
    if playing_sound == 0:
        game_over_sound.play()
        playing_sound += 1


def victory():
    global player_score, playing_sound
    screen.fill(color_black)
    screen.blit(victory_text, victory_text_rect)
    if playing_sound == 0:
        victory_sound.play()
        playing_sound += 1


def score_points_apple():
    global apple_pos, player_score
    apple_pos = apple_randomness_movement()
    eating_fruit_sound.play()
    snake.append((600, 600))
    player_score += 1
    return apple_pos, player_score


def score_points_grape():
    global grape_pos, player_score
    grape_pos = grape_randomness_movement()
    eating_fruit_sound.play()
    snake.append((600, 600))
    player_score += 3
    return grape_pos, player_score


def score_points_strawberry():
    global strawberry_pos, player_score
    strawberry_pos = strawberry_randomness_movement()
    eating_fruit_sound.play()
    snake.append((600, 600))
    player_score += 2
    return strawberry_pos, player_score


# looping to make the key pressed move the snake
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3
direction = LEFT


def game_loop():
    global direction, apple_pos, playing_sound, player_score, snake_body, snake_head, grape_pos, strawberry_pos
    game_on = True
    game_clock = pygame.time.Clock()
    while game_on:
        game_clock.tick(15)
        snake_head_pos = (snake[0][0] + 20, snake[0][1])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_on = False
            # mapping keys
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    direction = UP
                if event.key == pygame.K_s:
                    direction = DOWN
                if event.key == pygame.K_a:
                    direction = LEFT
                if event.key == pygame.K_d:
                    direction = RIGHT
        if direction == UP:
            snake[0] = (snake[0][0], snake[0][1] - 10)
        if direction == DOWN:
            snake[0] = (snake[0][0], snake[0][1] + 10)
        if direction == RIGHT:
            snake[0] = (snake[0][0] + 10, snake[0][1])
        if direction == LEFT:
            snake[0] = (snake[0][0] - 10, snake[0][1])

        # checking the score
        if snake_head_pos == apple_pos:
            score_points_apple()

        if snake_head_pos == grape_pos:
            score_points_grape()

        if snake_head_pos == strawberry_pos:
            score_points_strawberry()

        # updating score
        score_text = score_font.render('SCORE:' + str(player_score), True, color_white, color_black)
        snake_head_pos = (snake[0][1] - 20, snake[0][1])

        for i in range(len(snake) - 1, 0, -1):
            snake[i] = (snake[i - 1][0], snake[i - 1][1])

        else:
            body_snake_move()

            # updating screen
            screen.blit(score_text, score_text_rect)
            screen.blit(apple, apple_pos)
            screen.blit(grape, grape_pos)
            screen.blit(strawberry, strawberry_pos)

            for pos in snake:
                screen.blit(snake_body, pos)
            screen.blit(snake_head, snake_head_pos)

            # drawing the borders
            draw_borders()


if (snake[0][0] < 0) or (snake[0][1] < 40) or (snake[0][0] > 570) or (snake[0][1] > 570):
    game_over()
elif player_score == 10:
    victory()

game_loop()
