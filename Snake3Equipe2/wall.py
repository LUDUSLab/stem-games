import pygame


class Wall(object):
    def __init__(self, color: tuple = (200, 200, 200)):
        self.size = (40, 40)
        self.color = color

    def draw_wall(self, surface):
        for i in range(120, 1240, 40):
            pygame.draw.rect(surface, self.color, (i, 40) + self.size)
            pygame.draw.rect(surface, self.color, (0, 680) + self.size)

        for i in range(80, 680, 40):
            pygame.draw.rect(surface, self.color, (0, i) + self.size)
            pygame.draw.rect(surface, self.color, (1240, i) + self.size)


class Obstacles(Wall):
    def init(self):
        super(Obstacles, self).__init__()

    # def draw_obstacles(self, surface):
        # surface.blit(self._wall, (240, 240))
