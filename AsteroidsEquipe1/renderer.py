import pygame.display
from config import *
# from main import *
from hud import *
from player import *
from asteroids import *
from enemy import *
from particles import *


class Renderer(object):
    def __init__(self):
        self.playership = playership.PlayerShip()
        self.hud = hud.Hud()
        self.player_missile = PlayerMissile()
        self.big_asteroids = BigAsteroids()
        self.medium_asteroids = MediumAsteroids()
        self.small_asteroids = SmallAsteroids()
        self.small_enemy = SmallEnemyShip()
        self.big_enemy = BigEnemyShip()

    def display(self):
        self.hud.display_score(screen)
        self.hud.display_life(screen)
        self.playership.draw(screen)
        self.player_missile.draw(screen)
        self.big_asteroids.draw(screen)
        self.medium_asteroids.draw(screen)
        self.small_asteroids.draw(screen)
        self.small_enemy.draw(screen)
        self.big_enemy.draw(screen)
        pygame.display.update()


renderer = Renderer()
