from config import *
from abc import ABC, abstractmethod
from random import choice, randrange


class FactoryAsteroids(ABC):
    @abstractmethod
    def create(self):
        pass

    @abstractmethod
    def destroy(self):
        pass


class Factory(FactoryAsteroids):
    @abstractmethod
    def create(self):
        pass

    def destroy(self):
        pass


class Asteroids(ABC):

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def draw(self, screen):
        pass


class BigAsteroids(Asteroids):

    def __init__(self):
        self.w = self.h = 64
        self._image = pygame.image.load("assets/asteroid_big.png")

        self._speed_x = choice([1, 2, 3])
        self._speed_y = choice([1, 2, 3])

        self.ranPoint = choice([(randrange(0, sw - self.w), choice([-1 * self.h - 5, sh + 5])),
                                (choice([-1 * self.w - 5, sw + 5]), randrange(0, sh - self.h))])

        self.x, self.y = self.ranPoint

        if self.x < sw // 2:
            self.dir_x = 1

        else:
            self.dir_x = -1

        if self.y < sh // 2:
            self.dir_y = 1

        else:
            self.dir_y = -1

    def move(self):
        self.x += self.dir_x * self._speed_x
        self.y += self.dir_y * self._speed_y

    def draw(self, screen):
        screen.blit(self._image, (self.x, self.y))


class MediumAsteroids(Asteroids):

    def __init__(self):
        self.w = 32
        self.h = 32
        self._image = pygame.image.load("assets/asteroid_medium.png")

        self._speed_x = choice([1, 2, 3])
        self._speed_y = choice([1, 2, 3])

        self.ranPoint = choice([(randrange(0, sw - self.w), choice([-1 * self.h - 5, sh + 5])),
                                (choice([-1 * self.w - 5, sw + 5]), randrange(0, sh - self.h))])

        self.x, self.y = self.ranPoint

        if self.x < sw // 2:
            self.dir_x = 1

        else:
            self.dir_x = -1

        if self.y < sh // 2:
            self.dir_y = 1

        else:
            self.dir_y = -1

    def move(self):
        self.x += self.dir_x * self._speed_x
        self.y += self.dir_y * self._speed_y

    def draw(self, screen):
        screen.blit(self._image, (self.x, self.y))


class SmallAsteroids(Asteroids):

    def __init__(self):
        self.w = 16
        self.h = 16
        self._image = pygame.image.load("assets/asteroid_small.png")

        self._speed_x = choice([1, 2, 3])
        self._speed_y = choice([1, 2, 3])

        self.ranPoint = choice([(randrange(0, sw - self.w), choice([-1 * self.h - 5, sh + 5])),
                                (choice([-1 * self.w - 5, sw + 5]), randrange(0, sh - self.h))])

        self.x, self.y = self.ranPoint

        if self.x < sw // 2:
            self.dir_x = 1

        else:
            self.dir_x = -1

        if self.y < sh // 2:
            self.dir_y = 1

        else:
            self.dir_y = -1

    def move(self):
        self.x += self.dir_x * self._speed_x
        self.y += self.dir_y * self._speed_y

    def draw(self, screen):
        screen.blit(self._image, (self.x, self.y))
