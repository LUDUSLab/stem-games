import pygame

pygame.init()

sw, sh = 800, 60

screen = pygame.display.set_mode((sw, sh))
pygame.display.set_caption("Asteroids")

color_black = (0, 0, 0)
color_white = (255, 255, 255)

game_on = True
game_clock = pygame.time.Clock()
