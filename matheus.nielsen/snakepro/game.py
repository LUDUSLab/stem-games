# Modular snake in Python with Pygame
# Pygame website https://www.pygame.org/news
# Version 0.0
# Bite sfx by Koops available at https://freesound.org/people/Koops/sounds/20269/
# Game Over sfx by myfox14 available at https://freesound.org/people/myfox14/sounds/382310/
# Game font Press Start 2P, available at https://fonts.google.com/specimen/Press+Start+2P?preview.text_type=custom

import pygame
# import snake_script
# import apple_script

pygame.init()

# Title Screen
# screen setup
screen_size = (640, 640)
color_black = (0, 0, 0)
color_white = (255, 255, 255)
color_gray = (122, 122, 122)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Snake with Pygame - Version 1.0")

# Title screen text
# Title
title_font = pygame.font.Font('assets/PressStart2P.ttf', 96)
title_text = title_font.render('SNAKE', False, color_white)
title_rect = title_text.get_rect()
title_rect.center = (320, 120)

# Play and High score
subtitle_font = pygame.font.Font('assets/PressStart2P.ttf', 22)
play_text = subtitle_font.render('Press space to play!', False, color_white)
play_rect = play_text.get_rect()
play_rect.center = (320, 320)

highscore = open('highscores.md', 'r')
highscore_text = subtitle_font.render('Highscore: ' + highscore.read(), False, color_white)
highscore_rect = highscore_text.get_rect()
highscore_rect.center = (220, 520)

menu_open = True
game_clock = pygame.time.Clock()
while menu_open:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            menu_open = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                menu_open = False
            if event.key == pygame.K_ESCAPE:
                menu_open = False

    screen.blit(title_text, title_rect)
    screen.blit(play_text, play_rect)
    screen.blit(highscore_text, highscore_rect)

    game_clock.tick(10)
    pygame.display.update()

pygame.quit()
