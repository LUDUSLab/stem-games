import pygame
import config

class Ship:
    def __init__(self):
        self.sprite_path = "./assets/ship.png"
        self.sprite = pygame.image.load(self.sprite_path).convert_alpha()
        self.pos = (config.window.size[0]/2, config.window.size[1]/2)

    def display(self):
        config.window.screen.blit(self.sprite, self.pos)
