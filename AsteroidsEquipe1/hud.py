from config import *


class Hud(object):
    def __init__(self):
        self._image = pygame.image.load('../AsteroidsEquipe1/assets/player.png').convert_alpha()
        self._life_sprite = pygame.transform.scale(self._image, (30, 30))
        self._life = [(67, 50), (97, 50), (127, 50)]
        self._tam = len(self._life)
        self.point = 0
        self._p = 10000
        self._score_text = score_font.render(str(self.point), True, color_white)
        self._score_rect = self._score_text.get_rect()
        self._score_rect.center = (77, 25)

    def adding_life(self, screen):
        if self.point >= self._p:
            self._life.append((self._life[-1][0] + 30, self._life[-1][1]))
            self._tam = len(self._life)
            self._p += 10000

        for i in range(0, self._tam):
            screen.blit(self._life_sprite, self._life[i])
