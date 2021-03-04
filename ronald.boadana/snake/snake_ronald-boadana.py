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
pygame.display.set_caption('Snake v0.9')

# drawing snake
snake = [(200, 200), (230, 200), (260, 200)]
snake_head = pygame.image.load('../snake/assets/ronald.boadana_snakehead-right.png')
snake_body = pygame.Surface((30, 30))

# drawing apple
apple = pygame.image.load('../snake/assets/ronald.boadana_apple.png')
apple_pos = ((random.randint(60, 560) // 10 * 10), (random.randint(60, 560) // 10 * 10))

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
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3
direction = LEFT


def collision(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])


def apple_randomness_movement():
    apple_x = (random.randint(60, 560) // 10 * 10)
    apple_y = (random.randint(60, 560) // 10 * 10)
    return apple_x, apple_y


def draw_borders():
    pygame.draw.line(screen, color_white, [10, 50], [590, 50], 3)
    pygame.draw.line(screen, color_white, [10, 590], [590, 590], 3)
    pygame.draw.line(screen, color_white, [10, 50], [10, 590], 3)
    pygame.draw.line(screen, color_white, [590, 50], [590, 590], 3)


game_on = True
game_clock = pygame.time.Clock()
while game_on:
    game_clock.tick(90)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_on = False
        # mapping keys
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                direction = UP
            if event.key == pygame.K_s:
                direction = DOWN
            if event.key == pygame.K_a:
                direction = LEFT
            if event.key == pygame.K_d:
                direction = RIGHT

        # checking the score
        if player_score < max_score:

            if collision(snake[0], apple_pos):
                apple_pos = apple_randomness_movement()
                snake.append((600, 600))
                player_score += 1

            if direction == UP:
                snake[0] = (snake[0][0], snake[0][1] - 10)
                snake_head = pygame.image.load('../snake/assets/ronald.boadana_snakehead_up.png')
            if direction == DOWN:
                snake[0] = (snake[0][0], snake[0][1] + 10)
                snake_head = pygame.image.load('../snake/assets/ronald.boadana_snakehead.png')
            if direction == RIGHT:
                snake[0] = (snake[0][0] + 10, snake[0][1])
                snake_head = pygame.image.load('../snake/assets/ronald.boadana_snakehead-right.png')
            if direction == LEFT:
                snake[0] = (snake[0][0] - 10, snake[0][1])
                snake_head = pygame.image.load('../snake/assets/ronald.boadana_snakehead-left.png')

            for i in range(len(snake) - 1, 0, 1):
                snake[i] = (snake[i-1][0], snake[i-1][1])

            # updating score
            score_text = score_font.render('SCORE:' + str(player_score), True, color_white, color_black)

    # updating screen
    screen.blit(score_text, score_text_rect)
    screen.blit(apple, apple_pos)
    snake_body.fill((0, 0, 0))

    for pos in snake:
        screen.blit(snake_body, pos)
    screen.blit(snake_head, snake[0])

    # drawing the borders
    draw_borders()

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
