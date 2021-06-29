import pygame
import math
from config import color_white


class Bullet(object):

    def __init__(self, head, cos, sin):
        self.point = head
        self.x, self.y = self.point
        self.w, self.h = 4, 4
        self.c, self.s = cos, sin
        self.xv, self.yv = self.c * 10, self.s * 10

        self.rect = pygame.Surface((self.w, self.h))
        self.rect.fill(color_white)

    def move(self):
        self.x += self.xv
        self.y -= self.yv


class AlienBullet(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w = self.h = 4
        self.dx, self.dy = player.x - self.x, player.y - self.y
        self.dist = math.hypot(self.dx, self.dy)
        self.dx, self.dy = self.dx / self.dist, self.dy / self.dist
        self.xv = self.dx * 5
        self.yv = self.dy * 5

    def draw(self, win):
        pygame.draw.rect(win, (255, 255, 255), [self.x, self.y, self.w, self.h])
