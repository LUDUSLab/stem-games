import pygame
import config
from config import SQUARE_SIZE


class Cube(object):
    def __init__(self, start: tuple, color: tuple = (255, 0, 0)):
        self.pos: tuple = start
        self.dirnx = 1
        self.dirny = 0
        self.color = color

    def move(self, dirnx, dirny):
        self.dirnx = dirnx
        self.dirny = dirny
        self.pos = (self.pos[0] + self.dirnx, self.pos[1] + self.dirny)

    def draw(self, surface):
        i = self.pos[0]
        j = self.pos[1]
        pygame.draw.rect(surface, self.color,
                         (i * config.SQUARE_SIZE + 1, j * config.SQUARE_SIZE + 1,
                          config.SQUARE_SIZE - 2, config.SQUARE_SIZE - 2))


class Renderer(object):
    def __init__(self, pos: tuple, sprite):
        self.pos = pos
        self.sprite = sprite

    def blit(self):
        absolute_location = (self.pos[0] * SQUARE_SIZE, self.pos[1] * SQUARE_SIZE)
        config.window.screen.blit(self.sprite, absolute_location)
