import config


class Score(object):
    def __init__(self, score_p1, score_ia):
        self.font = config.font(30)
        self.text = self.font.render("Player " + str(score_p1) + "X" + str(score_ia) + " IA", True,
                                     config.COLOR_LIGHT_GRAY)
        self.text_rect = self.text.get_rect()


class Hud(object):
    # __cube1 = cube.Cube((5, 1), (255, 0, 0))
    def __init__(self, score_p1, score_ia):
        self.score = Score(score_p1, score_ia)

    def display_score(self):
        self.score.text_rect.center = (640, 60)
        config.window.screen.blit(self.score.text, self.score.text_rect)
