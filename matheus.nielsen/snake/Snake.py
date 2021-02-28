# Snake with Pygame by Matheus Nielsen 2021
# Pygame website https://www.pygame.org/news
# Version 0.2
# Bite sfx by Koops available at https://freesound.org/people/Koops/sounds/20269/
# Game Over sfx by myfox14 available at https://freesound.org/people/myfox14/sounds/382310/
# Game font Press Start 2P, available at https://fonts.google.com/specimen/Press+Start+2P?preview.text_type=custom

import pygame
from random import randrange

pygame.init()

# Game sound effects
apple_sfx = pygame.mixer.Sound("assets/20269__koops__apple-crunch-06.wav")
game_over_sfx = pygame.mixer.Sound("assets/382310__myfox14__game-over-arcade.wav")

# score
score = 0
score_font = pygame.font.Font('assets/PressStart2P.ttf', 32)
score_text = score_font.render('SCORE: 0', False, (255, 255, 255))
score_text_rect = score_text.get_rect()
score_text_rect.center = (320, 50)

# Game over text
game_over_font = pygame.font.Font('assets/PressStart2P.ttf', 50)
game_over_text = game_over_font.render('GAME OVER', False, (255, 255, 255))
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (320, 320)

# Screen render
screen_size = (640, 640)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Snake with Pygame - Version 0.2")

# Apple render
apple = pygame.image.load("assets/matheus.nielsen_apple.png")
apple_coordinates = (randrange(0, 640, 32), randrange(0, 640, 32))

# Snake render
snake = [(320, 320), (352, 320), (384, 320)]
snake_hitbox = []
snake_head = pygame.image.load("assets/matheus.nielsen_snake_head.png")
snake_body = pygame.image.load("assets/matheus.nielsen_snake_body.png")

# Snake directions
up = 0
right = 1
down = 2
left = 3
current_direction = 1

# Game loop
game_loop = True
game_clock = pygame.time.Clock()
defeat = False

while game_loop is True:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop = False

        #  Movement keys
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and (current_direction == 1 or current_direction == 3):
                current_direction = 0
            if event.key == pygame.K_RIGHT and (current_direction == 0 or current_direction == 2):
                current_direction = 1
            if event.key == pygame.K_DOWN and (current_direction == 1 or current_direction == 3):
                current_direction = 2
            if event.key == pygame.K_LEFT and (current_direction == 0 or current_direction == 2):
                current_direction = 3

    # Checking defeat condition
    if defeat is False:

        # Snake parts movement
        for i in range(len(snake) - 1, 0, -1):
            snake[i] = (snake[i - 1][0], snake[i - 1][1])
        for j in range(0, len(snake) - 4):
            snake_hitbox[j] = (snake[j + 3][0], snake[j + 3][1])

        # Snake head movement
        if current_direction == up:
            snake[0] = (snake[0][0], snake[0][1] - 32)
        if current_direction == right:
            snake[0] = (snake[0][0] + 32, snake[0][1])
        if current_direction == down:
            snake[0] = (snake[0][0], snake[0][1] + 32)
        if current_direction == left:
            snake[0] = (snake[0][0] - 32, snake[0][1])

        # Code that makes the snake head teleport to the other side
        if snake[0][0] > 608:
            snake[0] = (0, snake[0][1])
        if snake[0][0] < 0:
            snake[0] = (608, snake[0][1])
        if snake[0][1] > 608:
            snake[0] = (snake[0][0], 0)
        if snake[0][1] < 0:
            snake[0] = (snake[0][0], 608)

        # defeat condition
        if snake[0] in snake_hitbox:
            defeat = True
            pygame.mixer.Sound.play(game_over_sfx)

        # Point scoring and apple randomizer
        if snake[0] == apple_coordinates:
            # Apple coordinate smart randomizer
            if apple_coordinates[0] <= 320:
                # Quadrant 1 - up and left
                if apple_coordinates[1] <= 320:
                    apple_coordinates = (randrange(320, 640, 32), randrange(0, 640, 32))
                # Quadrant 2 - up and right
                elif apple_coordinates[1] > 320:
                    apple_coordinates = (randrange(0, 352, 32), randrange(0, 640, 32))
            if apple_coordinates[0] > 320:
                # Quadrant 3 - down and left
                if apple_coordinates[1] <= 320:
                    apple_coordinates = (randrange(0, 640, 32), randrange(320, 640, 32))
                # Quadrant 4 - down and right
                elif apple_coordinates[1] > 320:
                    apple_coordinates = (randrange(0, 640, 32), randrange(0, 352, 32))
            snake.append((640, 640))
            snake_hitbox.append((640, 640))
            pygame.mixer.Sound.play(apple_sfx)
            score += 1
            score_text = score_font.render('SCORE: ' + str(score), True, (255, 255, 255))

        # Object rendering
        screen.fill((133, 52, 9))
        screen.blit(apple, apple_coordinates)
        screen.blit(score_text, score_text_rect)
        for pos in snake:
            screen.blit(snake_body, pos)
        screen.blit(snake_head, snake[0])

        # Update screen
        pygame.display.flip()
        game_clock.tick(10)

    else:
        # Game over screen
        pygame.display.flip()
        screen.fill((250, 0, 0))
        screen.blit(game_over_text, game_over_rect)
        screen.blit(score_text, score_text_rect)
        apple_coordinates = (800, 800)
        screen.blit(game_over_text, game_over_rect)
        screen.blit(score_text, score_text_rect)

pygame.quit()
