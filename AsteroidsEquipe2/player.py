import scenario

class Player:
    def __init__(self, p_id):
        self.id = p_id
        self.scenario = scenario.Scenario(self)
        self.score = 0
        self.is_turn = False
        self.lives = 3
