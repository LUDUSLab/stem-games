import pygame
import config

game_surf = pygame.Surface(config.window_size)


class Cube(object):
    __rows: int = 32
    __columns: int = 18

    def __init__(self, start: tuple, color: tuple = config.COLOR_LIGHT_GRAY):
        self.pos = start
        self.dirnx = 1
        self.dirny = 0
        self.color = color

    def move(self, dirnx, dirny):
        self.dirnx = dirnx
        self.dirny = dirny
        self.pos = (self.pos[0] + self.dirnx, self.pos[1] + self.dirny)

    def draw(self, surface):
        dis = config.window_size[0]//self.__rows
        i = self.pos[0]
        j = self.pos[1]
        pygame.draw.rect(surface, self.color, (i * dis + 1, j * dis + 1, dis - 2, dis - 2))

    def get_rows(self):
        return self.__rows

    def get_columns(self):
        return self.__columns


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
                if c.dirnx == -1 and c.pos[0] <= 0:
                    c.pos = (c.get_rows() - 1, c.pos[1])
                elif c.dirnx == 1 and c.pos[0] >= c.get_rows()-1:
                    c.pos = (0, c.pos[1])
                elif c.dirny == 1 and c.pos[1] >= c.get_columns()-1:
                    c.pos = (c.pos[0], 0)
                elif c.dirny == -1 and c.pos[1] <= 0:
                    c.pos = (c.pos[0], c.get_columns()-1)
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

    def draw(self, surface):
        for i, c in enumerate(self.__body):
            c.draw(surface)

    def get_body(self):
        return self.__body

    def get_turns(self):
        return self.__turns

snake = Snake((255, 0, 0), (10, 10))


def draw_grid(sz, rows, columns, surface):
    sqrsize = sz[1] // rows
    x = 0
    y = 0
    for i in range(columns):
        x = x + sqrsize

        pygame.draw.line(surface, config.COLOR_LIGHT_GRAY, (x, 0), (x, sz[0]))
    for j in range(rows):
        y = y + sqrsize

        pygame.draw.line(surface, config.COLOR_LIGHT_GRAY, (0, y), (sz[0], y))

def redraw_window(surface):
    global snake
    surface.fill((0, 0, 0))
    snake.draw(surface)
    draw_grid(config.window_size, 18, 32, surface)

clock = pygame.time.Clock()

def display_game():
    clock.tick(10)
    config.screen.blit(game_surf, (0, 0))
    snake.move()
    for x in range(len(snake.get_body())):
        if snake.get_body()[x].pos in list(map(lambda z:z.pos, snake.get_body()[x+1:])):
            snake.reset((10, 10))
    redraw_window(game_surf)
    pygame.display.update()
