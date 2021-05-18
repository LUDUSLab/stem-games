import pygame
from random import uniform, randint
import gameobject


class Asteroid(gameobject.GameObject):
    score = 20
    min_asteroid_spawn_distance = 250

    def __init__(self, position):
        self.randomvisual = str(randint(1, 3))
        self.sprite_path = "./assets/asteroid_"+self.randomvisual+".png"
        self.sprite = pygame.image.load(self.sprite_path).convert_alpha()
        self.velx = uniform(-1.5, 1.5)
        self.vely = uniform(-1.5, 1.5)
        super().__init__(position, self.sprite, pygame.Vector2(self.velx, self.vely))

    def explode(self):
        pass
