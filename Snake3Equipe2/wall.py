from game_test_snake import *


class Wall(object):
    def __init__(self, size: tuple = (40, 40), color: tuple = (200, 200, 200)):
        self.size = size
        self.color = color
        self.wall = pygame.Surface(size)

    def draw_wall_borders(self, wall):
        for i in range(120, 1280, 40):
            self.screen.blit(self.wall, (i, 0))
            self.screen.blit(self.wall, (i, 1240))

        for i in range(40, 720, 40):
            self.screen.blit(self.wall, (0, i))
            self.screen.blit(self.wall, (680, i))


class Obstacles(Wall):
    def __init__(self, size, color, wall):
        super().__init__(size, color)
        self.obstacle_1 = self.wall
        self.obstacle_2 = self.wall

    def draw_obstacles(self):
        screen.blit(self.obstacle_1, (120, 120))