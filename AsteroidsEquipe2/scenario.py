import asteroid
import config
import ship
import ufo
import pygame
from random import randrange

class Scenario:
    aux_time = 100
    min_asteroid_spawn_distance = 100
    min_ship_spawn_distance = 100
    ship_can_spawn = False

    def __init__(self, player):
        self.player = player
        self.asteroids_quantity = 4
        self.asteroids = []
        self.ufo_projectiles = []
        self.ship_projectiles = []
        self.ship = ship.Ship(self.ship_projectiles.append)
        self.ufo = None
        for _ in range(self.asteroids_quantity):
            while True:
                position = pygame.Vector2(randrange(config.window.size[0]), randrange(config.window.size[1]))
                if position.distance_to(self.ship.position) > self.min_asteroid_spawn_distance:
                    break
            self.asteroids.append(asteroid.Asteroid(position, self.asteroids.append))
        self.player_turn_text = config.Text("Player 1", 32)
        self.player_turn_text.pos = ((config.window.size[0] -
                                      self.player_turn_text.font.size(self.player_turn_text.message)[0]) / 2, 110)
        self.aux_movey_time = 120
        self.aux_projectile_time = 40

    def display(self):
        if self.aux_time > 0:
            self.player_turn_text.display()
            self.aux_time -= 1
        else:
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
            else:
                randy = randrange(0, 721)
                randx = randrange(0, 1281)
                size = 1 if randx < 20 else 2
                if randx == 0 or randx == 1280:
                    self.ufo = ufo.UFO(pygame.Vector2(randx, randy), size, self.ufo_projectiles.append)
            for ast in self.asteroids:
                ast.display()
                ast.move()
                if self.ufo is not None and ast.collides_with(self.ufo):
                    self.asteroids.remove(ast)
                    ast.split()
                    self.ufo = None
                    break
            for ast in self.asteroids:
                ast.display()
                ast.move()
                if self.ship is not None:
                    if not self.ship.running_death_animation:
                        if ast.collides_with(self.ship):
                            self.asteroids.remove(ast)
                            self.player.lives -= 1
                            self.ship.running_death_animation = True
                            ast.split()
                            self.player.score += ast.score
                            break
            if self.ship is None:
                for ast in self.asteroids:
                    if pygame.Vector2(config.middle).distance_to(ast.position) < self.min_ship_spawn_distance:
                        self.ship_can_spawn = False
                        break
                    else:
                        self.ship_can_spawn = True
                if self.ship_can_spawn:
                    self.ship = ship.Ship(self.ship_projectiles.append)

            if self.ship is not None:
                if self.ship.running_death_animation:
                    self.ship.death_animation()
                    if self.ship.death_animation_time <= 0:
                        self.ship.death_animation_time = 100
                        self.ship.running_death_animation = False
                        self.ship = None

            for projectile in self.ship_projectiles:
                projectile.display()
                projectile.move()
                projectile.time_alive -= 1.45
                if projectile.time_alive <= 0:
                    self.ship_projectiles.remove(projectile)
                if self.ufo is not None and projectile.collides_with(self.ufo):
                    self.player.score += self.ufo.score
                    self.ufo = None
                for ast in self.asteroids:
                    if ast.collides_with(projectile):
                        self.asteroids.remove(ast)
                        self.ship_projectiles.remove(projectile)
                        ast.split()
                        self.player.score += ast.score
                        break

            for projectile in self.ufo_projectiles:
                projectile.display()
                projectile.move()
                projectile.time_alive -= 1.45
                if projectile.time_alive <= 0:
                    self.ufo_projectiles.remove(projectile)
                for ast in self.asteroids:
                    if ast.collides_with(projectile):
                        self.asteroids.remove(ast)
                        self.ufo_projectiles.remove(projectile)
                        ast.split()
                        self.player.score += ast.score
                        break
            if self.ship is not None:
                self.ship.move()
                self.ship.display()
