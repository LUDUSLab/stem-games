import pygame
import config

class Cube(object):
    def __init__(self, start: tuple, color: tuple = (255, 0, 0)):
        self.pos = start
        self.dirnx = 1
        self.dirny = 0
        self.color = color

    def move(self, dirnx, dirny):
        self.dirnx = dirnx
        self.dirny = dirny
        self.pos = (self.pos[0] + self.dirnx, self.pos[1] + self.dirny)

    def draw(self, dist, surface, eyes=False):
        i = self.pos[0]
        j = self.pos[1]
        pygame.draw.rect(surface, self.color, (i * dist + 1, j * dist + 1, dist - 2, dist - 2))
        if eyes:
            centre = dist//2
            radius = 4
            circle_middle = (i*dist+centre-radius, j*dist+8)
            circle_middle2 = (i*dist + dist - radius*2, j*dist+8)
            color = config.COLOR_BLACK
            pygame.draw.circle(surface, color, circle_middle, radius)
            pygame.draw.circle(surface, color, circle_middle2, radius)