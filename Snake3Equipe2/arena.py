import pygame
import config
import snake
import wall
import fruit
import cube


class Arena(object):
    def __init__(self, size: tuple, grid: bool = True):
        self.columns = 32
        self.rows = 18
        self.size = size
        self.grid = grid
        self.snake = snake.SnakePlayer((255, 0, 0), (15, 8))
        self.wall = wall.Wall()
        self.fruit = fruit.Fruit(1)
        self.p1 = cube.Cube((10, 1), (255, 0, 0))
        self.ia = cube.Cube((21, 1), (10, 150, 200))

    def collision_with_snake(self):
        if self.snake.head.pos[0] == 2 or self.snake.head.pos[0] == self.columns - 3 or self.snake.head.pos[1] == 2 \
                or self.snake.head.pos[1] == self.rows - 3:
            self.snake.reset((15, 8))

    def collision_fruit_snake(self):
        if self.snake.head.pos == self.fruit.fruit.pos:
            self.fruit = fruit.Fruit(1)
            self.snake.score += self.fruit.value

    def draw_grid(self, columns, rows, surface):
        if self.grid:
            sqrsize = self.size[0] // columns
            x = 0
            y = 0
            for i in range(columns - 5):
                x = x + sqrsize
                pygame.draw.line(surface, config.COLOR_LIGHT_GRAY, (x + 80, 120), (x + 80, self.size[0] - 680))
            for j in range(rows - 5):
                y = y + sqrsize
                pygame.draw.line(surface, config.COLOR_LIGHT_GRAY, (120, y + 80), (self.size[0] - 120, y + 80))

    def redraw_window(self, surface):
        surface.fill((0, 0, 0))
        self.snake.draw(self.size[0] // self.columns, surface)
        self.fruit.fruit.draw(self.size[0] // self.columns, surface)
        self.p1.draw(self.size[0] // self.columns, surface, True)
        self.ia.draw(self.size[0] // self.columns, surface, True)
        self.wall.draw_wall(surface)
        self.draw_grid(32, 18, surface)
