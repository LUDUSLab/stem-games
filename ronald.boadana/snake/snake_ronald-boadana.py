import pygame
import random  # randomness on apple positions

# Powered by Ronald Boadana
# game over sound available in https://freesound.org/people/EVRetro/sounds/533034/
# snake death sound available in https://freesound.org/people/jeckkech/sounds/391653/
# eating apple sound available in
# https://freesound.org/people/lulyc/sounds/346116/download/346116__lulyc__retro-game-heal-sound.wav

pygame.init()

# set the scores
max_score = 10
player_score = 0

# set the colors and screen
color_black = (0, 0, 0)
color_white = (255, 255, 255)
screen_size = (600, 600)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Snake v0.7')

# drawing snake
snake = pygame.image.load('../snake/assets/ronald.boadana_snakehead.png')
snake_x, snake_y = 300, 300

# drawing apple
apple = pygame.image.load('../snake/assets/ronald.boadana_apple.png')
apple_x = (random.randint(50, 560) // 10 * 10)
apple_y = (random.randint(50, 560) // 10 * 10)

# sounds
game_over_sound = pygame.mixer.Sound('../snake/assets/game-over-sound.wav')
eating_apple_sound = pygame.mixer.Sound('../snake/assets/eating-apple-sound.wav')
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

# conditions to snake can move
direction_x, direction_y = 10, 10

game_on = True
game_clock = pygame.time.Clock()
while game_on:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_on = False
        # mapping keys
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                snake_y -= direction_y
                snake = pygame.image.load('../snake/assets/ronald.boadana_snakehead_up.png')
            if event.key == pygame.K_s:
                snake_y += direction_y
                snake = pygame.image.load('../snake/assets/ronald.boadana_snakehead.png')
            if event.key == pygame.K_a:
                snake_x -= direction_x
                snake = pygame.image.load('../snake/assets/ronald.boadana_snakehead-left.png')
            if event.key == pygame.K_d:
                snake_x += direction_x
                snake = pygame.image.load('../snake/assets/ronald.boadana_snakehead-right.png')
        print(snake_x, snake_y)
        print(apple_x, apple_y)

    # checking the score
        if player_score < max_score:
            screen.fill(color_black)
            if snake_x == apple_x and snake_y == apple_y:
                player_score += 1
                apple_x = (random.randint(50, 560) // 10 * 10)
                apple_y = (random.randint(50, 560) // 10 * 10)
                eating_apple_sound.play()
                print(player_score)

        # updating score
        score_text = score_font.render('SCORE:' + str(player_score), True, color_white, color_black)

    # updating screen
    screen.blit(score_text, score_text_rect)
    screen.blit(snake, (snake_x, snake_y))
    screen.blit(apple, (apple_x, apple_y))

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

    # updating screen
    pygame.display.flip()
    screen.fill(color_black)
    game_clock.tick(90)

pygame.quit()
