import pygame
import config
import snake
import wall


class Arena(object):
    def __init__(self, size: tuple, grid: bool = True):
        self.columns = 32
        self.rows = 18
        self.size = size
        self.grid = grid
        self.snake = snake.SnakePlayer((255, 0, 0), (15, 8))
        self._wall = self._wall

    def collision_with_snake(self):
        if self.snake.head.pos[0] == -1 or self.snake.head.pos[0] == self.columns or self.snake.head.pos[1] == -1 \
           or self.snake.head.pos[1] == self.rows:
            self.snake.reset((15, 8))

    def draw_grid(self, columns, rows, surface):
        if self.grid:
            sqrsize = self.size[0] // columns
            x = 0
            y = 0
            for i in range(columns):
                x = x + sqrsize
                pygame.draw.line(surface, config.COLOR_LIGHT_GRAY, (x, 0), (x, self.size[0]))
            for j in range(rows):
                y = y + sqrsize
                pygame.draw.line(surface, config.COLOR_LIGHT_GRAY, (0, y), (self.size[0], y))

    def redraw_window(self, surface):
        surface.fill((0, 0, 0))
        self.snake.draw(self.size[0] // self.columns, surface)
        self._wall.draw_wall(surface)
        self.draw_grid(32, 18, surface)
