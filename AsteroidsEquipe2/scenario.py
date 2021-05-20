import asteroid
import config
import ship
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
        self.projectiles = []
        self.ship = ship.Ship(self.projectiles.append)
        for _ in range(self.asteroids_quantity):
            while True:
                position = pygame.Vector2(randrange(config.window.size[0]), randrange(config.window.size[1]))
                if position.distance_to(self.ship.position) > self.min_asteroid_spawn_distance:
                    break
            self.asteroids.append(asteroid.Asteroid(position, self.asteroids.append))
        self.player_turn_text = config.Text("Player 1", 32)
        self.player_turn_text.pos = ((config.window.size[0] -
                                      self.player_turn_text.font.size(self.player_turn_text.message)[0]) / 2, 110)

    def display(self):
        if self.aux_time > 0:
            self.player_turn_text.display()
            self.aux_time -= 1
        else:
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
                    self.ship = ship.Ship(self.projectiles.append)

            if self.ship is not None:
                if self.ship.running_death_animation:
                    self.ship.death_animation()
                    if self.ship.death_animation_time <= 0:
                        self.ship.death_animation_time = 100
                        self.ship.running_death_animation = False
                        self.ship = None

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
                        self.player.score += ast.score
                        break
            if self.ship is not None:
                self.ship.move()
                self.ship.display()
