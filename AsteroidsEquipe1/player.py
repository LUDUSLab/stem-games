import math
from config import *
from hud import *


class Player(object):
    def __init__(self):
        self.img = pygame.image.load("../AsteroidsEquipe1/assets/player.png").convert_alpha()
        self.w = self.img.get_width()
        self.h = self.img.get_height()
        self.x = sw // 2
        self.y = sh // 2
        self.angle = 0
        self.rotate = pygame.transform.rotate(self.img, self.angle)
        self.rotateRect = self.rotate.get_rect()
        self.rotateRect.center = (self.x, self.y)
        self.cos = math.cos(math.radians(self.angle + 90))
        self.sin = math.sin(math.radians(self.angle + 90))

        self.dx = self.cos
        self.dy = self.sin

        self.head = (self.x + self.cos * self.w // 2, self.y - self.sin * self.h // 2)

    def left(self):
        self.angle += 10
        self.rotate = pygame.transform.rotate(self.img, self.angle)
        self.rotateRect = self.rotate.get_rect()
        self.rotateRect.center = (self.x, self.y)
        self.cos = math.cos(math.radians(self.angle + 90))
        self.sin = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cos * self.w // 2, self.y - self.sin * self.h // 2)

    def right(self):
        self.angle -= 10
        self.rotate = pygame.transform.rotate(self.img, self.angle)
        self.rotateRect = self.rotate.get_rect()
        self.rotateRect.center = (self.x, self.y)
        self.cos = math.cos(math.radians(self.angle + 90))
        self.sin = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cos * self.w // 2, self.y - self.sin * self.h // 2)

    def forward(self):
        self.x += self.dx * 0.1
        self.y -= self.dy * 0.1
        self.rotate = pygame.transform.rotate(self.img, self.angle)
        self.rotateRect = self.rotate.get_rect()
        self.rotateRect.center = (self.x, self.y)
        self.cos = math.cos(math.radians(self.angle + 90))
        self.sin = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cos * self.w // 2, self.y - self.sin * self.h // 2)

    def acceleration(self):
        self.dx += self.cos
        self.dy += self.sin

    def outside(self):
        if self.x > sw + 50:
            self.x = 0
        elif self.x < -self.w:
            self.x = sw
        elif self.y < -50:
            self.y = sh
        elif self.y > sh + 50:
            self.y = 0

    def destroy(self):
        self.x = sw // 2
        self.y = sh // 2
        self.angle = 0
