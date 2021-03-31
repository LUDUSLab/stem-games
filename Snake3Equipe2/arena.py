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
        self.fruit = fruit.Fruit(1, (random.randrange(1, 30), random.randrange(3, 16)))
        self.snake_player = snake.SnakePlayer((255, 0, 0), (15, 8))
        self.snake_bot = snake.SnakeBot((10, 150, 200), (10, 10))
        self.wall = wall.Wall()
        self.wall = wall.Obstacles((200, 200, 200))
        self.obst_pos = [(1, 7), (2, 7), (6, 3), (6, 4), (6, 5), (16, 3), (16, 4), (16, 5), (25, 3), (25, 4), (25, 5),
                         (30, 7), (29, 7), (19, 9), (20, 9), (21, 9), (8, 8), (8, 9), (8, 10), (1, 12), (2, 12),
                         (13, 11), (13, 12), (13, 13), (8, 15), (8, 16), (8, 17), (30, 12), (29, 12), (22, 15),
                         (22, 16),
                         (22, 17)]

    def random_fruit(self):
        positions1 = self.snake_player.get_body()
        positions2 = self.snake_bot.get_body()

        while True:
            x = random.randrange(1, 30)
            y = random.randrange(3, 16)
            if len(list(filter(lambda z: z.pos == (x, y), positions1))) > 0 or \
                    len(list(filter(lambda z: z.pos == (x, y), positions2))) > 0:
                continue
            else:
                break

        return x, y

    def collision_with_snake(self):
        if self.snake_player.head.pos[0] == 1 or self.snake_player.head.pos[0] == self.columns or \
                self.snake_player.head.pos[1] == 2 or self.snake_player.head.pos[1] == self.rows - 1:
            self.snake_player.reset((15, 8))

        if self.snake_bot.head.pos[0] == 1 or self.snake_bot.head.pos[0] == self.columns or \
                self.snake_bot.head.pos[1] == 2 or self.snake_bot.head.pos[1] == self.rows - 1:
            self.snake_bot.reset((10, 10))

    def collision_fruit_snake(self):
        if self.snake_player.head.pos == self.fruit.fruit.pos:
            self.snake_player.add_cube()
            self.fruit = fruit.Fruit(1, self.random_fruit())
            self.snake_player.score += self.fruit.value
        elif self.snake_bot.head.pos == self.fruit.fruit.pos:
            self.snake_bot.add_cube()
            self.fruit = fruit.Fruit(1, self.random_fruit())
            self.snake_bot.score += self.fruit.value

    def collision_obstacles(self):
        for i in range(len(self.obst_pos)):
            if self.snake_player.head.pos == self.obst_pos[i]:
                self.snake_player.reset((15, 8))

    def draw_grid(self, columns, rows, surface):
        if self.grid:
            sqrsize = self.size[0] // columns
            x = 0
            y = 0
            for i in range(columns):
                x = x + sqrsize
                pygame.draw.line(surface, config.COLOR_LIGHT_GRAY, (x, 120), (x, self.size[0]))
            for j in range(rows):
                y = y + sqrsize
                pygame.draw.line(surface, config.COLOR_LIGHT_GRAY, (0, y + 80), (self.size[0], y + 80))

    def redraw_window(self, surface):
        surface.fill((0, 0, 0))
        self.fruit.fruit.draw(self.size[0] // self.columns, surface)
        self.snake_player.draw(self.size[0] // self.columns, surface)
        self.snake_bot.draw(self.size[0] // self.columns, surface)
        self.wall.draw_wall(surface)
        self.wall.draw_obstacles(surface)
        self.draw_grid(32, 18, surface)


arena_obj = Arena(config.window.size, True)
