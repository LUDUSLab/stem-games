from config import *
from asteroids import *
from player import *
from enemy import *
from hud import *
from particles import *
from renderer import *


class GameAsteroids(object):

    __ON = True
    __run = True
    __time = 0
    __keys = pygame.key.get_pressed()

    def __init__(self):
        self.asteroids = []
        self.bullets = []
        self.smallAlien = []
        self.bigAlien = []

        self.player = PlayerShip()

        self.factoryAsteroids = FactoryAsteroids()
        self.factoryAliens = FactoryAliens()

        self.hud = Hud()

        self.renderer = Renderer()

    def game(self):

        pygame.init()

        while self.__ON:

            self.__keys = pygame.key.get_pressed()

            if self.__run:
                if self.__keys[pygame.K_a]:
                    self.player.player_left()

                if self.__keys[pygame.K_d]:
                    self.player.player_right()

                if self.__keys[pygame.K_w]:
                    self.player.acceleration()
                    self.player.move_up()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.__ON = False

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            self.bullets.append(PlayerMissile(self.player.head, self.player.cos, self.player.sin))
                            shoot_sound.play()

                game_clock.tick(60)

                self.__time += 1

                self.factoryAsteroids.create(self.asteroids, self.__time)
                self.factoryAliens.create(self.smallAlien, self.bigAlien, self.__time)

                for index, alien in enumerate(self.smallAlien):
                    if (self.player.x - self.player.w // 2 <= alien.x <= self.player.x + self.player.w // 2) or (
                            self.player.x + self.player.w // 2 >= alien.x + alien.w >= self.player.x - self.player.w // 2):
                        if (self.player.y - self.player.h // 2 <= alien.y <= self.player.y + self.player.h // 2) or (
                                self.player.y - self.player.h // 2 <= alien.y + alien.h <= self.player.y + self.player.h // 2):
                            self.factoryAliens.destroy(self.smallAlien, index)
                            self.player.destroy()
                            break

                    for bullets in self.bullets:
                        if (alien.x <= bullets.x <= alien.x + alien.w) or alien.x <= bullets.x + bullets.w <= alien.x + alien.w:
                            if (alien.y <= bullets.y <= alien.y + alien.h) or alien.y <= bullets.y + bullets.h <= alien.y + alien.h:
                                self.factoryAliens.destroy(self.smallAlien, index)
                                self.bullets.pop(self.bullets.index(bullets))
                                player_ship_explosion_sound.play()
                                break

                for index, alien in enumerate(self.bigAlien):
                    if (self.player.x - self.player.w // 2 <= alien.x <= self.player.x + self.player.w // 2) or (
                            self.player.x + self.player.w // 2 >= alien.x + alien.w >= self.player.x - self.player.w // 2):
                        if (self.player.y - self.player.h // 2 <= alien.y <= self.player.y + self.player.h // 2) or (
                                self.player.y - self.player.h // 2 <= alien.y + alien.h <= self.player.y + self.player.h // 2):
                            self.factoryAliens.destroy(self.bigAlien, index)
                            self.player.destroy()
                            break

                    for bullets in self.bullets:
                        if (alien.x <= bullets.x <= alien.x + alien.w) or alien.x <= bullets.x + bullets.w <= alien.x + alien.w:
                            if (alien.y <= bullets.y <= alien.y + alien.h) or alien.y <= bullets.y + bullets.h <= alien.y + alien.h:
                                self.factoryAliens.destroy(self.bigAlien, index)
                                self.bullets.pop(self.bullets.index(bullets))
                                player_ship_explosion_sound.play()
                                break

                for asteroid in self.asteroids:
                    if (self.player.x - self.player.w // 2 <= asteroid.x <= self.player.x + self.player.w // 2) or (
                            self.player.x + self.player.w // 2 >= asteroid.x + asteroid.w >= self.player.x - self.player.w // 2):
                        if (self.player.y - self.player.h // 2 <= asteroid.y <= self.player.y + self.player.h // 2) or (
                                self.player.y - self.player.h // 2 <= asteroid.y + asteroid.h <= self.player.y + self.player.h // 2):
                            self.factoryAsteroids.destroy(self.asteroids, asteroid)
                            self.player.destroy()
                            break

                    # bullet collision
                    for bullets in self.bullets:
                        if (asteroid.x <= bullets.x <= asteroid.x + asteroid.w) or asteroid.x <= bullets.x + bullets.w <= asteroid.x + asteroid.w:
                            if (asteroid.y <= bullets.y <= asteroid.y + asteroid.h) or asteroid.y <= bullets.y + bullets.h <= asteroid.y + asteroid.h:

                                self.factoryAsteroids.crack(self.asteroids, asteroid)

                                self.factoryAsteroids.destroy(self.asteroids, asteroid)
                                self.bullets.pop(self.bullets.index(bullets))
                                break

                for index in self.asteroids:
                    index.move()
                for index in self.bullets:
                    index.move()
                for index in self.smallAlien:
                    index.move()
                for index in self.bigAlien:
                    index.move()

                self.player.player_outside_screen()

                self.renderer.display(self.asteroids,
                                      self.bullets,
                                      self.smallAlien,
                                      self.bigAlien,
                                      self.player)

        pygame.quit()

    def collision(self):
        pass

    def moves(self):
        pass


game = GameAsteroids()
game.game()
