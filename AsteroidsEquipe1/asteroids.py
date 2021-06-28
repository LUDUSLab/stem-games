from config import *
from abc import ABC, abstractmethod
from random import choice, randrange


class Factory(ABC):

    @abstractmethod
    def create(self, asteroids, time):
        pass

    def crack(self, asteroid, position):
        pass

    @abstractmethod
    def destroy(self, asteroids, position):
        pass


class FactoryAsteroids(Factory):

    def create(self, asteroids, time):
        if time % 65 == 0:
            asteroids.append(BigAsteroids())

    def crack(self, asteroids, position):
        if position.w == 64:
            asteroid_temporary1 = MediumAsteroids()
            asteroid_temporary2 = MediumAsteroids()

            asteroid_temporary1.x = asteroid_temporary2.x = position.x
            asteroid_temporary1.y = asteroid_temporary2.y = position.y

            asteroids.append(asteroid_temporary1)
            asteroids.append(asteroid_temporary2)

        elif position.w == 32:
            asteroid_temporary1 = SmallAsteroids()
            asteroid_temporary2 = SmallAsteroids()

            asteroid_temporary1.x = asteroid_temporary2.x = position.x
            asteroid_temporary1.y = asteroid_temporary2.y = position.y

            asteroids.append(asteroid_temporary1)
            asteroids.append(asteroid_temporary2)

    def destroy(self, asteroids, position):
        asteroids.pop(asteroids.index(position))


class Asteroids(ABC):

    @abstractmethod
    def move(self):
        pass


class BigAsteroids(Asteroids):

    def __init__(self):
        self.w = self.h = 64
        self._image = pygame.image.load("assets/asteroid_big.png").convert_alpha()

        self._speed_x = choice([1, 2, 3])
        self._speed_y = choice([1, 2, 3])

        self._ranPoint = choice([(randrange(0, sw - self.w), choice([-1 * self.h - 5, sh + 5])),
                                (choice([-1 * self.w - 5, sw + 5]), randrange(0, sh - self.h))])

        self.x, self.y = self._ranPoint

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


class MediumAsteroids(Asteroids):

    def __init__(self):
        self.w = self.h = 32

        self._image = pygame.image.load("assets/asteroid_medium.png").convert_alpha()

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
        self.w = self.h = 16

        self._image = pygame.image.load("assets/asteroid_small.png").convert_alpha()

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
