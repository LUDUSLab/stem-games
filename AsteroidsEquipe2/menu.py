import pygame

import config
import ufo
import hud
import asteroid
from random import randrange

class Menu:
    start_game = False
    header = config.Text("1 COIN 1 PLAY", 32)
    footer = config.Text("2 0 2 1  STEM GAMES", 16)
    start_txt = config.Text("PUSH START", 32, blink=True)
    header.pos = ((config.window.size[0] - header.font.size(header.message)[0])/2, 580)
    footer.pos = ((config.window.size[0] - footer.font.size(footer.message)[0])/2, 695)
    ufo = None
    hud = hud.HUD(None)
    projectiles = []
    asteroids = []
    aux_projectile_time = 40
    aux_movey_time = 120
    for _ in range(4):
        asteroids.append(asteroid.Asteroid(pygame.Vector2(randrange(config.window.size[0]), randrange(
                config.window.size[1])), asteroids.append))

    def check_game_enter(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.start_game = True

    def display(self):
        self.header.display()
        self.footer.display()
        self.start_txt.display()
        self.hud.menu_display()
        if self.ufo is not None:
            self.ufo.display()
            self.ufo.move()
            aux_rand = randrange(400)
            if aux_rand == 10 and not self.ufo.moving_y:
                self.ufo.movey()
            if self.ufo.moving_y:
                self.aux_movey_time -= 1
                if self.aux_movey_time <= 0:
                    self.aux_movey_time = 100
                    self.ufo.velocity.y = 0
                    self.ufo.moving_y = False

            self.aux_projectile_time -= 1
            if self.aux_projectile_time <= 0:
                self.ufo.shoot()
                self.aux_projectile_time = 40
            if self.ufo.position.x > 1300 or self.ufo.position.x < -20:
                self.ufo = None
            for projectile in self.projectiles:
                projectile.display()
                projectile.move()
                projectile.time_alive -= 1.45
                if projectile.time_alive <= 0:
                    self.projectiles.remove(projectile)
            for projectile in self.projectiles:
                for ast in self.asteroids:
                    if ast.collides_with(projectile):
                        self.asteroids.remove(ast)
                        self.projectiles.remove(projectile)
                        ast.split()
                        break
        else:
            randy = randrange(0, 721)
            randx = randrange(0, 1281)
            size = 1 if randx < 20 else 2
            if 0 <= randx <= 3 or 1277 <= randx <= 1280:
                self.ufo = ufo.UFO(pygame.Vector2(randx, randy), size, self.projectiles.append)
        for ast in self.asteroids:
            ast.display()
            ast.move()
