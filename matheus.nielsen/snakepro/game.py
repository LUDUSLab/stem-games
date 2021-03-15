# Modular snake in Python with Pygame
# Pygame website https://www.pygame.org/news
# Version 0.0
# Bite sfx by Koops available at https://freesound.org/people/Koops/sounds/20269/
# Game Over sfx by myfox14 available at https://freesound.org/people/myfox14/sounds/382310/
# Game font Press Start 2P, available at https://fonts.google.com/specimen/Press+Start+2P?preview.text_type=custom

from screen import *
import apple
import snake
import walls

pygame.init()

# Title screen text
# Title
title_font = pygame.font.Font('assets/PressStart2P.ttf', 96)
title_text = title_font.render('SNAKE', False, color_white)
title_rect = title_text.get_rect()
title_rect.center = (screen_size[0] / 2, screen_size[1] / 2 - 200)

# Play
subtitle_font = pygame.font.Font('assets/PressStart2P.ttf', 22)
play_text = subtitle_font.render('Press space to play!', False, color_white)
play_rect = play_text.get_rect()
play_rect.center = (screen_size[0] / 2, screen_size[1] / 2)

# High score
highscore = open('high_scores.md', 'r')
highscore_text = subtitle_font.render('Highscore: ' + highscore.read(), False, color_white)
highscore_rect = highscore_text.get_rect()
highscore_rect.center = (screen_size[0] / 2, screen_size[1] / 2 + 200)

# Game over Text
game_over_font = pygame.font.Font('assets/PressStart2P.ttf', 60)
game_over_text = game_over_font.render('GAMEOVER!', False, color_white)
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (screen_size[0] / 2, screen_size[1] / 2 - 150)

# Game over score text
score = 0
score_text = subtitle_font.render('Score: ' + str(score), False, color_white)
score_rect = score_text.get_rect()
score_rect.center = (screen_size[0] / 2, screen_size[1] / 2 + 150)

menu_open = True
game_open = True
end_screen_open = True
game_clock = pygame.time.Clock()
while menu_open:

    # Keystroke events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            menu_open = False
            game_open = False
            end_screen_open = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                menu_open = False
            if event.key == pygame.K_ESCAPE:
                menu_open = False
                game_open = False
                end_screen_open = False

    screen.blit(title_text, title_rect)
    screen.blit(play_text, play_rect)
    screen.blit(highscore_text, highscore_rect)

    game_clock.tick(10)
    pygame.display.update()
    highscore.close()

# Game Loop
while game_open:

    # Keystroke events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_open = False
            end_screen_open = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                if snake.get_direction() == 'UP' or snake.get_direction() == 'DOWN':
                    snake.set_direction('RIGHT')
            if event.key == pygame.K_LEFT:
                if snake.get_direction() == 'UP' or snake.get_direction() == 'DOWN':
                    snake.set_direction('LEFT')
            if event.key == pygame.K_UP:
                if snake.get_direction() == 'RIGHT' or snake.get_direction() == 'LEFT':
                    snake.set_direction('UP')
            if event.key == pygame.K_DOWN:
                if snake.get_direction() == 'RIGHT' or snake.get_direction() == 'LEFT':
                    snake.set_direction('DOWN')

    # Win condition checker
    if snake.on_player_collision():
        game_open = False

    elif snake.on_wall_collision():
        game_open = False

    # Normal game loop
    else:
        snake.on_player_collision()
        snake.on_apple_collision()
        snake.movement()

    # object rendering
    screen.fill(color_green)
    apple.blit()
    snake.blit()
    walls.blit()

    walls.score_blit()
    apple.get_points()
    score = apple.get_points()
    game_clock.tick(10)
    pygame.display.update()

# Game over screen
while end_screen_open:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end_screen_open = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE or event.key == pygame.K_END:
                end_screen_open = False

    screen.fill(color_black)
    score = apple.get_points()
    score_text = subtitle_font.render('Score: ' + str(score), False, color_white)
    screen.blit(game_over_text, game_over_rect)
    screen.blit(score_text, score_rect)

    pygame.display.update()
    game_clock.tick(10)

pygame.quit()
