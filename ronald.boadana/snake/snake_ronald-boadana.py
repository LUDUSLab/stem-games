import pygame
import random
# Powered by Ronald Boadana

pygame.init()

color_black = (0, 0, 0)
screen_size = (600, 600)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Snake v0.2')

snake = pygame.image.load('C:/Users/bh_ro/Documents/STEM/stem-games/mypong2/assets/ronald.boadana_ball.png')
snake_x, snake_y = 300, 300

apple = pygame.image.load('C:/Users/bh_ro/Documents/STEM/stem-games/mypong2/assets/ronald.boadana_ball.png')
apple_pos = (random.randrange(0, 590), random.randrange(0, 590))

# conditions to snake can move
direction_x, direction_y = 7, 7

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

    screen.blit(snake, (snake_x, snake_y))
    screen.blit(apple, apple_pos)
    pygame.display.update()
    # updating screen
    screen.fill(color_black)
    game_clock.tick(90)
