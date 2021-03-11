import pygame

pygame.init()
# setting the colors
color_black = (0, 0, 0)
color_white = (255, 255, 255)

game_clock = pygame.time.Clock()

# set the screen
screen_size = (800, 600)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Snake v1.0')

# score text
score_font = pygame.font.Font('./assets/PressStart2P.ttf', 30)
score_text = score_font.render('0', True, color_white, color_black)
score_text_rect = score_text.get_rect()
score_text_rect.center = (310, 25)

# defeat text
defeat_font = pygame.font.Font('./assets/PressStart2P.ttf', 65)
defeat_text = defeat_font.render('GAME OVER', True, color_white, color_black)
defeat_text_rect = score_text.get_rect()
defeat_text_rect.center = (115, 275)

# victory text
victory_font = pygame.font.Font('./assets/PressStart2P.ttf', 65)
victory_text = defeat_font.render('VICTORY!', True, color_white, color_black)
victory_text_rect = score_text.get_rect()
victory_text_rect.center = (175, 275)
