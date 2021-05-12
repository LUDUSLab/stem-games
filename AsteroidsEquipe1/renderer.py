import player
import enemy
import particles


class Renderer(object):
    def __init__(self):
        self.player = player.PlayerShip()
        self.enemy = enemy.EnemyShip()
        self.missile = missile.Missile()

    def display(self, screen):
        self.player.draw_playership(screen)
        self.enemy.draw_enemy(screen)
        self.missile.draw_missile(screen)
