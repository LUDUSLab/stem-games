import pygame
from random import uniform, randint

import config
import gameobject

class Asteroid(gameobject.GameObject):
    def __init__(self, position, asteroid_callback, size=3):
        self.asteroid_callback = asteroid_callback
        self.size = size
        size_to_scale = {3: 1, 2: 0.675,1: 0.35}
        self.scale = size_to_scale[size]
        self.randomvisual = str(randint(1, 3))
        self.sprite_path = "./assets/asteroid_"+self.randomvisual+".png"
        self.sprite = pygame.transform.rotozoom(pygame.image.load(self.sprite_path).convert_alpha(), 0, self.scale)
        self.velx = uniform(-4.5+self.size, 4.5-self.size)
        self.vely = uniform(-4.5+self.size, 4.5-self.size)
        self.score = 20
        self.explosion_sound = config.asteroid_explosion_sounds[3-self.size]
        super().__init__(position, self.sprite, pygame.Vector2(self.velx, self.vely))

    def split(self):
        pygame.mixer.Channel(2).play(self.explosion_sound)
        if self.size > 1:
            for _ in range(2):
                asteroid = Asteroid(self.position, self.asteroid_callback, self.size-1)
                if asteroid.size == 2:
                    asteroid.score = 50
                elif asteroid.size == 1:
                    asteroid.score = 100
                self.asteroid_callback(asteroid)
