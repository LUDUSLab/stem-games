import pygame


class Wall(object):
    def __init__(self, color: tuple = (200, 200, 200)):
        self.size = (40, 40)
        self.color = color

    def draw_wall(self, surface):
        # for 'y' coordinate
        for i in range(120, 1200, 40):
            pygame.draw.rect(surface, self.color, (i, 80) + self.size)
            pygame.draw.rect(surface, self.color, (i, 600) + self.size)

        # for 'x' coordinate
        for i in range(120, 600, 40):
            pygame.draw.rect(surface, self.color, (120, i) + self.size)
            pygame.draw.rect(surface, self.color, (1160, i) + self.size)


class Obstacles(Wall):
    def __init__(self, color):
        super().__init__(color)
        self.color = color

    def draw_obstacles(self, surface):
        # 1
        pygame.draw.rect(surface, self.color, (200, 200) + self.size)
        pygame.draw.rect(surface, self.color, (240, 200) + self.size)
        pygame.draw.rect(surface, self.color, (240, 160) + self.size)
        # 2
        pygame.draw.rect(surface, self.color, (360, 160) + self.size)
        pygame.draw.rect(surface, self.color, (360, 200) + self.size)
        # 3
        pygame.draw.rect(surface, self.color, (240, 400) + self.size)
        pygame.draw.rect(surface, self.color, (280, 400) + self.size)
        pygame.draw.rect(surface, self.color, (320, 400) + self.size)
        # 4
        pygame.draw.rect(surface, self.color, (200, 480) + self.size)
        pygame.draw.rect(surface, self.color, (240, 480) + self.size)
        pygame.draw.rect(surface, self.color, (240, 520) + self.size)
        # 5
        pygame.draw.rect(surface, self.color, (360, 480) + self.size)
        pygame.draw.rect(surface, self.color, (360, 520) + self.size)
        # 6
        pygame.draw.rect(surface, self.color, (480, 240) + self.size)
        pygame.draw.rect(surface, self.color, (520, 240) + self.size)
        pygame.draw.rect(surface, self.color, (560, 200) + self.size)
        pygame.draw.rect(surface, self.color, (560, 240) + self.size)
        pygame.draw.rect(surface, self.color, (560, 160) + self.size)
        # 7
        pygame.draw.rect(surface, self.color, (480, 440) + self.size)
        pygame.draw.rect(surface, self.color, (520, 440) + self.size)
        pygame.draw.rect(surface, self.color, (560, 440) + self.size)
        pygame.draw.rect(surface, self.color, (560, 480) + self.size)
        pygame.draw.rect(surface, self.color, (560, 520) + self.size)
        # 8
        pygame.draw.rect(surface, self.color, (760, 240) + self.size)
        pygame.draw.rect(surface, self.color, (800, 240) + self.size)
        pygame.draw.rect(surface, self.color, (720, 200) + self.size)
        pygame.draw.rect(surface, self.color, (720, 240) + self.size)
        pygame.draw.rect(surface, self.color, (720, 160) + self.size)
        # 9
        pygame.draw.rect(surface, self.color, (760, 440) + self.size)
        pygame.draw.rect(surface, self.color, (800, 440) + self.size)
        pygame.draw.rect(surface, self.color, (720, 440) + self.size)
        pygame.draw.rect(surface, self.color, (720, 480) + self.size)
        pygame.draw.rect(surface, self.color, (720, 520) + self.size)
        # 10
        pygame.draw.rect(surface, self.color, (920, 160) + self.size)
        pygame.draw.rect(surface, self.color, (920, 200) + self.size)
        # 11
        pygame.draw.rect(surface, self.color, (920, 480) + self.size)
        pygame.draw.rect(surface, self.color, (920, 520) + self.size)
        # 12
        pygame.draw.rect(surface, self.color, (1080, 200) + self.size)
        pygame.draw.rect(surface, self.color, (1040, 200) + self.size)
        pygame.draw.rect(surface, self.color, (1040, 160) + self.size)
        # 13
        pygame.draw.rect(surface, self.color, (1080, 480) + self.size)
        pygame.draw.rect(surface, self.color, (1040, 480) + self.size)
        pygame.draw.rect(surface, self.color, (1040, 520) + self.size)
        # 14
        pygame.draw.rect(surface, self.color, (1040, 400) + self.size)
        pygame.draw.rect(surface, self.color, (1000, 400) + self.size)
        pygame.draw.rect(surface, self.color, (960, 400) + self.size)
        # 15
        pygame.draw.rect(surface, self.color, (240, 280) + self.size)
        pygame.draw.rect(surface, self.color, (280, 280) + self.size)
        pygame.draw.rect(surface, self.color, (320, 280) + self.size)
        # 16
        pygame.draw.rect(surface, self.color, (1040, 280) + self.size)
        pygame.draw.rect(surface, self.color, (1000, 280) + self.size)
        pygame.draw.rect(surface, self.color, (960, 280) + self.size)
