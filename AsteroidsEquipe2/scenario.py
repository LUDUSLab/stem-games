import asteroid
import config

class Scenario:
    aux_time = 100

    def __init__(self):
        self.asteroids_quantity = 4
        self.asteroids = [asteroid.BigAsteroid() for _ in range(self.asteroids_quantity)]
        self.player_turn_text = config.Text("Player 1", 32)
        self.player_turn_text.pos = ((config.window.size[0] -
                                      self.player_turn_text.font.size(self.player_turn_text.message)[0]) / 2, 110)

    def display(self):
        if self.aux_time > 0:
            self.player_turn_text.display()
            self.aux_time -= 1
        else:
            for ast in self.asteroids:
                ast.display()
                ast.move()