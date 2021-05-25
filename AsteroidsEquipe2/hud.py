import config

class HUD:
    def __init__(self, players):
        self.score_p1 = config.Text("00", 32, (235, 0))
        self.record_score = config.Text("00", 16)
        self.record_score.pos = ((config.window.size[0]-self.record_score.font.size(self.record_score.message)[0])/2,
                                 20)
        self.score_p2 = config.Text("00", 32, (2*self.record_score.pos[0] - self.score_p1.pos[0], 0))
        self.players = players
        if self.players is not None:
            self.is_p1_turn = self.players[0].is_turn
            self.is_p2_turn = self.players[1].is_turn
            self.lives_sprite = self.players[0].scenario.ship.sprite
            self.p1_lives = self.players[0].lives
            self.p2_lives = self.players[1].lives

    def menu_display(self):
        self.record_score.display()
        self.score_p1.display()
        self.score_p2.display()

    def game_display(self, pvp_mode):
        aux_x = 195
        self.record_score.display()
        self.p1_lives = self.players[0].lives
        for _ in range(self.p1_lives):
            config.window.screen.blit(self.lives_sprite, (aux_x, 45))
            aux_x += 26
        self.score_p1.display()
        if pvp_mode:
            self.p2_lives = self.players[1].lives
            for _ in range(self.p2_lives):
                config.window.screen.blit(self.lives_sprite, (config.window.size[0] - aux_x+26, 45))
                aux_x -= 26
            self.score_p2.display()
