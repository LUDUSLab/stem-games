import cube


class Fruit(object):
    def __init__(self, value: int, pos: tuple):
        self.pos = pos
        self.fruit = cube.Cube(self.pos, (0, 255, 0))
        self.value = value
