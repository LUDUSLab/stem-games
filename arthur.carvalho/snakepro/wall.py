import pygame
from config import *


def wall_draw():
    wall_sprite = pygame.image.load('assets/wall_sprite.png')

    for c in range(0, 800, 32):
        screen.blit(wall_sprite, (c, 32))
        screen.blit(wall_sprite, (c, 608))

    for c in range(32, 640, 32):
        screen.blit(wall_sprite, (0, c))
        screen.blit(wall_sprite, (768, c))

