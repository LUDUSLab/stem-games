import pygame
import config

class Game(object):
    def __init__(self):
        self.surface = config.window.create_surface()
        self.arena = Arena(config.window.size)
        self.snake = self.arena.snake
        self.clock = pygame.time.Clock()
        self.framerate = 10

    def display_surface(self):
        config.window.display_surface(self.surface)

    def display_all(self):
        self.clock.tick(self.framerate)
        self.display_surface()
        self.snake.move()
        self.snake.collision_with_herself()
        self.arena.collision_with_snake()
        self.arena.redraw_window(self.surface)
        pygame.display.update()

class Cube(object):
    def __init__(self, start: tuple, color: tuple = (255, 0, 0)):
        self.pos = start
        self.dirnx = 1
        self.dirny = 0
        self.color = color

    def move(self, dirnx, dirny):
        self.dirnx = dirnx
        self.dirny = dirny
        self.pos = (self.pos[0] + self.dirnx, self.pos[1] + self.dirny)

    def draw(self, dist, surface, eyes=False):
        i = self.pos[0]
        j = self.pos[1]
        pygame.draw.rect(surface, self.color, (i * dist + 1, j * dist + 1, dist - 2, dist - 2))
        if eyes:
            centre = dist//2
            radius = 4
            circle_middle = (i*dist+centre-radius, j*dist+8)
            circle_middle2 = (i*dist + dist - radius*2, j*dist+8)
            color = config.COLOR_BLACK
            pygame.draw.circle(surface, color, circle_middle, radius)
            pygame.draw.circle(surface, color, circle_middle2, radius)


class Snake(object):
    __body: list = []
    __turns: dict = {}

    def __init__(self, color: tuple, pos: tuple):
        self.color = color
        self.head = Cube(pos)
        self.__body.append(self.head)
        self.dirnx = 0
        self.dirny = 1

    def move(self):
        for event in pygame.event.get():
            config.check_quit_event(event)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.dirnx = -1
                    self.dirny = 0
                    self.__turns[self.head.pos[:]] = [self.dirnx, self.dirny]
                elif event.key == pygame.K_d:
                    self.dirnx = 1
                    self.dirny = 0
                    self.__turns[self.head.pos[:]] = [self.dirnx, self.dirny]
                elif event.key == pygame.K_w:
                    self.dirnx = 0
                    self.dirny = -1
                    self.__turns[self.head.pos[:]] = [self.dirnx, self.dirny]
                elif event.key == pygame.K_s:
                    self.dirnx = 0
                    self.dirny = 1
                    self.__turns[self.head.pos[:]] = [self.dirnx, self.dirny]
        for i, c in enumerate(self.__body):
            p = c.pos[:]
            if p in self.__turns:
                turn = self.__turns[p]
                c.move(turn[0], turn[1])
                if i == len(self.__body) - 1:
                    self.__turns.pop(p)
            else:
                c.move(c.dirnx, c.dirny)

    def reset(self, pos):
        self.head = Cube(pos)
        self.__body = []
        self.__body.append(self.head)
        self.__turns = {}
        self.dirnx = 0
        self.dirny = 1

    def add_cube(self):
        pass

    def draw(self, dist, surface):
        for i, c in enumerate(self.__body):
            if i == 0:
                c.draw(dist, surface, True)
            else:
                c.draw(dist, surface)

    def collision_with_herself(self):
        for x in range(len(self.__body)):
            if self.__body[x].pos in list(map(lambda z: z.pos, self.__body[x + 1:])):
                self.reset((15, 8))


class Arena(object):
    def __init__(self, size: tuple, grid: bool = True):
        self.columns = 32
        self.rows = 18
        self.size = size
        self.grid = grid
        self.snake = Snake((255, 0, 0), (15, 8))

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
        self.draw_grid(32, 18, surface)
