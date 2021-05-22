import gameobject
import pygame

class Projectile(gameobject.GameObject):
    def __init__(self, position, velocity):
        self.time_alive = 80
        self.sprite_path = "./assets/projectile.png"
        self.sprite = pygame.image.load(self.sprite_path)
        super().__init__(position, self.sprite, velocity)
