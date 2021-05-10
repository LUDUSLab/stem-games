import player


class Missile(object):
    def __init__(self):
        self.point = playership.head
        self.x, self.y = self.point
        self.w, self.h = 4, 4
        self.c, self.s = playership.player_cos, playership.player_sin
        self.xv, self.yv = self.c * 10, self.s * 10

    def missile_move(self):
        self.x += self.xv
        self.y -= self.yv

    def draw_missile(self, screen):
        pygame.draw.rect(screen, color_white, [self.x, self.y, self.w, self.h])


missile = Missile()
