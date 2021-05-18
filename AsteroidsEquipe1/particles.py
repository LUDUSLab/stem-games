import player
from config import *
from player import playership
import math


class PlayerMissile(object):
    def __init__(self):
        self.point = playership.head
        self.x, self.y = self.point
        self.w, self.h = 4, 4
        self.c, self.s = playership.player_cos, playership.player_sin
        self.xv, self.yv = self.c * 10, self.s * 10

    def move(self):
        self.x += self.xv
        self.y -= self.yv

    def draw(self, screen):
        pygame.draw.rect(screen, color_white, [self.x, self.y, self.w, self.h])


class EnemyMissile(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w = 4
        self.h = 4
        self.dx, self.dy = player.x - self.x, player.y - self.y
        self.dist = math.hypot(self.dx, self.dy)
        self.dx /= self.dist
        self.dy /= self.dist

    def move(self):
        self.xv += self.dx * 5
        self.yv -= self.dy * 5

    def draw(self, screen):
        pygame.draw.rect(screen, color_white, [self.x, self.y, self.w, self.h])
