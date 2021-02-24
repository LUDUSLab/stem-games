import pygame
import random
# Powered by Ronald Boadana

pygame.init()

color_black = (255, 255, 255)
screen_size = (600, 600)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Snake v0.1')

snake = pygame.image.load('C:/Users/bh_ro/Documents/STEM/stem-games/mypong2/assets/ronald.boadana_ball.png')
snake_x, snake_y = 0, 0

apple = pygame.image.load('C:/Users/bh_ro/Documents/STEM/stem-games/mypong2/assets/ronald.boadana_ball.png')
apple_pos = (random.randrange(0, 590), random.randrange(0, 590))

game_on = True
while game_on:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    pygame.display.update()
