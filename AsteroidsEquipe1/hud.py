from config import *


class Hud(object):

    def __init__(self):
        self._image = pygame.image.load('../AsteroidsEquipe1/assets/player.png').convert_alpha()
        self._imageSize = pygame.transform.scale(self._image, (30, 30))

        self.position = [(67, 50), (97, 50), (127, 50)]
        self.size = len(self.position)

        self.point = 0
        self._max = 10000

    def adding(self):
        self._position.append((self._life[-1][0] + 30, self._life[-1][1]))

        self._size = len(self.position)

        self._max += 10000

    def delete(self):
        self._size = len(self.position)

        self.position.pop(self._size - 1)
