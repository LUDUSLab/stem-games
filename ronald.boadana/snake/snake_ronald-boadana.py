import pygame
import random

# Powered by Ronald Boadana

pygame.init()

color_white = (0, 0, 0)
color_black = (255, 255, 255)
screen_size = (600, 600)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Snake v0.2')

snake = pygame.image.load('../snake/assets/ronald.boadana_snakehead.png')
snake_x, snake_y = 300, 300
snake_pos = (snake_x, snake_y)

apple = pygame.image.load('../snake/assets/ronald.boadana_apple.png')
apple_pos = (random.randrange(0, 590), random.randrange(0, 590))

# score text
score_font = pygame.font.Font('../assets/PressStart2P.ttf', 44)
score_text = score_font.render('0', True, color_white, color_black)
score_text_rect = score_text.get_rect()
score_text_rect.center = (680, 50)

# defeat text
defeat_font = pygame.font.Font('../assets/PressStart2P.ttf', 100)
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

        if (snake_x == 0) or 600 and (snake_y == 0 or 600)
    screen.blit(snake, (snake_x, snake_y))
    screen.blit(apple, apple_pos)
    pygame.display.update()
    # updating screen
    screen.fill(color_black)
    game_clock.tick(90)
