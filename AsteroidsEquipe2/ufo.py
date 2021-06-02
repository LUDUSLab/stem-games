import pygame
from math import atan2, pi, cos, sin, radians

import config
import projectile
import gameobject
from random import uniform, randrange

class UFO(gameobject.GameObject):
    PROJECTILE_SPEED = 8

    def __init__(self, position, size, projectile_callback):
        self.size = size
        size_to_scale = {2: 1, 1: 0.5}
        self.create_projectile_callback = projectile_callback
        self.scale = size_to_scale[size]
        self.sprite_path = "./assets/ufo.png"
        self.sprite = pygame.transform.rotozoom(pygame.image.load(self.sprite_path).convert_alpha(), 0, self.scale)
        self.velx = 2.5/self.size if position.x == 0 else -2.5/self.size
        self.vely = 0
        self.moving_y = False
        self.score = 200 if self.size == 2 else 1000
        self.running_death_animation = False
        if self.size == 2:
            pygame.mixer.Channel(4).play(config.big_ufo_appears, loops=-1)
        elif self.size == 1:
            pygame.mixer.Channel(4).play(config.small_ufo_appears, loops=-1)
        super().__init__(position, self.sprite, pygame.Vector2(self.velx, self.vely))

    def shoot(self, ship_position=None):
        if self.size == 2 or ship_position is None:
            angle = radians(uniform(0, 360))
            projectile_velocity = pygame.Vector2(cos(angle), sin(angle)) * self.PROJECTILE_SPEED + self.velocity
        else:
            dx = self.position.x - ship_position.x
            dy = self.position.y - ship_position.y
            angle = atan2(-dy, -dx)
            angle %= 2*pi
            projectile_velocity = pygame.Vector2(cos(angle), sin(angle)) * self.PROJECTILE_SPEED + self.velocity
        bullet = projectile.Projectile(self.position, projectile_velocity)
        pygame.mixer.Channel(3).play(config.ship_shoot_sound)
        self.create_projectile_callback(bullet)

    def movey(self):
        self.velocity.y = randrange(-1, 2, 2)*self.velx
        self.moving_y = True
