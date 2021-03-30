import pygame


class Wall(object):
    def __init__(self, color: tuple = (200, 200, 200)):
        self.size = (40, 40)
        self.color = color

    def draw_wall(self, surface):
        # for 'y' coordinate
        for i in range(120, 1200, 40):
            pygame.draw.rect(surface, self.color, (i, 120) + self.size)
            pygame.draw.rect(surface, self.color, (i, 600) + self.size)

        # for 'x' coordinate
        for i in range(120, 600, 40):
            pygame.draw.rect(surface, self.color, (120, i) + self.size)
            pygame.draw.rect(surface, self.color, (1160, i) + self.size)


class Obstacles(Wall):
    def init(self):
        super(Obstacles, self).__init__()

    # def draw_obstacles(self, surface):
        # surface.blit(self._wall, (240, 240))
