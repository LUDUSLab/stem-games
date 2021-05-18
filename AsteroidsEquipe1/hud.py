import pygame.image
from config import *


class Hud(object):
    def __init__(self):
        self.life_sprite = pygame.image.load("../AsteroidsEquipe1/assets/player.png")
        self.life_sprite = pygame.transform.scale(self.life_sprite, (30, 30))
        self.life = [(67, 50), (97, 50), (127, 50)]
        self.score = font.render('0000', True, color_white, color_black)
        self.score_rect = self.score.get_rect()
        self.score_rect.center = (100, 25)
        self.live = 0

        self.score = font.render('' + str(self.live), True, color_white, color_black)

    def display_life(self, screen):
        for i in self.life:
            screen.blit(self.life_sprite, i)

    def display_score(self, screen):
        screen.blit(self.score, self.score_rect)

hud = Hud()
