import pygame

pygame.init()

sw, sh = 1280, 720

screen = pygame.display.set_mode((sw, sh))
pygame.display.set_caption("Asteroids")

score_font = pygame.font.Font('../AsteroidsEquipe1/assets/ThinPixel7-1Yq0.ttf', 80)
credits_font = pygame.font.Font('../AsteroidsEquipe1/assets/ThinPixel7-1Yq0.ttf', 40)
play_font = pygame.font.Font('../AsteroidsEquipe1/assets/ThinPixel7-1Yq0.ttf', 55)

shoot_sound = pygame.mixer.Sound('../AsteroidsEquipe1/assets/391660__jeckkech__projectile.wav')

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
