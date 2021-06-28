import pygame
from config import sw, sh
from abc import ABC, abstractmethod
import random


class Factory(ABC):

    @abstractmethod
    def create(self, small, big, time):
        pass

    @abstractmethod
    def destroy(self, alien, position):
        pass


class FactoryAliens(Factory):

    def create(self, small, big, time):
        if time % 200 == 0:
            big.append(BigAlien())

        if time % 400 == 0:
            small.append(SmallAlien())

    def destroy(self, alien, position):
        alien.pop(position)


class AlienShip(ABC):
    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def shoot(self):
        pass


class SmallAlien(AlienShip):
    def __init__(self):
        self.img = pygame.image.load("../AsteroidsEquipe1/assets/enemy_small.png").convert_alpha()
        self.img = pygame.transform.scale(self.img, [27, 27])
        self.w = self.img.get_width()
        self.h = self.img.get_height()
        self.x, self.y = random.choice([(random.randrange(0, sw - self.w), random.choice([-1 * self.h - 5, sh + 5])),
                                       (random.choice([-1 * self.w - 5, sw + 5]), random.randrange(0, sh - self.h))])
        if self.x < sw // 2:
            self.x_dir = 1
        else:
            self.x_dir = -1

    def move(self):
        self.x += self.x_dir

    def shoot(self):
        pass


class BigAlien(AlienShip):
    def __init__(self):
        self.img = pygame.image.load("../AsteroidsEquipe1/assets/enemy_big.png").convert_alpha()
        self.img = pygame.transform.scale(self.img, [64, 64])
        self.w = self.img.get_width()
        self.h = self.img.get_height()
        self.x, self.y = random.choice([(random.randrange(0, sw - self.w), random.choice([-1 * self.h - 5, sh + 5])),
                                       (random.choice([-1 * self.w - 5, sw + 5]), random.randrange(0, sh - self.h))])

        if self.x < sw // 2:
            self.x_dir = 1
        else:
            self.x_dir = -1

    def move(self):
        self.x += self.x_dir * 2

    def shoot(self):
        pass
