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
    can_move = {"right": True,"down": True,"left": True,"up": True}

    def __init__(self, color: tuple, pos: tuple):
        super().__init__(color, pos)

    def move(self, goal, obstacle_matrix):
        if self.head.pos[0] < 31:
            if obstacle_matrix[self.head.pos[0] + 1][self.head.pos[1]]:
                self.can_move["right"] = False
            else:
                self.can_move["right"] = True
        if self.head.pos[0] > 0:
            if obstacle_matrix[self.head.pos[0] - 1][self.head.pos[1]]:
                self.can_move["left"] = False
            else:
                self.can_move["left"] = True
        if self.head.pos[1] < 18:
            if obstacle_matrix[self.head.pos[0]][self.head.pos[1] + 1]:
                self.can_move["down"] = False
            else:
                self.can_move["down"] = True
        if self.head.pos[1] > 0:
            if obstacle_matrix[self.head.pos[0]][self.head.pos[1] - 1]:
                self.can_move["up"] = False
            else:
                self.can_move["up"] = True
        if self.dirnx > 0:
            self.can_move["left"] = False
        elif self.dirnx < 0:
            self.can_move["right"] = False
        elif self.dirny > 0:
            self.can_move["up"] = False
        elif self.dirny < 0:
            self.can_move["down"] = False

        def check_move(s):
            if s == "vertical":
                if self.head.pos[1] > goal[1]:
                    if self.can_move["up"]:
                        self.go_up()
                    elif self.can_move["down"]:
                        self.go_down()
                if self.head.pos[1] < goal[1]:
                    if self.can_move["down"]:
                        self.go_down()
                    elif self.can_move["up"]:
                        self.go_up()
            if s == "vertical2":
                if self.head.pos[1] < goal[1]:
                    if self.can_move["down"]:
                        self.go_down()
                    elif self.can_move["up"]:
                        self.go_up()
                if self.head.pos[1] > goal[1]:
                    if self.can_move["up"]:
                        self.go_up()
                    elif self.can_move["down"]:
                        self.go_down()

            if s == "horizontal":
                if self.head.pos[0] < goal[0]:
                    if self.can_move["right"]:
                        self.go_right()
                    elif self.can_move["left"]:
                        self.go_left()
                if self.head.pos[0] > goal[0]:
                    if self.can_move["left"]:
                        self.go_left()
                    elif self.can_move["right"]:
                        self.go_right()

        if abs(self.head.pos[0] - goal[0]) >= abs(self.head.pos[1] - goal[1]):
            if self.head.pos[0] < goal[0]:
                if self.can_move["right"]:
                    self.go_right()
                else:
                    check_move("vertical")

            elif self.head.pos[0] > goal[0]:
                if self.can_move["left"]:
                    self.go_left()
                else:
                    check_move("vertical")

            else:
                if self.head.pos[1] < goal[1]:
                    if self.can_move["down"]:
                        self.go_down()
                    else:
                        check_move("horizontal")
                elif self.head.pos[1] > goal[1]:
                    if self.can_move["up"]:
                        self.go_up()
                    else:
                        check_move("horizontal")
        else:
            if self.head.pos[1] < goal[1]:
                if self.can_move["down"]:
                    self.go_down()
                else:
                    check_move("horizontal")

            elif self.head.pos[1] > goal[1]:
                if self.can_move["up"]:
                    self.go_up()
                else:
                    check_move("horizontal")
            else:
                if self.head.pos[0] < goal[0]:
                    if self.can_move["right"]:
                        self.go_right()
                    else:
                        check_move("vertical2")
                elif self.head.pos[0] > goal[0]:
                    if self.can_move["left"]:
                        self.go_left()
                    else:
                        check_move("vertical2")
        false_move(self._body, self._turns)
