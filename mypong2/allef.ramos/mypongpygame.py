import pygame
from random import choice

pygame.init()

COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)

SCORE_MAX = 2

size = (1280, 720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("MyPong - PyGame Edition - 2021.01.30")

# score text
score_font = pygame.font.Font('../assets/PressStart2P.ttf', 44)
score_text = score_font.render('00 x 00', True, COLOR_WHITE, COLOR_BLACK)
score_text_rect = score_text.get_rect()
score_text_rect.center = (680, 50)

# victory text
victory_font = pygame.font.Font('../assets/PressStart2P.ttf', 100)
victory_text = victory_font .render('VICTORY', True, COLOR_WHITE, COLOR_BLACK)
victory_text_rect = score_text.get_rect()
victory_text_rect.center = (450, 350)

# sound effects
bounce_sound_effect = pygame.mixer.Sound('../assets/bounce.wav')
scoring_sound_effect = pygame.mixer.Sound('../assets/258020__kodack__arcade-bleep-sound.wav')

# player 1
player_1 = pygame.image.load("../assets/allef.ramos.paddle.png")
player_1_y = 300
player_1_move_up = False
player_1_move_down = False

# player 2 - robot
player_2 = pygame.image.load("../assets/allef.ramos.paddle.png")
player_2_y = 300

# ball
ball = pygame.image.load("../assets/allef.ramos.ball.png")
ball_x = 640
ball_y = 360
ball_dx = 7
ball_dy = 7

# score
score_1 = 0
score_2 = 0

# game loop
game_loop = True
game_clock = pygame.time.Clock()


def keystroke_events():
    global game_loop, player_1_move_up, player_1_move_down
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop = False

        #  keystroke events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_1_move_up = True
            if event.key == pygame.K_DOWN:
                player_1_move_down = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player_1_move_up = False
            if event.key == pygame.K_DOWN:
                player_1_move_down = False


def players_movement():
    global player_1_move_down, player_1_move_up, player_1_y, player_2_y
    # player 1 up movement
    if player_1_move_up:
        player_1_y -= 6
    else:
        player_1_y += 0

    # player 1 down movement
    if player_1_move_down:
        player_1_y += 6
    else:
        player_1_y += 0

    # player 1 collides with upper wall
    if player_1_y <= 0:
        player_1_y = 0

    # player 1 collides with lower wall
    elif player_1_y >= 560:
        player_1_y = 560

    # player 2 "Artificial Intelligence"
    if ball_y - 15 > (player_2_y + 70) and player_2_y < 560:
        player_2_y += 6
    if ball_y - 15 < player_2_y and player_2_y > 0:
        player_2_y -= 6


def ball_animation():
    global ball_dy, ball_dx, ball_x, ball_y

    # ball collision with the wall
    if ball_y > 700:
        ball_dy *= -1
        bounce_sound_effect.play()

    if ball_y <= 0:
        ball_dy *= -1
        bounce_sound_effect.play()

    # ball collision with the player 1 's paddle
    if (50 <= ball_x <= 82) and (player_1_y < ball_y + 30) and (player_1_y + 160 > ball_y):
        ball_x = 82
        if player_1_y + 45 < ball_y < player_1_y + 75:
            ball_dy = choice([4, 3]) * choice([-1, 1])
            ball_dx = 15
        else:
            ball_dy = 5 * choice([-1, 1]) * choice([1, 1.2, 1.5])
            ball_dx = 5 * choice([1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7])
        bounce_sound_effect.play()

    # ball collision with the player 2 's paddle
    if (1180 >= ball_x >= 1148) and (player_2_y < ball_y + 30) and (player_2_y + 160 > ball_y):
        ball_x = 1148
        if player_2_y + 45 < ball_y < player_2_y + 75:
            ball_dy = choice([4, 3]) * choice([-1, 1])
            ball_dx = -15
        else:
            ball_dy = 5 * choice([-1, 1]) * choice([1, 1.2, 1.5])
            ball_dx = -5 * choice([1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7])
        bounce_sound_effect.play()

    ball_x = ball_x + ball_dx
    ball_y = ball_y + ball_dy


def scoring_points():
    global score_1, score_2, ball_x, ball_y, ball_dy, ball_dx
    if ball_x < -50:
        ball_x = 640
        ball_y = 360
        ball_dy = -5
        ball_dx = -5
        score_2 += 1
        scoring_sound_effect.play()
    elif ball_x > 1320:
        ball_x = 640
        ball_y = 360
        ball_dy = 5
        ball_dx = 5
        score_1 += 1
        scoring_sound_effect.play()


def draw():
    screen.blit(ball, (ball_x, ball_y))
    screen.blit(player_1, (50, player_1_y))
    screen.blit(player_2, (1180, player_2_y))
    screen.blit(score_text, score_text_rect)


while game_loop:

    keystroke_events()

    # checking the victory condition
    if score_1 < SCORE_MAX and score_2 < SCORE_MAX:

        # clear screen
        screen.fill(COLOR_BLACK)

        #ball interact whit other objects
        ball_animation()

        #score
        scoring_points()

        #paddles
        players_movement()

        #update score hud
        score_text = score_font.render(str(score_1) + ' x ' + str(score_2), True, COLOR_WHITE, COLOR_BLACK)

        # drawing objects
        draw()
    else:
        # drawing victory
        screen.fill(COLOR_BLACK)
        screen.blit(score_text, score_text_rect)
        screen.blit(victory_text, victory_text_rect)

    # update screen
    pygame.display.flip()
    game_clock.tick(60)

pygame.quit()
