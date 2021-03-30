import random
import cube


class Fruit(object):
    def __init__(self, value: int):
        self.fruit = cube.Cube((random.randrange(3, 28), random.randrange(3, 14)), (0, 255, 0))
        self.value = value
