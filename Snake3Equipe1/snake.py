import pygame
from config import screen


class Snake:

    def __init__(self, color_1, color_2, position, image):
        self._body1 = pygame.Surface((32, 32))
        self._body1.fill(color_1)
        self._body2 = pygame.Surface((32, 32))
        self._body2.fill(color_2)

        self._head = pygame.image.load(image)

        self._position = position
        self._move_x = 0
        self._move_y = 0

    @property
    def position(self):
        return self._position

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


class Player(Snake):
    W, A, S, D = 0, 1, 2, 3

    def snake_moves(self, direction):
        if direction == self.S:
            self._move_x = -32
            self._move_y = 0

        if direction == self.W:
            self._move_x = 0
            self._move_y = -32

        if direction == self.D:
            self._move_x = 32
            self._move_y = 0

        if direction == self.S:
            self._move_x = 0
            self._move_y = 32

        for c in range(len(self._position) - 1, 0, -1):
            self._position[c] = (self._position[c - 1][0], self._position[c - 1][1])

        self._position[0] = (self._position[0][0] + self._move_x, self._position[0][1] + self._move_y)


class ArtificialIntelligence(Snake):

    def ia_moves(self, fruit_position):

        for c in range(len(self._position) - 1, 0, -1):
            self._position[c] = (self._position[c - 1][0], self._position[c - 1][1])

        if fruit_position[0] - self._position[0][0] > 0 and fruit_position[1] - self._position[0][1] == 0:
            self._move_x = 32
            self._move_y = 0

        elif fruit_position[0] - self._position[0][0] < 0 and fruit_position[1] - self._position[0][1] == 0:
            self._move_x = -32
            self._move_y = 0

        elif fruit_position[0] - self._position[0][0] == 0 and fruit_position[1] - self._position[0][1] > 0:
            self._move_x = 0
            self._move_y = 32

        elif fruit_position[0] - self._position[0][0] == 0 and fruit_position[1] - self._position[0][1] < 0:
            self._move_x = 0
            self._move_y = -32

        elif fruit_position[0] - self._position[0][0] > 0 and fruit_position[1] - self._position[0][1] > 0:
            self._move_x = 32
            self._move_y = 0

            if fruit_position[0] - self._position[0][0] < 0:
                self._move_x = 0
                self._move_y = 32

        elif fruit_position[0] - self._position[0][0] > 0 > fruit_position[1] - self._position[0][1]:
            self._move_x = 32
            self._move_y = 0

            if fruit_position[0] - self._position[0][0] < 0:
                self._move_x = 0
                self._move_y = -32

        elif fruit_position[0] - self._position[0][0] < 0 < fruit_position[1] - self._position[0][1]:
            self._move_x = -32
            self._move_y = 0

            if fruit_position[0] - self._position[0][0] > 0:
                self._move_x = 0
                self._move_y = 32

        elif fruit_position[0] - self._position[0][0] < 0 and fruit_position[1] - self._position[0][1] < 0:
            self._move_x = -32
            self._move_y = 0

            if fruit_position[0] - self._position[0][0] > 0:
                self._move_x = 0
                self._move_y = -32

        self._position[0] = (self._position[0][0] + self._move_x, self._position[0][1] + self._move_y)
