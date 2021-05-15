import player
import hud
import config

class Game:
    pvp_mode = False
    game_over = False
    turns = (1, 2)
    turns_aux = 0
    player_turn = turns[turns_aux % 2]

    def __init__(self):
        self.player1 = player.Player()
        self.player2 = player.Player()
        self.hud = hud.HUD()

    def display_hud(self):
        self.hud.score_p1 = config.Text('0'+ str(self.player1.score), 32, (235, 0))
        self.hud.score_p2 = config.Text('0' + str(self.player2.score), 32,
                                        (2 * self.hud.record_score.pos[0] - self.hud.score_p1.pos[0], 0))
        if self.game_over:
            if self.player1.record > self.player2.record:
                self.hud.record_score = config.Text('0' + str(self.player1.record), 16)
            else:
                self.hud.record_score = config.Text('0' + str(self.player2.record), 16)
        self.hud.game_display()

    def pre_game_display(self):
        self.hud.player_turn_text.display()

    def display(self):
        self.display_hud()
        self.pre_game_display()