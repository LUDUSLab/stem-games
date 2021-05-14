import player
import enemy
import particles


class Renderer(object):
    def __init__(self):
        self.player = player.PlayerShip()
        self.enemy = enemy.EnemyShip()
        self.player_missile = player_missile.Missile()
        self.enemy_missile = enemy_missile.EnemyMissile()

    def display(self, screen):
        self.player.draw(screen)
        self.enemy.draw(screen)
        self.player_missile.draw(screen)
        self.enemy_missile.draw(screen)
