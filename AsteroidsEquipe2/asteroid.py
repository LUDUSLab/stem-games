import pygame.image
from pygame.math import Vector2
import config
from random import uniform, randint

screen_size = config.window.size

class Asteroid:
    def __init__(self):
        self.randomvisual = str(randint(1, 3))
        self.sprite_path = "./assets/asteroid_"+self.randomvisual+".png"
        self.sprite = pygame.image.load(self.sprite_path).convert_alpha()

    @staticmethod
    def wrap_position(pos):
        x, y = pos
        w, h = screen_size
        return Vector2(x % w, y % h)

    def move(self):
        pass

    def explode(self):
        pass

class BigAsteroid(Asteroid):
    score = 20

    def __init__(self):
        super().__init__()
        self.velx = uniform(-1.5, 1.5)
        self.vely = uniform(-1.5, 1.5)
        self.pos = (randint(0, screen_size[0]), randint(0, screen_size[1]))

    def move(self):
        new_pos = (self.pos[0] + self.velx, self.pos[1] + self.vely)
        self.pos = self.wrap_position(new_pos)

    def display(self):
        config.window.screen.blit(self.sprite, self.pos)
