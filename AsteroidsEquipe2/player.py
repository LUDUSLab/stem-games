import scenario

class Player:
    def __init__(self):
        self.scenario = scenario.Scenario(self)
        self.score = 0
        self.record = 0
        self.is_turn = False
        self.lives = 3
