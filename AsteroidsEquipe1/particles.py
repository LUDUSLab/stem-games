import pygame
import math
from config import color_white
from abc import ABC, abstractmethod


class Factory(ABC):

    @abstractmethod
    def create(self, bullets, time, x, y, px, py):
        pass

    def destroy(self, bullet, position):
        pass


class FactoryBullet(Factory):

    def create(self, bullets, time, x, y, px, py):
        if (time % 200 == 0) or (time % 400 == 0):
            bullets.append(AlienBullet(x, y, px, py))

    def destroy(self, bullet, position):
        bullet.pop(position)


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
    def __init__(self, x, y, px, py):
        self.x = x
        self.y = y
        self.w = self.h = 4
        self.dx, self.dy = px - self.x, py - self.y
        self.dist = math.hypot(self.dx, self.dy)
        self.dx, self.dy = self.dx / self.dist, self.dy / self.dist
        self.xv = self.dx * 5
        self.yv = self.dy * 5

        self.rect = pygame.Surface((self.w, self.h))
        self.rect.fill(color_white)

    def move(self):
        self.x += self.xv
        self.y -= self.yv
