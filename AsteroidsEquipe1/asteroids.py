from config import *
from abc import ABC, abstractmethod
from random import choice, randrange


class Factory(ABC):

    @abstractmethod
    def create(self):
        pass

    def crack(self, asteroid):
        pass

    @abstractmethod
    def destroy(self, position):
        pass


class FactoryAsteroids(Factory):

    def create(self):
        asteroids.append(BigAsteroids())

    def crack(self, asteroid):
        if asteroid.w == 64:
            asteroid_temporary1 = MediumAsteroids()
            asteroid_temporary2 = MediumAsteroids()

            asteroid_temporary1.x = asteroid_temporary2.x = asteroid.x
            asteroid_temporary1.y = asteroid_temporary2.y = asteroid.y

            asteroids.append(asteoridTemporary1)
            asteroids.append(asteoridTemporary2)

        elif asteroid.w == 32:
            asteroid_temporary1 = SmallAsteroids()
            asteroid_temporary2 = SmallAsteroids()

            asteroid_temporary1.x = asteroid_temporary2.x = asteroid.x
            asteroid_temporary1.y = asteroid_temporary2.y = asteroid.y

            asteroids.append(asteoridTemporary1)
            asteroids.append(asteoridTemporary2)

    def destroy(self, position):
        asteroids.pop(asteroids.index(position))


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
        self.w = self.h = 32

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
        self.w = self.h = 16

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
