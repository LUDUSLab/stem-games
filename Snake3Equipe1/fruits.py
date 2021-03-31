import pygame
import random
import config


class Fruit:
    def __init__(self):
        self._pos = (640, 360)
        self._fruits = ["assets/apple_sprite.png","assets/orange_sprite.png","assets/banana_sprite.png",
                        "assets/grape_sprite.png"]
        self._fruit = ("assets/apple_sprite.png")

    @property
    def position(self):
        return self._pos

    def changep(self):
        self._pos = (random.randint(32, 1216), random.randint(64, 656))

    def draw(self):
        config.screen.blit(self._fruit, self._pos)

    def choose(self):
        vari = random.randint(0,20)
        if vari in [1,2,3,4,5,6,7,8,9,10]:
            self._fruit = ("assets/apple_sprite.png")
        elif vari in [11,12,13,14,15]:
            self._fruit = ("assets/orange_sprite.png")
        elif vari in [16,17,18,19]:
            self._fruit = ("assets/banana_sprite.png")
        elif vari in [20]:
            self._fruit = ("assets/grape_sprite.png")
