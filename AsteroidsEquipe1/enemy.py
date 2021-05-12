import pygame
import random


class EnemyShip(object):
    def __init__(self):
        self.img = pygame.image.load("../ronald.boadana/snakepro/assets/ronald.boadana_snakehead2.png")
        self.w = self.img.get_width()
        self.h = self.img.get_height()
        self.x = random.randrange(1480, 1500)
        self.y = random.randrange(155, 955)

    def move(self):
        if (self.x != 500) and (self.y != 500):
            self.x -= 10
            self.y -= 10
            print(self.x, self.y)

    def draw_enemy(self, screen):
        screen.blit(self.img, (self.x, self.y))


class SmallEnemyShip(EnemyShip):
    pass


class BigEnemyShip(EnemyShip):
    pass


enemy = EnemyShip()
pygame.init()
sw, sh = 1440, 1080
color_black = (0, 0, 0)
color_white = (255, 255, 255)
screen = pygame.display.set_mode((sw, sh))
pygame.display.set_caption("Asteroids")
game_on = True
game_over = False
game_clock = pygame.time.Clock()
while game_on:
    game_clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_on = False
            enemy.move()

    screen.fill(color_black)
    enemy.draw_enemy(screen)
    pygame.display.update()

pygame.quit()