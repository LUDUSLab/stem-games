import pygame
import random  # randomness on apple positions

# game over sound available in https://freesound.org/people/EVRetro/sounds/533034/
# snake death sound available in https://freesound.org/people/jeckkech/sounds/391653/
# eating apple sound available in
# https://freesound.org/people/lulyc/sounds/346116/download/346116__lulyc__retro-game-heal-sound.wav
# victory sound available in https://freesound.org/people/honeybone82/sounds/513253/
# press key sound available in https://freesound.org/people/testing_player/sounds/243038/
# Powered by Ronald Boadana
# note: somethings is using '#' because it's things that i'll add on game, but from now i didn't get

pygame.init()

# set the scores
max_score = 10
player_score = 0

# set the colors and screen
color_black = (0, 0, 0)
color_white = (255, 255, 255)
screen_size = (600, 600)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Snake v0.7.1')

# drawing snake
snake = pygame.image.load('../snake/assets/ronald.boadana_snakehead.png')
snake_x, snake_y = 300, 300
# snake_body_up_down = pygame.image.load('../snake/assets/ronald.boadana-snake-body-up-down.png')
# snake_x_body_up_down, snake_y_body_up_down = (snake_x, snake_y - 30)
# snake_tail = pygame.image.load('../snake/assets/ronald.boadana-snake-tail.png')
# snake_tail_x, snake_tail_y = (snake_x + 4, snake_y_body_up_down - 30)

# drawing apple
apple = pygame.image.load('../snake/assets/ronald.boadana_apple.png')
apple_x = (random.randint(50, 560) // 10 * 10)
apple_y = (random.randint(50, 560) // 10 * 10)

# sounds
game_over_sound = pygame.mixer.Sound('../snake/assets/game-over-sound.wav')
victory_sound = pygame.mixer.Sound('../snake/assets/victory-sound.wav')
eating_apple_sound = pygame.mixer.Sound('../snake/assets/eating-apple-sound.wav')
press_key_sound = pygame.mixer.Sound('../snake/assets/press-key-sound.wav')
# snake_death_sound = pygame.mixer.Sound('../snake/assets/snake-death-sound.wav')

# score text
score_font = pygame.font.Font('../snake/assets/PressStart2P.ttf', 30)
score_text = score_font.render('0', True, color_white, color_black)
score_text_rect = score_text.get_rect()
score_text_rect.center = (210, 25)

# defeat text
defeat_font = pygame.font.Font('../snake/assets/PressStart2P.ttf', 30)
defeat_text = defeat_font.render('GAME OVER', True, color_white, color_black)
defeat_text_rect = score_text.get_rect()
defeat_text_rect.center = (175, 275)

# victory text
victory_font = pygame.font.Font('../snake/assets/PressStart2P.ttf', 30)
victory_text = defeat_font.render('VICTORY!', True, color_white, color_black)
victory_text_rect = score_text.get_rect()
victory_text_rect.center = (200, 275)

game_on = True
game_clock = pygame.time.Clock()
while game_on:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_on = False
        # mapping keys
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                snake_y -= 10
                press_key_sound.play()
                snake = pygame.image.load('../snake/assets/ronald.boadana_snakehead_up.png')
            if event.key == pygame.K_s:
                snake_y += 10
                press_key_sound.play()
                # snake_y_body += direction_y
                # snake_tail_y += direction_y
                snake = pygame.image.load('../snake/assets/ronald.boadana_snakehead.png')
            if event.key == pygame.K_a:
                snake_x -= 10
                press_key_sound.play()
                # snake_x_body -= direction_x
                # snake_tail_x -= direction_x
                snake = pygame.image.load('../snake/assets/ronald.boadana_snakehead-left.png')
            if event.key == pygame.K_d:
                snake_x += 10
                press_key_sound.play()
                # snake_x_body += direction_x
                # snake_tail_x += direction_x
                snake = pygame.image.load('../snake/assets/ronald.boadana_snakehead-right.png')

        # checking the score
        if player_score < max_score:
            screen.fill(color_black)
            if snake_x == apple_x and snake_y == apple_y:
                player_score += 1
                apple_x = (random.randint(50, 560) // 10 * 10)
                apple_y = (random.randint(50, 560) // 10 * 10)
                eating_apple_sound.play()

        # updating score
        score_text = score_font.render('SCORE:' + str(player_score), True, color_white, color_black)

    # updating screen
    screen.blit(score_text, score_text_rect)
    screen.blit(snake, (snake_x, snake_y))
    screen.blit(apple, (apple_x, apple_y))

    # drawing the borders
    pygame.draw.line(screen, color_white, [10, 50], [590, 50], 3)
    pygame.draw.line(screen, color_white, [10, 580], [590, 580], 3)
    pygame.draw.line(screen, color_white, [10, 50], [10, 580], 3)
    pygame.draw.line(screen, color_white, [590, 50], [590, 580], 3)
    # screen.blit(snake_body, (snake_x_body, snake_y_body))
    # screen.blit(snake_tail, (snake_tail_x, snake_tail_y))

    # snake collision with 'x' coordinate
    if snake_x <= 0:
        snake_x = 0
    elif snake_x >= 570:
        snake_x = 570

    # snake collision with 'y' coordinate
    if snake_y <= 40:
        snake_y = 40
    elif snake_y >= 570:
        snake_y = 570

    # defeat condition
    if (snake_x == 0) or (snake_y == 40) or (snake_x == 570) or (snake_y == 570):
        screen.fill(color_black)
        screen.blit(defeat_text, defeat_text_rect)
        game_over_sound.play()

    # victory condition
    if player_score == 10:
        screen.fill(color_black)
        screen.blit(victory_text, victory_text_rect)
        victory_sound.play()

    # updating screen
    pygame.display.flip()
    screen.fill(color_black)
    game_clock.tick(120)

pygame.quit()
