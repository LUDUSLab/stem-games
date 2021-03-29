import pygame


class Snake:

    def __init__(self, color_1, color_2, position):
        self._body1 = pygame.Surface((32, 32))
        self._body1.fill(color_1)
        self._body2 = pygame.Surface((32, 32))
        self._body2.fill(color_2)
        self._position = position
        self._move_x = 0
        self._move_y = 0

    def new_body(self):
        self._position.append((1280, 640))

    def reset(self, position):
        self._position = position
        self._move_x = 0
        self._move_y = 0

    def draw_snake(self):
        for i, position in enumerate(self._position):
            if i % 2 == 0:
                screen.blit(self._body2, position)

            else:
                screen.blit(self._body1, position)

