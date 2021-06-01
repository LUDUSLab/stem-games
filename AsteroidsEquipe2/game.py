import player
import hud
import config

class Game:
    game_over = False
    turns_aux = 0
    pvp_mode = False

    def __init__(self):
        self.players = [player.Player(1), player.Player(2)]
        self.hud = hud.HUD(self.players)
        if self.pvp_mode:
            self.players[0].scenario.aux_time2, self.players[1].scenario.aux_time2 = 100, 100

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
        self.hud.game_display(self.pvp_mode)

    def display(self):
        self.players[self.turns_aux % 2].scenario.display()
        if self.pvp_mode:
            if self.players[self.turns_aux % 2].scenario.switch_round and \
                    (self.players[0].lives > 0 and self.players[1].lives > 0):
                self.players[self.turns_aux % 2].scenario.switch_round = False
                self.turns_aux += 1
                self.players[self.turns_aux % 2].scenario.aux_time2 = 100

        else:
            self.players[self.turns_aux % 2].scenario.switch_round = False
            if self.players[self.turns_aux % 2].lives <= 0 and \
                    not self.players[self.turns_aux % 2].scenario.showing_game_over_header:
                self.game_over = True
        if self.game_over:
            self.hud.record_score = config.Text(str(max([x.score for x in self.players])), 16)
            self.hud.record_score.pos = (
                (config.window.size[0] - self.hud.record_score.font.size(self.hud.record_score.message)[0]) / 2, 20)

        self.display_hud()
