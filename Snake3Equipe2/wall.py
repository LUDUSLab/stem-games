import pygame

pygame.init()

color_black = (255, 255, 255)
window_size = (1280, 720)
screen = pygame.display.set_mode(window_size)

pygame.display.set_caption("screen test")


class Wall:
    def __init__(self):
        self.size = (40, 40)
        self.color = (200, 200, 200)
        self._wall = pygame.Surface(self.size)
        self._wall.fill(self.color)

    def draw_wall(self):
        screen.blit(self._wall, (0, 32))
        screen.blit(self._wall, (0, 608))
        screen.blit(self._wall, (1248, 32))
        screen.blit(self._wall, (1248, 608))
        for i in range(32, 1248, 32):
            screen.blit(self._wall, (i, 32))
            screen.blit(self._wall, (i, 608))

        for i in range(64, 608, 32):
            screen.blit(self._wall, (0, i))
            screen.blit(self._wall, (1248, i))
