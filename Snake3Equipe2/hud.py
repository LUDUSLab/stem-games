import config
import arena
import cube


class Score(object):
    def __init__(self):
        self.font = config.font(30)
        self.text = self.font.render("Player " + str(arena.arena_obj.snake_player.score) + "X" +
                                     str(arena.arena_obj.snake_bot.score) + " IA", True, config.COLOR_LIGHT_GRAY)
        self.text_rect = self.text.get_rect()


class Hud(object):
    # __cube1 = cube.Cube((5, 1), (255, 0, 0))
    p1 = cube.Cube((9.5, 1), (255, 0, 0))
    ia = cube.Cube((21.5, 1), (10, 150, 200))

    def __init__(self):
        self.score = Score()

    def display_score(self, surface):
        self.score = Score()
        self.score.text_rect.center = (640, 60)
        surface.blit(self.score.text, self.score.text_rect)

    def display_hud_cubes(self, surface):
        self.p1.draw(config.SQUARE_SIZE, surface, True)
        self.ia.draw(config.SQUARE_SIZE, surface, True)


hud_obj = Hud()
