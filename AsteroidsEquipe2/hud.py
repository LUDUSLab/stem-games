import config

class HUD:
    def __init__(self, players):
        self.score_p1 = config.Text("00", 32, (235, 0))
        self.record_score = config.Text("00", 16)
        self.record_score.pos = ((config.window.size[0]-self.record_score.font.size(self.record_score.message)[0])/2,
                                 20)
        self.score_p2 = config.Text("00", 32, (2*self.record_score.pos[0] - self.score_p1.pos[0], 0))
        if players is not None:
            self.is_p1_turn = players[0].is_turn
            self.is_p2_turn = players[1].is_turn
            self.lives_sprite = players[0].scenario.ship.sprite
        self.lives = 0

    def menu_display(self):
        self.record_score.display()
        self.score_p1.display()
        self.score_p2.display()

    def game_display(self):
        self.record_score.display()
        if self.is_p1_turn:
            self.score_p1.display()
        else:
            self.score_p2.display()
        # Here i need to display the ship lives sprite
