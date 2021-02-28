import pygame
import random  # randomness on apple positions

# game over sound available in https://freesound.org/people/EVRetro/sounds/533034/
# snake death sound available in https://freesound.org/people/jeckkech/sounds/391653/
# eating apple sound available in
# https://freesound.org/people/lulyc/sounds/346116/download/346116__lulyc__retro-game-heal-sound.wav
# victory sound available in https://freesound.org/people/honeybone82/sounds/513253/
# press key sound available in https://freesound.org/people/testing_player/sounds/243038/
# Powered by Ronald Boadana
# note: i added some lines as comments because there are somethings that i couldn't put on code

pygame.init()

# set the scores
max_score = 10
player_score = 0

# set the colors and screen
color_black = (0, 0, 0)
color_white = (255, 255, 255)
screen_size = (600, 600)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Snake v0.7.5')

# drawing snake
snake = pygame.image.load('../snake/assets/ronald.boadana_snakehead-right.png')
snake_x, snake_y = 150, 300
# snake_body = pygame.image.load('../snake/assets/ronald.boadana-snake-body-right-left.png')
# snake_x_body, snake_y_body = snake_x, snake_y - 30

# drawing apple
apple = pygame.image.load('../snake/assets/ronald.boadana_apple.png')
apple_x, apple_y = 400, 300

# sounds
game_over_sound = pygame.mixer.Sound('../snake/assets/game-over-sound.wav')
victory_sound = pygame.mixer.Sound('../snake/assets/victory-sound.wav')
eating_apple_sound = pygame.mixer.Sound('../snake/assets/eating-apple-sound.wav')
playing_sound = 0

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

# looping to make the key pressed move the snake
UP = DOWN = RIGHT = LEFT = False

game_on = True
game_clock = pygame.time.Clock()
while game_on:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_on = False
        # mapping keys
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                UP = True
            if event.key == pygame.K_s:
                DOWN = True
            if event.key == pygame.K_a:
                LEFT = True
            if event.key == pygame.K_d:
                RIGHT = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                UP = False
            if event.key == pygame.K_s:
                DOWN = False
            if event.key == pygame.K_a:
                LEFT = False
            if event.key == pygame.K_d:
                RIGHT = False

        # checking the score
        if player_score < max_score:
            screen.fill(color_black)
            if snake_x == apple_x and snake_y == apple_y:
                player_score += 1
                # snake_body = pygame.image.load('../snake/assets/ronald.boadana-snake-body-right-left.png')
                apple_x = (random.randint(60, 560) // 10 * 10)
                apple_y = (random.randint(60, 560) // 10 * 10)
                eating_apple_sound.play()

            # snake movement on key pressed
            if UP:
                snake_y -= 10
                snake = pygame.image.load('../snake/assets/ronald.boadana_snakehead_up.png')
            else:
                snake_y += 0
            if DOWN:
                snake_y += 10
                snake = pygame.image.load('../snake/assets/ronald.boadana_snakehead.png')
            else:
                snake_y += 0
            if RIGHT:
                snake_x += 10
                snake = pygame.image.load('../snake/assets/ronald.boadana_snakehead-right.png')
                # snake_body = pygame.image.load('../snake/assets/ronald.boadana-snake-body-right-left.png')
            else:
                snake_x += 0
            if LEFT:
                snake_x -= 10
                snake = pygame.image.load('../snake/assets/ronald.boadana_snakehead-left.png')
                # snake_body = pygame.image.load('../snake/assets/ronald.boadana-snake-body-right-left.png')
            else:
                snake_x += 0

            # updating score
            score_text = score_font.render('SCORE:' + str(player_score), True, color_white, color_black)

    # updating screen
    screen.blit(score_text, score_text_rect)
    screen.blit(snake, (snake_x, snake_y))
    screen.blit(apple, (apple_x, apple_y))
    # screen.blit(snake_body, (snake_x_body, snake_y_body))

    # drawing the borders
    pygame.draw.line(screen, color_white, [10, 50], [590, 50], 3)
    pygame.draw.line(screen, color_white, [10, 590], [590, 590], 3)
    pygame.draw.line(screen, color_white, [10, 50], [10, 590], 3)
    pygame.draw.line(screen, color_white, [590, 50], [590, 590], 3)

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
        if playing_sound == 0:
            game_over_sound.play()
            playing_sound += 1

    # victory condition
    if player_score == 10:
        screen.fill(color_black)
        screen.blit(victory_text, victory_text_rect)
        if playing_sound == 0:
            victory_sound.play()
            playing_sound += 1

    # updating screen
    pygame.display.flip()
    screen.fill(color_black)
    game_clock.tick(90)

pygame.quit()
