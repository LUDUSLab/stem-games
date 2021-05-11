import config
import ship

class HUD:
    def __init__(self):
        self.record_score1 = config.Text(str(ship.score)+"0", 32, (235, 0))
        self.record_score = config.Text(str(ship.record)+"0", 16)
        self.record_score.pos = ((config.window.size[0]-self.record_score.font.size(self.record_score.message)[0])/2,
                                 20)
        self.record_score2 = config.Text(str(ship.score)+"0", 32,
                                         (2*self.record_score.pos[0] - self.record_score1.pos[0], 0))

    def menu_display(self):
        self.record_score.display()
        self.record_score1.display()
        self.record_score2.display()
