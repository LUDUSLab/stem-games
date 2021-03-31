import pygame
import config
import cube

def false_move(body, turns):
    for i, c in enumerate(body):
        p = c.pos[:]
        if p in turns:
            turn = turns[p]
            c.move(turn[0], turn[1])
            if i == len(body) - 1:
                turns.pop(p)
        else:
            c.move(c.dirnx, c.dirny)


class Snake(object):
    def __init__(self, color: tuple, pos: tuple):
        self.color = color
        self._body: list = []
        self._turns: dict = {}
        self.head = cube.Cube(pos, self.color)
        self._body.append(self.head)
        self.dirnx = 0
        self.dirny = 1
        self.score = 0

    def reset(self, pos):
        self.head = cube.Cube(pos, self.color)
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
            self._body.append(cube.Cube((tail.pos[0] - 1, tail.pos[1]), self.color))
        elif dx == -1 and dy == 0:
            self._body.append(cube.Cube((tail.pos[0] + 1, tail.pos[1]), self.color))
        elif dx == 0 and dy == 1:
            self._body.append(cube.Cube((tail.pos[0], tail.pos[1] - 1), self.color))
        elif dx == 0 and dy == -1:
            self._body.append(cube.Cube((tail.pos[0], tail.pos[1] + 1), self.color))

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
            if self._body[0].pos in list(map(lambda z: z.pos, self._body[x + 1:])):
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
        false_move(self._body, self._turns)


class SnakeBot(Snake):
    def __init__(self, color: tuple, pos: tuple):
        super().__init__(color, pos)

    def move(self, goal):
        if abs(self.head.pos[0] - goal[0]) >= abs(self.head.pos[1] - goal[1]):
            if self.head.pos[0] < goal[0]:
                self.go_right()
            else:
                self.go_left()
        else:
            if self.head.pos[1] < goal[1]:
                self.go_down()
            else:
                self.go_up()

        false_move(self._body, self._turns)