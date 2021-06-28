from config import *


class Hud(object):
    def __init__(self):
        self._life_sprite = pygame.image.load('../AsteroidsEquipe1/assets/player.png').convert_alpha()
        self._background = pygame.image.load('../AsteroidsEquipe1/assets/space1.png').convert_alpha()
        self._life_sprite = pygame.transform.scale(self._life_sprite, (30, 30))
        self._life = [(67, 50), (97, 50), (127, 50)]
        self._tam = len(self._life)
        self._point = 0
        self._p = 10000
        self._score_text = score_font.render(str(self._point), True, color_white)
        self._score_rect = self._score_text.get_rect()
        self._score_rect.center = (77, 25)
        self._credits = credits_font.render('ASTEROIDSTEAM1 POWERED BY ©2021 STEM-GAMES', True, color_white)

    @property
    def point(self):
        return self._point

    def adding_life(self, screen):
        if self._point >= self._p:
            self._life.append((self._life[-1][0] + 30, self._life[-1][1]))
            self._tam = len(self._life)
            self._p += 10000

        for i in range(0, self._tam):
            screen.blit(self._life_sprite, self._life[i])

    def display_score(self, screen):
        screen.blit(self._score_text, self._score_rect)
        screen.blit(self._credits, (385, 640))


hud = Hud()
