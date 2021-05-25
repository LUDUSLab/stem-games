import player
import hud
import config

class Game:
    game_over = False
    turns_aux = 0
    aux_time = 100
    pvp_mode = False

    def __init__(self):
        self.players = [player.Player(1), player.Player(2)]
        self.hud = hud.HUD(self.players)

    def display_hud(self):
        if self.players[0].score < 10:
            self.hud.score_p1 = config.Text('0'+ str(self.players[0].score), 32, (235, 0))
        else:
            self.hud.score_p1 = config.Text(str(self.players[0].score), 32, (235, 0))
        if self.players[1].score < 10:
            self.hud.score_p2 = config.Text('0' + str(self.players[1].score), 32,
                                            (2 * self.hud.record_score.pos[0] - self.hud.score_p1.pos[0], 0))
        else:
            self.hud.score_p2 = config.Text(str(self.players[1].score), 32,
                                            (2 * self.hud.record_score.pos[0] - self.hud.score_p1.pos[0], 0))
        if self.game_over:
            if self.players[0].record > self.players[1].record:
                self.hud.record_score = config.Text('0' + str(self.players[0].record), 16)
            else:
                self.hud.record_score = config.Text('0' + str(self.players[1].record), 16)
        self.hud.game_display(self.pvp_mode)

    def display(self):
        self.display_hud()
        self.players[self.turns_aux % 2].scenario.display()
        if self.pvp_mode and self.players[self.turns_aux % 2].scenario.ship is None:
            self.turns_aux += 1
