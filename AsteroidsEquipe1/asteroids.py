from config import *
from abc import ABC, abstractmethod
from random import choice, randrange


class Asteroids(ABC):

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def destroy(self):
        pass

    @abstractmethod
    def draw(self, screen):
        pass


class BigAsteroids(Asteroids):

    def __init__(self):
        self._w = 64
        self._h = 64

        self._speed_x = choice([1, 2, 3])
        self._speed_y = choice([1, 2, 3])

        self.ranPoint = choice([(randrange(0, sw - self._w), choice([-1 * self._h - 5, sh + 5])),
                                (choice([-1 * self._w - 5, sw + 5]), randrange(0, sh - self._h))])

        self._x, self._y = self.ranPoint

        if self._x < sw // 2:
            self.dir_x = 1

        else:
            self.dir_x = -1

        if self._y < sh // 2:
            self.dir_y = 1

        else:
            self.dir_y = -1

        self._asteroids = [pygame.color.Color('white'), (self._x, self._y, self._w, self._h)]


    def move(self):
        self._x += self.dir_x * self._speed_x
        self._y += self.dir_y * self._speed_y

        self._asteroids = [pygame.color.Color('white'), (self._x, self._y, self._w, self._h)]

    def destroy(self):
        pass

    def draw(self, screen):
        pygame.draw.rect(screen, self._asteroids[0], self._asteroids[1])


big_asteroids = BigAsteroids()


class MediumAsteroids(Asteroids):

    def __init__(self):
        self._w = 32
        self._h = 32

        self._speed_x = choice([1, 2, 3])
        self._speed_y = choice([1, 2, 3])

        self.ranPoint = choice([(randrange(0, sw - self._w), choice([-1 * self._h - 5, sh + 5])),
                                (choice([-1 * self._w - 5, sw + 5]), randrange(0, sh - self._h))])

        self._x, self._y = self.ranPoint

        if self._x < sw // 2:
            self.dir_x = 1

        else:
            self.dir_x = -1

        if self._y < sh // 2:
            self.dir_y = 1

        else:
            self.dir_y = -1

        self._asteroids = [pygame.color.Color('white'), (self._x, self._y, self._w, self._h)]

    def move(self):
        self._x += self.dir_x * self._speed_x
        self._y += self.dir_y * self._speed_y

        self._asteroids = [pygame.color.Color('white'), (self._x, self._y, self._w, self._h)]

    def destroy(self):
        pass

    def draw(self, screen):
        pygame.draw.rect(screen, self._asteroids[0], self._asteroids[1])


medium_asteroids = MediumAsteroids()


class SmallAsteroids(Asteroids):

    def __init__(self):
        self._w = 16
        self._h = 16

        self._speed_x = choice([1, 2, 3])
        self._speed_y = choice([1, 2, 3])

        self.ranPoint = choice([(randrange(0, sw - self._w), choice([-1 * self._h - 5, sh + 5])),
                                (choice([-1 * self._w - 5, sw + 5]), randrange(0, sh - self._h))])

        self._x, self._y = self.ranPoint

        if self._x < sw // 2:
            self.dir_x = 1

        else:
            self.dir_x = -1

        if self._y < sh // 2:
            self.dir_y = 1

        else:
            self.dir_y = -1

        self._asteroids = [pygame.color.Color('white'), (self._x, self._y, self._w, self._h)]

    def move(self):
        self._x += self.dir_x * self._speed_x
        self._y += self.dir_y * self._speed_y

        self._asteroids = [pygame.color.Color('white'), (self._x, self._y, self._w, self._h)]

    def destroy(self):
        pass

    def draw(self, screen):
        pygame.draw.rect(screen, self._asteroids[0], self._asteroids[1])

small_asteroids = SmallAsteroids()
