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
        self.snake_player = snake.SnakePlayer((215, 34, 34), (9, 9))
        self.snake_bot = snake.SnakeBot((71, 77, 188), (25, 9))
        self.wall = wall.Wall()
        self.obstacles = wall.Obstacles()
        self.wall_pos = [x.pos for x in self.wall.wall]
        self.obst_pos = [x.pos for x in self.obstacles.obstacles]
        self.obstacle_matrix = [[False for _ in range(self.rows)] for _ in range(self.columns)]
        for wpos in self.wall_pos:
            self.obstacle_matrix[wpos[0]][wpos[1]] = True
        for opos in self.obst_pos:
            self.obstacle_matrix[opos[0]][opos[1]] = True

    @staticmethod
    def fruit_randomizer():
        # rolls a 100-sided die that determines the next fruit to spawn
        d100 = random.randrange(0, 100)
        fruit_type = 0
        if d100 in range(0, 50):
            fruit_type = 1

        if d100 in range(51, 75):
            fruit_type = 2

        if d100 in range(76, 90):
            fruit_type = 3

        if d100 in range(91, 100):
            fruit_type = 4

        return fruit_type

    def random_fruit(self):
        positions1 = self.snake_player.get_body()
        positions2 = self.snake_bot.get_body()

        while True:
            x = random.randrange(2, 30)
            y = random.randrange(3, 16)
            if len(list(filter(lambda z: z.pos == (x, y), positions1))) > 0 or \
                    len(list(filter(lambda z: z.pos == (x, y), positions2))) > 0:
                continue
            for pos in self.obst_pos:
                if (x, y) == pos:
                    x = random.randrange(2, 30)
                    y = random.randrange(3, 16)
            else:
                break

        return x, y

    def collision_with_snake(self):
        if self.snake_player.head.pos[0] == 1 or self.snake_player.head.pos[0] == self.columns or \
                self.snake_player.head.pos[1] == 2 or self.snake_player.head.pos[1] == self.rows - 1:
            self.snake_player.reset((9, 9))

        if self.snake_bot.head.pos[0] == 1 or self.snake_bot.head.pos[0] == self.columns or \
                self.snake_bot.head.pos[1] == 2 or self.snake_bot.head.pos[1] == self.rows - 1:
            self.snake_bot.reset((25, 9))

    def collision_between_snakes(self):
        for bpos in self.snake_player.get_body():
            if self.snake_bot.head.pos == bpos.pos:
                self.snake_bot.reset((25, 9))
        for bpos in self.snake_bot.get_body():
            if self.snake_player.head.pos == bpos.pos:
                self.snake_player.reset((9, 9))

    def collision_fruit_snake(self):
        if self.snake_player.head.pos == self.fruit.fruit.pos:
            config.eat_sound.play()
            self.snake_player.add_cube()
            self.snake_player.score += self.fruit.value
            self.fruit = fruit.Fruit(self.fruit_randomizer(), self.random_fruit())

        elif self.snake_bot.head.pos == self.fruit.fruit.pos:
            config.eat_sound.play()
            self.snake_bot.add_cube()
            self.snake_bot.score += self.fruit.value
            self.fruit = fruit.Fruit(self.fruit_randomizer(), self.random_fruit())

    def collision_obstacles(self):
        for pos in self.obst_pos:
            if self.snake_player.head.pos == pos:
                self.snake_player.reset((9, 9))
            if self.snake_bot.head.pos == pos:
                self.snake_bot.reset((25, 9))
        for pos in self.wall_pos:
            if self.snake_player.head.pos == pos:
                self.snake_player.reset((9, 9))
            if self.snake_bot.head.pos == pos:
                self.snake_bot.reset((25, 9))

    def draw_grid(self, surface):
        if self.grid:
            x = 0
            y = 0
            for i in range(self.columns):
                x = x + config.SQUARE_SIZE
                pygame.draw.line(surface, config.COLOR_LIGHT_GRAY, (x, 120), (x, self.size[0]))
            for j in range(self.rows):
                y = y + config.SQUARE_SIZE
                pygame.draw.line(surface, config.COLOR_LIGHT_GRAY, (0, y + 80), (self.size[0], y + 80))

    def redraw_window(self, surface):
        surface.fill((0, 0, 0))
        self.fruit.fruit.blit()
        self.snake_player.draw(surface)
        self.snake_bot.draw(surface)
        self.wall.draw_wall()
        self.obstacles.draw_obstacles()
        self.draw_grid(surface)


arena_obj = Arena(config.window.size, False)
