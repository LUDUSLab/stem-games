import cube
import pygame

wall_sprite = pygame.image.load('assets/Walls.png')


class Wall(object):
    def __init__(self, color: tuple = (200, 200, 200)):
        self.wall = []
        self.color = color
        self.sprite = wall_sprite

        # for 'y' coordinate
        for i in range(32):
            for j in [2, 17]:
                self.wall.append(cube.Renderer((i, j), self.sprite))

        # for 'x' coordinate
        for i in range(2, 18):
            for j in [0, 31]:
                self.wall.append(cube.Renderer((j, i), self.sprite))

    def draw_wall(self):
        for block in self.wall:
            block.blit()


# manages walls inside the arena
class Obstacles(object):
    def __init__(self):
        self.sprite = wall_sprite
        self.obstacles = []

        # 1, 2, 3, 4
        for k in [1, 29]:
            for j in [7, 12]:
                for i in range(2):
                    self.obstacles.append(cube.Renderer((k+i, j), self.sprite))
        # 5, 6, 7
        for j in [6, 16, 25]:
            for i in range(3):
                self.obstacles.append(cube.Renderer((j, 3+i), self.sprite))
        # 8, 9
        for j in [8, 22]:
            for i in range(3):
                self.obstacles.append(cube.Renderer((j, 15+i), self.sprite))
        # 10, 11
        aux = 8
        for i in range(6):
            self.obstacles.append(cube.Renderer((aux, 8+i), self.sprite))
            if i == 2:
                aux = 13
        # 12
        for i in range(3):
            self.obstacles.append(cube.Renderer((19+i, 9), self.sprite))

    def draw_obstacles(self):
        for obstacle in self.obstacles:
            obstacle.blit()
