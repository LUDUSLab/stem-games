import pygame
import config

class UFO:
    def __init__(self, score, vel):
        self.score = score
        self.vel = vel

    def shoot(self):
        pass

    def move(self):
        pass

    def display(self):
        pass

class BigUFO(UFO):
    sprite = pygame.image.load("./assets/temporary_ufo.png").convert_alpha()

    def __init__(self, score, vel, pos=(0, config.window.size[1]/2)):
        super().__init__(score, vel)
        self.pos = pos

    def move(self):
        self.pos = (self.pos[0] + self.vel, self.pos[1])

    def shoot(self):
        pass

    def display(self):
        config.window.screen.blit(self.sprite, self.pos)
