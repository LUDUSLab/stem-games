import asteroid
import config
import ship
import pygame
from random import randrange

class Scenario:
    aux_time = 100
    min_asteroid_spawn_distance = 200

    def __init__(self):
        self.ship = ship.Ship()
        self.asteroids_quantity = 4
        self.asteroids = []
        for _ in range(self.asteroids_quantity):
            while True:
                position = pygame.Vector2(randrange(config.window.size[0]), randrange(config.window.size[1]))
                if position.distance_to(self.ship.position) > self.min_asteroid_spawn_distance:
                    break
            self.asteroids.append(asteroid.Asteroid(position))
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
            self.ship.display()
            self.ship.move()