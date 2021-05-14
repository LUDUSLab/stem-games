from config import *
from abc import ABC, abstractmethod
import random


class Asteroids(ABC):

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def destroy(self):
        pass

    @abstractmethod
    def draw(self):
        pass


class BigAsteroids(Asteroids):

    def __init__(self, rank):
        self.w = 50 * rank
        self.h = 50 * rank

        self.ranPoint = random.choice([(random.randrange(0, sw - self.w), random.choice([-1 * self.h - 5, sh + 5])),
                                       (random.choice([-1 * self.w - 5, sw + 5]), random.randrange(0, sh - self.h))])

    def move(self):
        pass

    def destroy(self):
        pass

    def draw(self):
        pass


class MediumAsteroids(Asteroids):

    def move(self):
        pass

    def destroy(self):
        pass

    def draw(self):
        pass


class SmallAsteroids(Asteroids):

    def move(self):
        pass

    def destroy(self):
        pass

    def draw(self):
        pass
