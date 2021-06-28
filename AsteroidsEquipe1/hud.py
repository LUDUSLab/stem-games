from config import *


class Hud(object):
    def init(self):
        self._image = pygame.image.load('../AsteroidsEquipe1/assets/player.png').convert_alpha()
        self._imageSize = pygame.transform.scale(self._image, (30, 30))

        self._position = [(67, 50), (97, 50), (127, 50)]
        self._size = len(self._position)

        self.point = 0
        self._max = 10000

        self._score_text = score_font.render(str(self.point), True, color_white)
        self._score_rect = self._score_text.get_rect()
        self._score_rect.center = (77, 25)

    def adding(self, screen):
        self._position.append((self._life[-1][0] + 30, self._life[-1][1]))

        self._size = len(self._position)

        self._max += 10000

    def delete(self):
        self._position.pop(self._size - 1)