import pygame
from random import uniform, randint
import gameobject


class Asteroid(gameobject.GameObject):

    def __init__(self, position, asteroid_callback, size=3):
        self.asteroid_callback = asteroid_callback
        self.size = size
        size_to_scale = {3: 1, 2: 0.7,1: 0.4}
        self.scale = size_to_scale[size]
        self.randomvisual = str(randint(1, 3))
        self.sprite_path = "./assets/asteroid_"+self.randomvisual+".png"
        self.sprite = pygame.transform.rotozoom(pygame.image.load(self.sprite_path).convert_alpha(), 0, self.scale)
        self.velx = uniform(-1.5, 1.5)
        self.vely = uniform(-1.5, 1.5)
        self.score = 20
        super().__init__(position, self.sprite, pygame.Vector2(self.velx, self.vely))

    def split(self):
        if self.size > 1:
            for _ in range(2):
                asteroid = Asteroid(self.position, self.asteroid_callback, self.size-1)
                if asteroid.size == 2:
                    asteroid.score = 50
                elif asteroid.size == 1:
                    asteroid.score = 100
                self.asteroid_callback(asteroid)
