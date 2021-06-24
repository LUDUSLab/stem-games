import math
from config import *


class PlayerShip(object):
    def __init__(self):
        self.img = pygame.image.load("../AsteroidsEquipe1/assets/player.png").convert_alpha()
        self.w = self.img.get_width()
        self.h = self.img.get_height()
        self.x = sw // 2
        self.y = sh // 2
        self.angle = 0
        self.a = 0
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
        self.x += self.player_cos * self.a
        self.y -= self.player_sin * self.a
        self.rotate = pygame.transform.rotate(self.img, self.angle)
        self.rotateRect = self.rotate.get_rect()
        self.rotateRect.center = (self.x, self.y)
        self.player_cos = math.cos(math.radians(self.angle + 90))
        self.player_sin = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.player_cos * self.w // 2, self.y - self.player_sin * self.h // 2)

    def player_outside_screen(self):
        if self.x > sw + 50:
            self.x = 0
        elif self.x < -self.w:
            self.x = sw
        elif self.y < -50:
            self.y = sh
        elif self.y > sh + 50:
            self.y = 0

    def acceleration(self):
        if self.a < 5:
            self.a += 0.08

        else:
            self.a = 4

    def non_acceleration(self):
        if self.a > 0:
            self.a -= 0.08

        else:
            self.a = 0

    def destroy(self):
        self.x = sw // 2
        self.y = sh // 2

    def draw(self, screen):
        screen.blit(self.rotate, self.rotateRect)


player = PlayerShip()
