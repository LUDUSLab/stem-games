import pygame
pygame.init()

# Screen setup
grid_square = 32
screen_size = (20 * grid_square, 23 * grid_square)
hud_y = 5 * grid_square
play_area = (20 * grid_square, hud_y + 18 * grid_square)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Snake with Pygame - Version 0.3")

# sound setup
score_sfx = pygame.mixer.Sound('assets/20269__koops__apple-crunch-06.wav')
game_over_sfx = pygame.mixer.Sound('assets/382310__myfox14__game-over-arcade.wav')

# color setup
color_black = (0, 0, 0)
color_green = (40, 100, 40)
color_white = (255, 255, 255)
color_gray = (132, 126, 135)
