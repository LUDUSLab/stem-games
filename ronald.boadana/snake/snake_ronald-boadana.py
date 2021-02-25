import pygame
import random

# Powered by Ronald Boadana

pygame.init()

max_score = 10
player_score = 0

color_black = (0, 0, 0)
color_white = (255, 255, 255)
screen_size = (600, 600)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Snake v0.5')

# drawing snake
snake = pygame.image.load('../snake/assets/ronald.boadana_snakehead.png')
snake_x, snake_y = 300, 300
snake_pos = (snake_x, snake_y)

# drawing apple
apple = pygame.image.load('../snake/assets/ronald.boadana_apple.png')
apple_pos = (random.randint(0, 590)//10 * 10, random.randint(0, 590)//10 * 10)

# score text
score_font = pygame.font.Font('../snake/assets/PressStart2P.ttf', 30)
score_text = score_font.render('0', True, color_white, color_black)
score_text_rect = score_text.get_rect()
score_text_rect.center = (300, 25)

# defeat text
defeat_font = pygame.font.Font('../snake/assets/PressStart2P.ttf', 60)
defeat_text = defeat_font.render('GAME OVER', True, color_white, color_black)
defeat_text_rect = score_text.get_rect()
defeat_text_rect.center = (350, 350)

# conditions to snake can move
direction_x, direction_y = 10, 10

game_on = True
game_clock = pygame.time.Clock()
while game_on:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        # mapping keys
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                snake_y -= direction_y
            if event.key == pygame.K_s:
                snake_y += direction_y
            if event.key == pygame.K_a:
                snake_x -= direction_x
            if event.key == pygame.K_d:
                snake_x += direction_x

    # victory condition
    if player_score < max_score:
        if snake_x == apple_pos:
            player_score += 1
            apple_pos = (random.randint(0, 590)//10*10, random.randint(0, 590)//10*10)
            print(apple_pos)
            print(snake_x)
            print(snake_y)

        score_text = score_font.render(str(player_score), True, color_white, color_black)

    else:
        if (snake_x == 0 or snake_y == 0) and (snake_x == 600 or snake_y == 600):
            screen.blit(defeat_text, defeat_text_rect)

    screen.blit(score_text, score_text_rect)
    screen.blit(snake, (snake_x, snake_y))
    screen.blit(apple, apple_pos)

    pygame.display.update()
    # updating screen
    screen.fill(color_black)
    game_clock.tick(90)
