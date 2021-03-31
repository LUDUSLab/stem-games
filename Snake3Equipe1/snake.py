import pygame
from game_logic import Action

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


class Player(Snake):

    LEFT, UP, RIGHT, DOWN = 37, 38, 39, 40

    def __init__(self, color_1, color_2, position):
        super().__init__(color_1, color_2, position)
        self._current_action = Action.LEFT

    def snake_moves(self, direction):
        if direction == self.LEFT:
            self._move_x = -32
            self._move_y = 0

        if direction == self.UP:
            self._move_x = 0
            self._move_y = -32

        if direction == self.RIGHT:
            self._move_x = 32
            self._move_y = 0

        if direction == self.DOWN:
            self._move_x = 0
            self._move_y = 32

        for c in range(len(self._position) - 1, 0, -1):
            self._position[c] = (self._position[c - 1][0], self._position[c - 1][1])

        self._position[0] = (self._position[0][0] + self._move_x, self._position[0][1] + self._move_y)

    def act(self, user_events=None):
        """ Returns the action taken by the human player. """
        events = user_events if user_events is not None else pygame.event.get()
        new_action = self._current_action
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and self._current_action != Action.RIGHT:
                    new_action = Action.LEFT
                elif event.key == pygame.K_RIGHT and self._current_action != Action.LEFT:
                    new_action = Action.RIGHT
                elif event.key == pygame.K_UP and self._current_action != Action.DOWN:
                    new_action = Action.UP
                elif event.key == pygame.K_DOWN and self._current_action != Action.UP:
                    new_action = Action.DOWN

        return new_action


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
