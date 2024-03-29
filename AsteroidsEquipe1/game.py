import pygame
from config import *
from asteroids import *
from player import *
from enemy import *
from hud import *
from particles import *
from renderer import *
from operator import itemgetter


class GameAsteroids(object):
    __ON = True
    __start = True
    __score = False

    __time = 0
    __keys = pygame.key.get_pressed()

    __text = ""

    __scoreBoard = []
    __scoreBoardSorted = __scoreBoard

    def __init__(self):
        self.asteroids = []
        self.bullets = []
        self.smallAlien = []
        self.bigAlien = []
        self.alienBullets = []

        self.player = Player()

        self.factoryAsteroids = FactoryAsteroids()
        self.factoryAliens = FactoryAliens()
        self.factoryBullets = FactoryBullet()

        self.hud = Hud()

        self.renderer = Renderer()

    def game(self):

        pygame.init()

        while self.__start:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                    if event.key == pygame.K_RETURN:
                        self.__start = False

            self.renderer.start()

        while self.__ON:
            game_clock.tick(60)

            self.__keys = pygame.key.get_pressed()

            self.hud.size = len(self.hud.position)

            if self.hud.size >= 1:
                if self.__keys[pygame.K_a]:
                    self.player.left()

                if self.__keys[pygame.K_d]:
                    self.player.right()

                if self.__keys[pygame.K_w]:
                    self.player.acceleration()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.__ON = False

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            self.bullets.append(Bullet(self.player.head, self.player.cos, self.player.sin))
                            shootSound.play()

                        if event.key == pygame.K_ESCAPE:
                            pygame.quit()

                if self.hud.point >= self.hud.max:
                    self.hud.adding()

                if self.hud.highest_score > self.hud.point:
                    self.hud.highest_score = self.hud.point

                self.__time += 1

                self.factoryAsteroids.create(self.asteroids, self.__time)
                self.factoryAliens.create(self.smallAlien, self.bigAlien, self.__time)

                GameAsteroids.moves(self)
                GameAsteroids.collision(self)

                self.renderer.display(self.asteroids,
                                      self.bullets,
                                      self.alienBullets,
                                      self.smallAlien,
                                      self.bigAlien,
                                      self.player,
                                      self.hud.point,
                                      self.hud.highest_score,
                                      self.hud.position)

            else:
                if not self.__score:

                    for event in pygame.event.get():

                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_ESCAPE:
                                pygame.quit()

                            if event.key == pygame.K_RETURN:
                                self.__scoreBoard.append({"name": self.__text, "point": self.hud.point})
                                self.__scoreBoardSorted = \
                                    sorted(self.__scoreBoard, key=itemgetter("point"), reverse=True)

                                self.__score = True

                            if event.key == pygame.K_BACKSPACE:
                                if len(self.__text) > 0:
                                    self.__text = self.__text[:-1]

                            else:
                                self.__text += event.unicode

                    self.renderer.game_over(self.hud.point,
                                            self.hud.highest_score,
                                            self.__text)

                else:
                    for event in pygame.event.get():

                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_ESCAPE:
                                pygame.quit()

                            if event.key == pygame.K_RETURN:
                                self.__score = False

                                GameAsteroids.reset(self)

                    self.renderer.score(self.__scoreBoardSorted)

    def collision(self):
        for index, alien in enumerate(self.bigAlien):
            self.factoryBullets.create(self.alienBullets,
                                       self.__time,
                                       alien.x + alien.w // 2,
                                       alien.y + alien.h // 2,
                                       self.player.x,
                                       self.player.y)

            if (self.player.x - self.player.w // 2 <= alien.x <= self.player.x + self.player.w // 2) or (
                    self.player.x + self.player.w // 2 >=
                    alien.x + alien.w >= self.player.x - self.player.w // 2):
                if (self.player.y - self.player.h // 2 <= alien.y <= self.player.y + self.player.h // 2) or (
                        self.player.y - self.player.h // 2 <= alien.y + alien.h <=
                        self.player.y + self.player.h // 2):
                    self.player.destroy()

                    self.factoryAliens.destroy(self.bigAlien, index)

                    self.hud.delete()

                    shipDestruction.play()
                    break

            for bullets in self.bullets:
                if (alien.x <= bullets.x <= alien.x + alien.w) or \
                        alien.x <= bullets.x + bullets.w <= alien.x + alien.w:
                    if (alien.y <= bullets.y <= alien.y + alien.h) or \
                            alien.y <= bullets.y + bullets.h <= alien.y + alien.h:
                        self.factoryAliens.destroy(self.bigAlien, index)

                        self.bullets.pop(self.bullets.index(bullets))

                        self.hud.point += 250

                        shipDestruction.play()
                        break

        for index, alien in enumerate(self.smallAlien):
            self.factoryBullets.create(self.alienBullets,
                                       self.__time,
                                       alien.x + alien.w // 2,
                                       alien.y + alien.h // 2,
                                       self.player.x,
                                       self.player.y)

            if (self.player.x - self.player.w // 2 <= alien.x <= self.player.x + self.player.w // 2) or \
                    (self.player.x + self.player.w // 2 >= alien.x + alien.w >= self.player.x - self.player.w // 2):
                if (self.player.y - self.player.h // 2 <= alien.y <= self.player.y + self.player.h // 2) or \
                        (self.player.y - self.player.h // 2 <= alien.y + alien.h <= self.player.y + self.player.h // 2):
                    self.player.destroy()

                    self.factoryAliens.destroy(self.smallAlien, index)

                    self.hud.delete()

                    shipDestruction.play()
                    break

            for bullets in self.bullets:
                if (alien.x <= bullets.x <= alien.x + alien.w) or \
                        alien.x <= bullets.x + bullets.w <= alien.x + alien.w:
                    if (alien.y <= bullets.y <= alien.y + alien.h) or \
                            alien.y <= bullets.y + bullets.h <= alien.y + alien.h:
                        self.factoryAliens.destroy(self.smallAlien, index)

                        self.bullets.pop(self.bullets.index(bullets))

                        self.hud.point += 500

                        shipDestruction.play()
                        break

        for index, bullet in enumerate(self.alienBullets):
            if (bullet.x >= self.player.x - self.player.w // 2) \
                    and (bullet.x <= self.player.x + self.player.w // 2) or \
                    (bullet.x + bullet.w >= self.player.x - self.player.w // 2) and (
                    bullet.x + bullet.w <= self.player.x + self.player.w // 2):
                if (bullet.y >= self.player.y - self.player.h // 2) and (
                        bullet.y <= self.player.y + self.player.h // 2) or \
                        (bullet.y + bullet.h >= self.player.y - self.player.h // 2) and (
                        bullet.y + bullet.h <= self.player.y + self.player.h // 2):
                    self.alienBullets.pop(index)

                    self.hud.delete()
                    self.player.destroy()

                    shipDestruction.play()
                    break

        for asteroid in self.asteroids:
            if (self.player.x - self.player.w // 2 <= asteroid.x <= self.player.x + self.player.w // 2) or \
                    (self.player.x + self.player.w // 2 >= asteroid.x + asteroid.w
                     >= self.player.x - self.player.w // 2):
                if (self.player.y - self.player.h // 2
                    <= asteroid.y <= self.player.y + self.player.h // 2) or (
                        self.player.y - self.player.h // 2 <= asteroid.y + asteroid.h
                        <= self.player.y + self.player.h // 2):
                    self.player.destroy()

                    self.factoryAsteroids.crack(self.asteroids, asteroid)
                    self.factoryAsteroids.destroy(self.asteroids, asteroid)

                    self.hud.delete()

                    shipDestruction.play()
                    asteroidsDestruction.play()
                    break

            for bullets in self.bullets:
                if (asteroid.x <= bullets.x <= asteroid.x + asteroid.w) or \
                        asteroid.x <= bullets.x + bullets.w <= asteroid.x + asteroid.w:
                    if (asteroid.y <= bullets.y <= asteroid.y + asteroid.h) or \
                            asteroid.y <= bullets.y + bullets.h <= asteroid.y + asteroid.h:

                        self.factoryAsteroids.destroy(self.asteroids, asteroid)
                        self.factoryAsteroids.crack(self.asteroids, asteroid)

                        self.bullets.pop(self.bullets.index(bullets))

                        if asteroid.w == 64:
                            self.hud.point += 50

                        elif asteroid.w == 32:
                            self.hud.point += 100

                        elif asteroid.w == 16:
                            self.hud.point += 150

                        asteroidsDestruction.play()
                        break

    def moves(self):

        for asteroid in self.asteroids:
            asteroid.move()

        for bullet in self.bullets:
            bullet.move()

        for alienBullet in self.alienBullets:
            alienBullet.move()

        for alien in self.smallAlien:
            alien.move()

        for alien in self.bigAlien:
            alien.move()

        self.player.forward()

        self.player.outside()

    def reset(self):
        self.asteroids = []
        self.bullets = []
        self.smallAlien = []
        self.bigAlien = []
        self.alienBullets = []

        self.player = Player()

        self.factoryAsteroids = FactoryAsteroids()
        self.factoryAliens = FactoryAliens()

        self.hud = Hud()
