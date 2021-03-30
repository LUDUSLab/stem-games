import pygame
import config
import cube


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

    def add_cube(self):
        pass

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


class SnakePlayer(Snake):
    def __init__(self, color: tuple, pos: tuple):
        super().__init__(color, pos)

    def move(self):
        for event in pygame.event.get():
            config.check_quit_event(event)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.dirnx = -1
                    self.dirny = 0
                    self._turns[self.head.pos[:]] = [self.dirnx, self.dirny]

                elif event.key == pygame.K_d:
                    self.dirnx = 1
                    self.dirny = 0
                    self._turns[self.head.pos[:]] = [self.dirnx, self.dirny]
                elif event.key == pygame.K_w:
                    self.dirnx = 0
                    self.dirny = -1
                    self._turns[self.head.pos[:]] = [self.dirnx, self.dirny]
                elif event.key == pygame.K_s:
                    self.dirnx = 0
                    self.dirny = 1
                    self._turns[self.head.pos[:]] = [self.dirnx, self.dirny]

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
    def __init__(self, color: tuple, pos: tuple):
        super().__init__(color, pos)
