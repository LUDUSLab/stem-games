import pygame
import config
import cube
import astar


class Snake(object):
    _body: list = []
    _turns: dict = {}

    def __init__(self, color: tuple, pos: tuple):
        self.color = color
        self.head = cube.Cube(pos)
        self._body.append(self.head)
        self.dirnx = 0
        self.dirny = 1
        self.score = 0

    def reset(self, pos):
        self.head = cube.Cube(pos)
        self._body = []
        self._body.append(self.head)
        self._turns = {}
        self.dirnx = 0
        self.dirny = 1
        self.score = 0

    def go_right(self):
        self.dirnx = 1
        self.dirny = 0
        self._turns[self.head.pos[:]] = [self.dirnx, self.dirny]

    def go_down(self):
        self.dirnx = 0
        self.dirny = 1
        self._turns[self.head.pos[:]] = [self.dirnx, self.dirny]

    def go_left(self):
        self.dirnx = -1
        self.dirny = 0
        self._turns[self.head.pos[:]] = [self.dirnx, self.dirny]

    def go_up(self):
        self.dirnx = 0
        self.dirny = -1
        self._turns[self.head.pos[:]] = [self.dirnx, self.dirny]

    def add_cube(self):
        tail = self._body[-1]
        dx, dy = tail.dirnx, tail.dirny

        if dx == 1 and dy == 0:
            self._body.append(cube.Cube((tail.pos[0] - 1, tail.pos[1])))
        elif dx == -1 and dy == 0:
            self._body.append(cube.Cube((tail.pos[0] + 1, tail.pos[1])))
        elif dx == 0 and dy == 1:
            self._body.append(cube.Cube((tail.pos[0], tail.pos[1] - 1)))
        elif dx == 0 and dy == -1:
            self._body.append(cube.Cube((tail.pos[0], tail.pos[1] + 1)))

        self._body[-1].dirnx = dx
        self._body[-1].dirny = dy

    def draw(self, dist, surface):
        for i, c in enumerate(self._body):
            if i == 0:
                c.draw(dist, surface, True)
            else:
                c.draw(dist, surface)

    def collision_with_herself(self):
        for x in range(len(self._body)):
            if self._body[x].pos in list(map(lambda z: z.pos, self._body[x + 1:])):
                self.reset((15, 8))

    def get_body(self):
        return self._body


class SnakePlayer(Snake):
    def __init__(self, color: tuple, pos: tuple):
        super().__init__(color, pos)

    def move(self):
        for event in pygame.event.get():
            config.check_quit_event(event)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.go_left()
                elif event.key == pygame.K_d:
                    self.go_right()
                elif event.key == pygame.K_w:
                    self.go_up()
                elif event.key == pygame.K_s:
                    self.go_down()

        for i, c in enumerate(self._body):
            p = c.pos[:]
            if p in self._turns:
                turn = self._turns[p]
                c.move(turn[0], turn[1])
                if i == len(self._body) - 1:
                    self._turns.pop(p)
            else:
                c.move(c.dirnx, c.dirny)


class SnakeBot(Snake):
    def __init__(self, color: tuple, pos: tuple, afruit):
        super().__init__(color, pos)
        self.start = self.head.pos
        self.end = afruit.pos
        self.path = astar.Astar(self.start, self.end).run()
        self.x_head, self.y_head = self.head.pos[0], self.head.pos[1]

    def move(self):
        for (x, y) in self.path:
            if x > self.x_head:
                self.go_right()
            if x < self.x_head:
                self.go_left()
            if y > self.y_head:
                self.go_down()
            if y < self.y_head:
                self.go_up()
            self.x_head = x
            self.y_head = y
