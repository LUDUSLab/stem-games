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
snake = [(200, 200), (220, 200), (240, 200)]
snake_head = pygame.image.load('../snake/assets/ronald.boadana_snakehead.png')
snake_head = pygame.transform.scale(snake_head, [20, 20])
snake_body = pygame.image.load('../snake/assets/ronald.boadana_snake_body_up_down.png')
snake_body = pygame.transform.scale(snake_body, [20, 20])

# drawing apple
apple = pygame.image.load('../snake/assets/ronald.boadana_apple.png')
apple = pygame.transform.scale(apple, [20, 20])
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


# apple randomness positions
def apple_randomness_movement():
    apple_x = (random.randint(60, 560) // 10 * 10)
    apple_y = (random.randint(60, 560) // 10 * 10)
    return apple_x, apple_y


# drawing the borders
def draw_borders():
    pygame.draw.line(screen, color_white, [10, 50], [590, 50], 3)
    pygame.draw.line(screen, color_white, [10, 590], [590, 590], 3)
    pygame.draw.line(screen, color_white, [10, 50], [10, 590], 3)
    pygame.draw.line(screen, color_white, [590, 50], [590, 590], 3)


game_on = True
game_clock = pygame.time.Clock()
while game_on:
    game_clock.tick(15)
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
        if snake[0] == apple_pos:
            apple_pos = apple_randomness_movement()
            eating_apple_sound.play()
            snake.append((600, 600))
            player_score += 1

        # updating score
        score_text = score_font.render('SCORE:' + str(player_score), True, color_white, color_black)

    # defeat condition
    if (snake[0][0] < 0) or (snake[0][1] < 40) or (snake[0][0] > 570) or (snake[0][1] > 570):
        screen.fill(color_black)
        screen.blit(defeat_text, defeat_text_rect)
        if playing_sound == 0:
            game_over_sound.play()
            playing_sound += 1

    # victory condition
    elif player_score == 10:
        screen.fill(color_black)
        screen.blit(victory_text, victory_text_rect)
        if playing_sound == 0:
            victory_sound.play()
            playing_sound += 1

    else:
        if direction == UP:
            snake[0] = (snake[0][0], snake[0][1] - 10)
            snake_head = pygame.image.load('../snake/assets/ronald.boadana_snakehead_up.png')
            snake_head = pygame.transform.scale(snake_head, [20, 20])
            snake_body = pygame.image.load('../snake/assets/ronald.boadana_snake_body_up_down.png')
            snake_body = pygame.transform.scale(snake_body, [20, 20])
            for i in range(len(snake) - 1, 0, -1):
                snake[i] = (snake[i - 1][0], snake[i - 1][1])
        if direction == DOWN:
            snake[0] = (snake[0][0], snake[0][1] + 10)
            snake_head = pygame.image.load('../snake/assets/ronald.boadana_snakehead.png')
            snake_head = pygame.transform.scale(snake_head, [20, 20])
            snake_body = pygame.image.load('../snake/assets/ronald.boadana_snake_body_up_down.png')
            snake_body = pygame.transform.scale(snake_body, [20, 20])
            for i in range(len(snake) - 1, 0, -1):
                snake[i] = (snake[i - 1][0], snake[i - 1][1])
        if direction == RIGHT:
            snake[0] = (snake[0][0] + 10, snake[0][1])
            snake_head = pygame.image.load('../snake/assets/ronald.boadana_snakehead-right.png')
            snake_head = pygame.transform.scale(snake_head, [20, 20])
            snake_body = pygame.image.load('../snake/assets/ronald.boadana_snake_body_right_left.png')
            snake_body = pygame.transform.scale(snake_body, [20, 20])
            for i in range(len(snake) - 1, 0, -1):
                snake[i] = (snake[i - 1][0], snake[i - 1][1])
        if direction == LEFT:
            snake[0] = (snake[0][0] - 10, snake[0][1])
            snake_head = pygame.image.load('../snake/assets/ronald.boadana_snakehead-left.png')
            snake_head = pygame.transform.scale(snake_head, [20, 20])
            snake_body = pygame.image.load('../snake/assets/ronald.boadana_snake_body_right_left.png')
            snake_body = pygame.transform.scale(snake_body, [20, 20])
            for i in range(len(snake) - 1, 0, -1):
                snake[i] = (snake[i - 1][0], snake[i - 1][1])

        # updating screen
        screen.blit(score_text, score_text_rect)
        screen.blit(apple, apple_pos)

        for pos in snake:
            screen.blit(snake_body, pos)
        screen.blit(snake_head, snake[0])

        # drawing the borders
        draw_borders()

    # updating screen
    pygame.display.update()
    screen.fill(color_black)

pygame.quit()
