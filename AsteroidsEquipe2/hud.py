import config

class HUD:
    def __init__(self):
        self.score_p1 = config.Text("00", 32, (235, 0))
        self.record_score = config.Text("00", 16)
        self.record_score.pos = ((config.window.size[0]-self.record_score.font.size(self.record_score.message)[0])/2,
                                 20)
        self.score_p2 = config.Text("00", 32, (2*self.record_score.pos[0] - self.score_p1.pos[0], 0))
        self.player_turn_text = config.Text("Player 1", 32)
        self.player_turn_text.pos = ((config.window.size[0] -
                                      self.player_turn_text.font.size(self.player_turn_text.message)[0])/2, 110)
        self.lives = 0

    def menu_display(self):
        self.record_score.display()
        self.score_p2.display()
        self.score_p1.display()

    def game_display(self):
        self.menu_display()
        # Here i need to display the ship lives sprite
