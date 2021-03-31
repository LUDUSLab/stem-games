import cube


class Wall(object):
    def __init__(self, color: tuple = (200, 200, 200)):
        self.wall = []
        self.color = color
        # for 'y' coordinate
        for i in range(32):
            for j in [2, 17]:
                self.wall.append(cube.Cube((i, j), self.color))

        # for 'x' coordinate
        for i in range(2, 18):
            for j in [0, 31]:
                self.wall.append(cube.Cube((j, i), self.color))

    def draw_wall(self, surface):
        for block in self.wall:
            block.draw(40, surface)


class Obstacles(Wall):
    def __init__(self, color):
        super().__init__(color)
        self.color = color
        self.obstacles = []
        # 1, 2, 3, 4
        for k in [1, 29]:
            for j in [7, 12]:
                for i in range(2):
                    self.obstacles.append(cube.Cube((k+i, j), self.color))
        # 5, 6, 7
        for j in [6, 16, 25]:
            for i in range(3):
                self.obstacles.append(cube.Cube((j, 3+i), self.color))
        # 8, 9
        for j in [8, 22]:
            for i in range(3):
                self.obstacles.append(cube.Cube((j, 15+i), self.color))
        # 10, 11
        aux = 8
        for i in range(6):
            self.obstacles.append(cube.Cube((aux, 8+i), self.color))
            if i == 2:
                aux = 13
        # 12
        for i in range(3):
            self.obstacles.append(cube.Cube((19+i, 9), self.color))

    def draw_obstacles(self, surface):
        for obstacle in self.obstacles:
            obstacle.draw(40, surface)
