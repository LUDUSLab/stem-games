import pygame
import config


game_surf = config.window.create_surface()


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

    def draw(self, dist, surface):
        i = self.pos[0]
        j = self.pos[1]
        pygame.draw.rect(surface, self.color, (i * dist + 1, j * dist + 1, dist - 2, dist - 2))


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
            c.draw(dist, surface)

    def get_body(self):
        return self.__body

    def get_turns(self):
        return self.__turns

class Arena(object):
    def __init__(self, size: tuple, grid: bool = True):
        self.columns = 32
        self.rows = 18
        self.size = size
        self.grid = grid
        self.snake = Snake((255, 0, 0), (15, 8))

    def draw_grid(self, columns, rows, surface):
        if self.grid:
            sqrsize = self.size[0] // rows
            x = 0
            y = 0
            for i in range(rows):
                x = x + sqrsize
                pygame.draw.line(surface, config.COLOR_LIGHT_GRAY, (x, 0), (x, self.size[0]))
            for j in range(columns):
                y = y + sqrsize
                pygame.draw.line(surface, config.COLOR_LIGHT_GRAY, (0, y), (self.size[0], y))

    def redraw_window(self, surface):
        surface.fill((0, 0, 0))
        self.snake.draw(self.size[0] // self.columns, surface)
        self.draw_grid(18, 32, surface)

arena = Arena(config.window.size)
snake = arena.snake

clock = pygame.time.Clock()

def display_game():
    clock.tick(10)
    config.window.draw_surface(game_surf)
    snake.move()
    for x in range(len(snake.get_body())):
        if snake.get_body()[x].pos in list(map(lambda z:z.pos, snake.get_body()[x+1:])) \
                or snake.head.pos[0] == -1 or snake.head.pos[0] == arena.columns or snake.head.pos[1] == -1 \
                or snake.head.pos[1] == arena.rows:
            snake.reset((15, 8))
    arena.redraw_window(game_surf)
    pygame.display.update()
