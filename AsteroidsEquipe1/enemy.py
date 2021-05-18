from config import *
import random


class EnemyShip(object):
    def __init__(self):
        self.img = pygame.image.load("../ronald.boadana/snakepro/assets/ronald.boadana_snakehead2.png")
        self.w = self.img.get_width()
        self.h = self.img.get_height()
        self.x, self.y = random.choice([(random.randrange(0, sw - self.w), random.choice([-1 * self.h - 5, sh + 5])),
                                       (random.choice([-1 * self.w - 5, sw + 5]), random.randrange(0, sh - self.h))])
        self.x_dir = 0
        self.y_dir = 0
        self.xv = 0
        self.yv = 0

    def move(self):
        if self.x < sw // 2:
            self.x_dir = 1
        else:
            self.x_dir = -1
        if self.y < sh // 2:
            self.y_dir = 1
        else:
            self.y_dir = -1
        self.xv = self.x_dir * 2
        self.yv = self.y_dir * 2

    def draw(self, screen):
        screen.blit(self.img, (self.x, self.y))


class SmallEnemyShip(EnemyShip):
    pass


class BigEnemyShip(EnemyShip):
    pass


enemyship = EnemyShip()
