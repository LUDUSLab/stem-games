import pygame
import window
import game


class Wall(object):
    def __init__(self):
        self.size = (40, 40)
        self.color = (200, 200, 200)
        self._wall = pygame.Surface(self.size)
        self._wall.fill(self.color)

    def draw(self, surface):
        surface.blit(self._wall, (0, 32))
        surface.blit(self._wall, (0, 608))
        surface.blit(self._wall, (1248, 32))
        surface.blit(self._wall, (1248, 608))
        for i in range(32, 1248, 32):
            surface.blit(self._wall, (i, 32))
            surface.blit(self._wall, (i, 608))

        for i in range(64, 608, 32):
            surface.blit(self._wall, (0, i))
            surface.blit(self._wall, (1248, i))


class Obstacles(Wall):
    def __init__(self):
        super().__init__()
        self._obstacles_1 = self._wall


