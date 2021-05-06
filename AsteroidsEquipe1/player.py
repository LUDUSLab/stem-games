import pygame.rect
from config import *


class PlayerShip:
    def __init__(self):
        self.size = (20, 20)
        self.color = (255, 255, 255)
        self.position = [(500, 500)]

    def player_move(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    self.position[0] = (self.position[0][0], self.position[0][1] - 5)
                elif event.key == pygame.K_s:
                    self.position[0] = (self.position[0][0], self.position[0][1] + 5)
                elif event.key == pygame.K_a:
                    self.position[0] = (self.position[0][0] - 5, self.position[0][1])
                elif event.key == pygame.K_d:
                    self.position[0] = (self.position[0][0] + 5, self.position[0][1])

    def draw(self):
        pygame.draw.rect(screen, self.color, (250, 250) + self.size)

playership = PlayerShip()