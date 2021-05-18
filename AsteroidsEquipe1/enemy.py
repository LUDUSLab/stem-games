from config import *
from abc import ABC, abstractmethod
import random


class EnemyShip(ABC):
    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def shoot(self):
        pass

    @abstractmethod
    def destroy(self):
        pass

    @abstractmethod
    def draw(self, screen):
        pass


class SmallEnemyShip(EnemyShip, ABC):
    def __init__(self):
        self.img = pygame.image.load("../AsteroidsEquipe1/assets/enemy_small.png")
        self.w = self.img.get_width()
        self.h = self.img.get_height()
        self.x, self.y = random.choice([(random.randrange(0, sw - self.w), random.choice([-1 * self.h - 5, sh + 5])),
                                       (random.choice([-1 * self.w - 5, sw + 5]), random.randrange(0, sh - self.h))])
        if self.x < sw // 2:
            self.x_dir = 1
        else:
            self.x_dir = -1
        if self.y < sh // 2:
            self.y_dir = 1
        else:
            self.y_dir = -1

    def move(self):
        self.x += self.x_dir * 2
        self.y += self.y_dir * 2

    def shoot(self):
        pass

    def destroy(self):
        pass

    def draw(self, screen):
        screen.blit(self.img, (self.x, self.y))


class BigEnemyShip(EnemyShip, ABC):
    def __init__(self):
        self.img = pygame.image.load("../AsteroidsEquipe1/assets/enemy_big.png")
        self.w = self.img.get_width()
        self.h = self.img.get_height()
        self.x, self.y = random.choice([(random.randrange(0, sw - self.w), random.choice([-1 * self.h - 5, sh + 5])),
                                       (random.choice([-1 * self.w - 5, sw + 5]), random.randrange(0, sh - self.h))])

        if self.x < sw // 2:
            self.x_dir = 1
        else:
            self.x_dir = -1
        if self.y < sh // 2:
            self.y_dir = 1
        else:
            self.y_dir = -1

    def move(self):
        self.x += self.x_dir * 2
        self.y += self.y_dir * 2

    def shoot(self):
        pass

    def destroy(self):
        pass

    def draw(self, screen):
        screen.blit(self.img, (self.x, self.y))
