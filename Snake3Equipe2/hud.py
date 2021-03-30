import config


class Hud(object):
    # __cube1 = cube.Cube((5, 1), (255, 0, 0))
    def display_score(self, score_p1, score_ia):
        score_font = config.font(30)
        score_text = score_font.render("Player " + str(score_p1) + "X" + str(score_ia) + " IA", True, config.COLOR_LIGHT_GRAY)
        score_text_rect = score_text.get_rect()
        score_text_rect.center = (640, 60)
        config.window.screen.blit(score_text, score_text_rect)
