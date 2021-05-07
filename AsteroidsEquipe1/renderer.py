import config
import player
import pygame.display


class Renderer:
    def __init__(self):
        self.playership = playership.PlayerShip()

    def redrawgamewindow(self, screen):
        screen.fill(color_black)
        screen.blit(self.player_ship, self.player_ship.position)
        pygame.display.update()


renderer = Renderer()
