import config

class ScoreMenu:
    def __init__(self, hud):
        self.hud = hud
        self.header = config.Text("HIGH SCORES", 32)
        self.header.pos = ((config.window.size[0] - self.header.text.get_size()[0])/2, 100)
        self.record_scores = [hud.score_p1.message, hud.score_p2.message]

    def display(self):
        self.hud.menu_display()
        self.header.display()