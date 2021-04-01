import pygame
from config import screen


class Wall:
    def __init__(self):
        self._wall_1 = pygame.image.load('assets/wall_sprite1.png')
        self._wall_2 = pygame.image.load('assets/wall_sprite2.png')
        self._wall_corner1 = pygame.image.load('assets/wall_corner1.png')
        self._wall_corner2 = pygame.image.load('assets/wall_corner2.png')
        self._wall_corner3 = pygame.image.load('assets/wall_corner3.png')
        self._wall_corner4 = pygame.image.load('assets/wall_corner4.png')
        self._wall_obstacle = pygame.image.load('assets/obstacle.png')

    def draw_wall(self):
        screen.blit(self._wall_corner1, (0, 32))
        screen.blit(self._wall_corner2, (1248, 32))
        screen.blit(self._wall_corner3, (0, 608))
        screen.blit(self._wall_corner4, (1248, 608))

        screen.blit(self._wall_obstacle, (192, 192))
        screen.blit(self._wall_obstacle, (192, 448))
        screen.blit(self._wall_obstacle, (640, 192))
        screen.blit(self._wall_obstacle, (640, 448))
        screen.blit(self._wall_obstacle, (1056, 192))
        screen.blit(self._wall_obstacle, (1056, 448))

        for c in range(32, 1248, 32):
            screen.blit(self._wall_1, (c, 32))
            screen.blit(self._wall_1, (c, 608))

        for c in range(64, 608, 32):
            screen.blit(self._wall_2, (0, c))
            screen.blit(self._wall_2, (1248, c))