import pygame
import config
import snake
import wall
import fruit
import random


class Arena(object):
    def __init__(self, size: tuple, grid: bool = True):
        self.columns = 32
        self.rows = 18
        self.size = size
        self.grid = grid
        self.snake_player = snake.snake_player
        self.wall = wall.Wall()
        self.wall = wall.Obstacles((200, 200, 200))
        self.fruit = fruit.Fruit(1, (random.randrange(3, 28), random.randrange(3, 14)))

    def random_fruit(self):

        positions = self.snake_player.body

        while True:
            x = random.randrange(3, 28)
            y = random.randrange(3, 14)
            if len(list(filter(lambda z: z.pos == (x, y), positions))) > 0:
                continue
            else:
                break
        return x, y

    def collision_with_snake(self):
        if self.snake_player.head.pos[0] == 2 or self.snake_player.head.pos[0] == self.columns - 3 or \
                self.snake_player.head.pos[1] == 2 or self.snake_player.head.pos[1] == self.rows - 3:
            self.snake_player.reset((15, 8))

    def collision_fruit_snake(self):
        if self.snake_player.head.pos == self.fruit.fruit.pos:
            self.snake_player.add_cube()
            self.fruit = fruit.Fruit(1, self.random_fruit())
            self.snake_player.score += self.fruit.value

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
        self.snake_player.draw(self.size[0] // self.columns, surface)
        self.fruit.fruit.draw(self.size[0] // self.columns, surface)
        self.wall.draw_wall(surface)
        self.wall.draw_obstacles(surface)
        self.draw_grid(32, 18, surface)

arena_obj = Arena(config.window.size, True)