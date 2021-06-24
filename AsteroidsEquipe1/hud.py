import pygame.image
import turtle
from config import *


class Hud(object):
    def __init__(self):
        self.colors = ['color_black', 'color_white']
        self.life_sprite = pygame.image.load('../AsteroidsEquipe1/assets/player.png').convert_alpha()
        self.background = pygame.image.load('../AsteroidsEquipe1/assets/space1.png').convert_alpha()
        self.life_sprite = pygame.transform.scale(self.life_sprite, (30, 30))
        self.life = [(67, 50), (97, 50), (127, 50)]
        self.point = 0
        self.score_text = score_font.render(str(self.point), True, color_white)
        self.score_rect = self.score_text.get_rect()
        self.score_rect.center = (77, 25)
        self.play = play_font.render('| COIN | PLAY', True, color_white)
        self.credits = credits_font.render('ASTEROIDSTEAM1 POWERED BY ©2021 STEM-GAMES', True, color_white)

    def display_life(self, screen):
        for i in self.life:
            screen.blit(self.life_sprite, i)
            if self.point == 10000:
                self.life.append((2000, 2000))

    def text_blink_effect(self):
        pass

    def display_score(self, screen):
        screen.blit(self.score_text, self.score_rect)
        screen.blit(self.credits, (385, 640))
        screen.blit(self.play, (525, 550))


hud = Hud()
