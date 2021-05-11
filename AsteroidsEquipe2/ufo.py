import pygame
import config

class UFO:
    def __init__(self, vel: tuple):
        self.velx = vel[0]
        self.vely = vel[1]

    def shoot(self):
        pass

    def move(self):
        pass

    def display(self):
        pass

class BigUFO(UFO):
    sprite_path = "./assets/temporary_ufo.png"
    sprite = pygame.image.load(sprite_path).convert_alpha()
    score = 200

    def __init__(self, vel: tuple, pos=(0, config.window.size[1]/2)):
        super().__init__(vel)
        self.pos = pos

    def move(self):
        self.pos = (self.pos[0] + self.velx, self.pos[1] + self.vely)

    def shoot(self):
        pass

    def display(self):
        config.window.screen.blit(self.sprite, self.pos)
