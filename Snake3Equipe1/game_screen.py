import pygame
import config


class GameScreen:

    def __init__(self, size=config.screen_dimensions):
        self._size = size
        self._display = pygame.display.set_mode(size)
        self._FONT = pygame.font.SysFont(config.font, 32)

    def draw(self, score, start_msg=False):
        """ Draws the game on the screen. """
        self._display.fill(config.BACKGROUND_COLOR)

        txt_surface = self._FONT.render("SCORE: %d" % score, False, (255, 247, 0))
        self._display.blit(txt_surface, (550, 85))

        # "press space" msg para poder comecar
        if start_msg:
            txt_surface = self._FONT.render("Press SPACE to start.", False, (255, 255, 255))
            self._display.blit(txt_surface, (530, 450))

        pygame.display.update()
