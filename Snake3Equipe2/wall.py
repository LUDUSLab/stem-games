import pygame


class Wall(object):
    def __init__(self, color: tuple = (200, 200, 200)):
        self.size = (40, 40)
        self.color = color

    def draw_wall(self, surface):
        # for 'y' coordinate
        for i in range(0, 1280, 40):
            pygame.draw.rect(surface, self.color, (i, 80) + self.size)
            pygame.draw.rect(surface, self.color, (i, 680) + self.size)

        # for 'x' coordinate
        for i in range(80, 720, 40):
            pygame.draw.rect(surface, self.color, (0, i) + self.size)
            pygame.draw.rect(surface, self.color, (1240, i) + self.size)


class Obstacles(Wall):
    def __init__(self, color):
        super().__init__(color)
        self.color = color

    def draw_obstacles(self, surface):
        # 1
        pygame.draw.rect(surface, self.color, (40, 280) + self.size)
        pygame.draw.rect(surface, self.color, (80, 280) + self.size)
        # 2
        pygame.draw.rect(surface, self.color, (240, 120) + self.size)
        pygame.draw.rect(surface, self.color, (240, 160) + self.size)
        pygame.draw.rect(surface, self.color, (240, 200) + self.size)
        # 3
        pygame.draw.rect(surface, self.color, (640, 120) + self.size)
        pygame.draw.rect(surface, self.color, (640, 160) + self.size)
        pygame.draw.rect(surface, self.color, (640, 200) + self.size)
        # 4
        pygame.draw.rect(surface, self.color, (1000, 120) + self.size)
        pygame.draw.rect(surface, self.color, (1000, 160) + self.size)
        pygame.draw.rect(surface, self.color, (1000, 200) + self.size)
        # 5
        pygame.draw.rect(surface, self.color, (1200, 280) + self.size)
        pygame.draw.rect(surface, self.color, (1160, 280) + self.size)
        # 6
        pygame.draw.rect(surface, self.color, (760, 360) + self.size)
        pygame.draw.rect(surface, self.color, (800, 360) + self.size)
        pygame.draw.rect(surface, self.color, (840, 360) + self.size)
        # 7
        pygame.draw.rect(surface, self.color, (320, 320) + self.size)
        pygame.draw.rect(surface, self.color, (320, 360) + self.size)
        pygame.draw.rect(surface, self.color, (320, 400) + self.size)
        # 8
        pygame.draw.rect(surface, self.color, (40, 480) + self.size)
        pygame.draw.rect(surface, self.color, (80, 480) + self.size)
        # 9
        pygame.draw.rect(surface, self.color, (520, 440) + self.size)
        pygame.draw.rect(surface, self.color, (520, 480) + self.size)
        pygame.draw.rect(surface, self.color, (520, 520) + self.size)
        # 10
        pygame.draw.rect(surface, self.color, (320, 600) + self.size)
        pygame.draw.rect(surface, self.color, (320, 640) + self.size)
        pygame.draw.rect(surface, self.color, (320, 680) + self.size)
        # 11
        pygame.draw.rect(surface, self.color, (1200, 480) + self.size)
        pygame.draw.rect(surface, self.color, (1160, 480) + self.size)
        # 12
        pygame.draw.rect(surface, self.color, (880, 600) + self.size)
        pygame.draw.rect(surface, self.color, (880, 640) + self.size)
        pygame.draw.rect(surface, self.color, (880, 680) + self.size)
