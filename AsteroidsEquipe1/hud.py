import pygame.image
from config import *


class Hud(object):
    def __init__(self):
        self.colors = ['color_black', 'color_white']
        self.life_sprite = pygame.image.load('../AsteroidsEquipe1/assets/player.png').convert_alpha()
        self.background = pygame.image.load('../AsteroidsEquipe1/assets/space1.png').convert_alpha()
        self.life_sprite = pygame.transform.scale(self.life_sprite, (30, 30))
        self.life = [(67, 50), (97, 50), (127, 50)]
        self.tam = len(self.life)
        self.point = 9900
        self.p = 10000
        self.score_text = score_font.render(str(self.point), True, color_white)
        self.score_rect = self.score_text.get_rect()
        self.score_rect.center = (77, 25)
        self.play = play_font.render('| COIN | PLAY', True, color_white)
        self.credits = credits_font.render('ASTEROIDSTEAM1 POWERED BY ©2021 STEM-GAMES', True, color_white)

    def display_life(self, screen):
        if self.point >= self.p:
            self.p += 10000
            self.life.append((self.life[-1][0] + 30, 50))
        for i in range(0, self.tam):
            screen.blit(self.life_sprite, self.life[i])

    def display_score(self, screen):
        screen.blit(self.score_text, self.score_rect)
        screen.blit(self.credits, (385, 640))
        screen.blit(self.play, (525, 550))


hud = Hud()
