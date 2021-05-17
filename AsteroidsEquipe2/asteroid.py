import pygame
import config
from random import uniform, randint
import gameobject


class Asteroid(gameobject.GameObject):
    def __init__(self, position):
        self.randomvisual = str(randint(1, 3))
        self.sprite_path = "./assets/asteroid_"+self.randomvisual+".png"
        self.sprite = pygame.image.load(self.sprite_path).convert_alpha()
        super().__init__(position, self.sprite, (0, 0))

    def move(self):
        pass

    def explode(self):
        pass

class BigAsteroid(Asteroid):
    score = 20

    def __init__(self, position):
        super().__init__(position)
        self.velx = uniform(-1.5, 1.5)
        self.vely = uniform(-1.5, 1.5)
        self.pos = (randint(0, config.window.size[0]), randint(0, config.window.size[1]))

    def move(self):
        new_pos = (self.pos[0] + self.velx, self.pos[1] + self.vely)
        self.pos = self.wrap_position(new_pos)

    def display(self):
        config.window.screen.blit(self.sprite, self.pos)
