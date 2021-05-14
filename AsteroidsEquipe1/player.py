import pygame
import math
from config import *


class PlayerShip(object):
    def __init__(self):
        self.img = pygame.image.load("../ronald.boadana/snakepro/assets/ronald.boadana_snakehead2.png")
        self.w = self.img.get_width()
        self.h = self.img.get_height()
        self.x = sw // 2
        self.y = sh // 2
        self.angle = 0
        self.rotate = pygame.transform.rotate(self.img, self.angle)
        self.rotateRect = self.rotate.get_rect()
        self.rotateRect.center = (self.x, self.y)
        self.player_cos = math.cos(math.radians(self.angle + 90))
        self.player_sin = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.player_cos * self.w // 2, self.y - self.player_sin * self.h // 2)

    def player_left(self):
        self.angle += 5
        self.rotate = pygame.transform.rotate(self.img, self.angle)
        self.rotateRect = self.rotate.get_rect()
        self.rotateRect.center = (self.x, self.y)
        self.player_cos = math.cos(math.radians(self.angle + 90))
        self.player_sin = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.player_cos * self.w // 2, self.y - self.player_sin * self.h // 2)

    def player_right(self):
        self.angle -= 5
        self.rotate = pygame.transform.rotate(self.img, self.angle)
        self.rotateRect = self.rotate.get_rect()
        self.rotateRect.center = (self.x, self.y)
        self.player_cos = math.cos(math.radians(self.angle + 90))
        self.player_sin = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.player_cos * self.w // 2, self.y - self.player_sin * self.h // 2)

    def move_up(self):
        self.x += self.player_cos * 6
        self.y -= self.player_sin * 6
        self.rotate = pygame.transform.rotate(self.img, self.angle)
        self.rotateRect = self.rotate.get_rect()
        self.rotateRect.center = (self.x, self.y)
        self.player_cos = math.cos(math.radians(self.angle + 90))
        self.player_sin = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.player_cos * self.w // 2, self.y - self.player_sin * self.h // 2)
        print(self.x, self.y)

    def draw_playership(self, screen):
        # screen.blit(self.img, [self.x, self.y, self.w, self.h])
        screen.blit(self.rotate, self.rotateRect)


class Missile(object):
    def __init__(self):
        self.point = playership.head
        self.x, self.y = self.point
        self.w, self.h = 4, 4
        self.c, self.s = playership.player_cos, playership.player_sin
        self.xv, self.yv = self.c * 10, self.s * 10

    def missile_move(self):
        self.x += self.xv
        self.y -= self.yv

    def draw_missile(self, screen):
        pygame.draw.rect(screen, color_white, [self.x, self.y, self.w, self.h])


missile = Missile()
playership = PlayerShip()
player_missile = []

