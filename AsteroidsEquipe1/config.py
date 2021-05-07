import pygame
import player
import renderer

pygame.init()
sw, sh = 800, 800
color_black = (0, 0, 0)
screen = pygame.display.set_mode((sw, sh))
pygame.display.set_caption("Asteroids")

game_on = True
game_clock = pygame.time.Clock()
while game_on:
    game_clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_on = False

pygame.quit()
