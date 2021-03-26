import pygame
import config
import cube


class Snake(object):
    __body: list = []
    __turns: dict = {}

    def __init__(self, color: tuple, pos: tuple):
        self.color = color
        self.head = cube.Cube(pos)
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
        self.head = cube.Cube(pos)
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