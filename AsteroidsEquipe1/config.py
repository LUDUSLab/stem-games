import pygame

pygame.init()

sw, sh = 1000, 800

screen = pygame.display.set_mode((sw, sh))
pygame.display.set_caption("Asteroids")

color_black = (0, 0, 0)
color_white = (255, 255, 255)

game_on = True
game_over = False

game_clock = pygame.time.Clock()

lives = 0
small_enemy = []
big_enemy = []
enemy_missile = []
asteroids = []
player_missile = []
