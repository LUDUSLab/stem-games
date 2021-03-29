import pygame
import arena


class Wall(object):
    def __init__(self, size: tuple = (40, 40), color: tuple = (200, 200, 200)):
        self.size = size
        self.color = color
        self._wall = pygame.Surface(self.size)
        self._wall.fill(self.color)

    def draw_wall(self, surface):
        surface.blit(self._wall, (0, 40))
        surface.blit(self._wall, (0, 680))
        surface.blit(self._wall, (1240, 40))
        surface.blit(self._wall, (1240, 680))
        for i in range(120, 1240, 40):
            surface.blit(self._wall, (i, 40))
            surface.blit(self._wall, (i, 680))

        for i in range(80, 680, 40):
            surface.blit(self._wall, (0, i))
            surface.blit(self._wall, (1240, i))


class Obstacles(Wall):
    def init(self):
        super(Obstacles, self).__init__()

    def draw_obstacles(self, surface):
        surface.blit(self._wall, (240, 240))
