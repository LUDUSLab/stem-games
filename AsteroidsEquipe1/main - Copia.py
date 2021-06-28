from config import *
from asteroids import *
from player import *
from enemy import *
from hud import *
from particles import *
from renderer import *


class GameAsteroids(object):

    __ON = True
    __time = 0

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
            game_clock.tick(60)

            self.__time += 1

            self.factoryAsteroids.create(self.asteroids, self.__time)
            self.factoryAliens.create(self.smallAlien, self.bigAlien, self.__time)

            for i, asteroid in enumerate(self.smallAlien):
                for bullets in self.bullets:
                    if (asteroid.x <= bullets.x <= asteroid.x + asteroid.w) or asteroid.x <= bullets.x + bullets.w <= asteroid.x + asteroid.w:
                        if (asteroid.y <= bullets.y <= asteroid.y + asteroid.h) or asteroid.y <= bullets.y + bullets.h <= asteroid.y + asteroid.h:
                            self.smallAlien.pop(i)
                            player_ship_explosion_sound.play()
                            self.hud._point += 1000
                            break

            for i, asteroid in enumerate(self.bigAlien):
                for bullets in self.bullets:
                    if (asteroid.x <= bullets.x <= asteroid.x + asteroid.w) or asteroid.x <= bullets.x + bullets.w <= asteroid.x + asteroid.w:
                        if (asteroid.y <= bullets.y <= asteroid.y + asteroid.h) or asteroid.y <= bullets.y + bullets.h <= asteroid.y + asteroid.h:
                            self.bigAlien.pop(i)
                            player_ship_explosion_sound.play()
                            hud._point += 200
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

            for i in self.asteroids:
                i.move()
            for i in self.bullets:
                i.move()
            for i in self.smallAlien:
                i.move()
            for i in self.bigAlien:
                i.move()

            hud.score_text = score_font.render(str(hud._point), True, color_white)

            if not game_over:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_a]:
                    self.player.player_left()
                if keys[pygame.K_d]:
                    self.player.player_right()
                if keys[pygame.K_w]:
                    self.player.acceleration()
                    self.player.move_up()

                self.player.player_outside_screen()

            for event in pygame.event.get():
                # background_sound.play()
                if event.type == pygame.QUIT:
                    self.__ON = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.__ON = False
                    if event.key == pygame.K_SPACE:
                        if not game_over:
                            self.bullets.append(PlayerMissile(self.player.head, self.player.cos, self.player.sin))
                            shoot_sound.play()
                            # enemy_missile.append(EnemyMissile())

            screen.blit(hud._background, (0, 0))

            for i in self.bullets:
                i.draw(screen)
            for i in self.asteroids:
                i.draw(screen)
            for i in self.smallAlien:
                i.draw(screen)
            for i in self.bigAlien:
                i.draw(screen)

            self.player.draw(screen)
            self.hud.adding_life(screen)
            self.hud.display_score(screen)

            pygame.display.update()

        pygame.quit()

    @staticmethod
    def collision():
        pass


game = GameAsteroids()
game.game()
