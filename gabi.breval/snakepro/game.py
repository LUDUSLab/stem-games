import pygame
import config

# Colors ------------------------------------------------------------------------------------------------------- #
light_grey = (200, 200, 200)
bg_color = pygame.Color('grey12')
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# score text --------------------------------------------------------------------------------------------------- #
font = config.address('gabi.brevalFont.otf', 'font')
score_font = pygame.font.Font(config.address('gabi.brevalFont.otf', 'font'), 35)
score_text = score_font.render(' 0', True, COLOR_WHITE, COLOR_BLACK)
score_text_rect = score_text.get_rect()
score_text_rect.center = (config.WIDTH / 2, 30)
score = 0

# Game over text ----------------------------------------------------------------------------------------------- #
lose_font = pygame.font.Font(config.address('gabi.brevalFont.otf', 'font'),
                             100)
lose_text = lose_font.render('Game over!', True, COLOR_WHITE, COLOR_BLACK)
lose_text_rect = score_text.get_rect()
lose_text_rect.center = (600, 350)
# -------------------------------------------------------------------------------------------------------------- #

# Sound ------------------------------------------------------------------------------------------------------ #
munch_sound_effect = pygame.mixer.Sound(config.address('gabi.breval.munch-sound.wav', 'sound'))
game_over_effect = pygame.mixer.Sound(config.address('batida_gabi.breval.wav', 'sound'))


# Grass -------------------------------------------------------------------------------------------------------- #
grass = pygame.image.load(config.address('gabi.breval.folha.png', 'skin'))

