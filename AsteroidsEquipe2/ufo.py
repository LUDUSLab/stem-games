import pygame
import gameobject


class UFO(gameobject.GameObject):
    def __init__(self, position, size):
        self.size = size
        size_to_scale = {2: 1, 1: 0.5}
        self.scale = size_to_scale[size]
        self.sprite_path = "./assets/ufo.png"
        self.sprite = pygame.transform.rotozoom(pygame.image.load(self.sprite_path).convert_alpha(), 0, self.scale)
        self.velx = 2.2/self.size if position.x == 0 else -2.2/self.size
        self.vely = 0
        super().__init__(position, self.sprite, pygame.Vector2(self.velx, self.vely))

    def shoot(self):
        pass
