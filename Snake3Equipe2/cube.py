import pygame
import config


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

    def draw(self, surface, eyes=False):
        i = self.pos[0]
        j = self.pos[1]
        pygame.draw.rect(surface, self.color, (
            i * config.SQUARE_SIZE + 1, j * config.SQUARE_SIZE + 1, config.SQUARE_SIZE - 2, config.SQUARE_SIZE - 2
        ))
        if eyes:
            centre = config.SQUARE_SIZE//2
            radius = 4
            circle_middle = (i*config.SQUARE_SIZE+centre-radius, j*config.SQUARE_SIZE+8)
            circle_middle2 = (i*config.SQUARE_SIZE + config.SQUARE_SIZE - radius*2, j*config.SQUARE_SIZE+8)
            color = config.COLOR_BLACK
            pygame.draw.circle(surface, color, circle_middle, radius)
            pygame.draw.circle(surface, color, circle_middle2, radius)