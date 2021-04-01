from random import randint, randrange
import pygame
from config import screen


class Fruit:
    def __init__(self):
        self._fruits = ['assets/apple_sprite.png',
                        'assets/orange_sprite.png',
                        'assets/banana_sprite.png',
                        'assets/grape_sprite.png']

        self._fruit = pygame.image.load('assets/apple_sprite.png')
        self._type = 0

        self._position = (640, 352)

    @property
    def position(self):
        return self._position

    @property
    def type(self):
        return self._type

    def change_position(self):
        self._position = (randrange(64, 1216, 32), randrange(64, 576, 32))

        if self._position in [(192, 192), (192, 448), (640, 192), (640, 448), (1056, 192), (1056, 448)]:
            self._position = (randrange(64, 1216, 32), randrange(64, 576, 32))

    def draw_fruit(self):
        screen.blit(self._fruit, self._position)

    def choose_fruit(self):
        type_fruit = randint(0, 20)

        if type_fruit in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
            self._fruit = pygame.image.load('assets/apple_sprite.png')
            self._type = 0

        elif type_fruit in [11, 12, 13, 14, 15]:
            self._fruit = pygame.image.load('assets/orange_sprite.png')
            self._type = 1

        elif type_fruit in [16, 17, 18, 19]:
            self._fruit = pygame.image.load('assets/banana_sprite.png')
            self._type = 2

        elif type_fruit in [20]:
            self._fruit = pygame.image.load('assets/grape_sprite.png')
            self._type = 3