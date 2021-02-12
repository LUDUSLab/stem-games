import pygame
import random  # for ball randomness and 'A.I.' loss any concentration
# Powered by Ronald Boadana

pygame.init()

COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)

SCORE_MAX = 10

size = (1280, 720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong 2.0 (Beta 1.1) - PyGame Edition - 2021.02.12")

# score text
score_font = pygame.font.Font('../assets/PressStart2P.ttf', 44)
score_text = score_font.render('00 x 00', True, COLOR_WHITE, COLOR_BLACK)
score_text_rect = score_text.get_rect()
score_text_rect.center = (680, 50)

# victory text
victory_font = pygame.font.Font('../assets/PressStart2P.ttf', 100)
victory_text = victory_font.render('VICTORY', True, COLOR_WHITE, COLOR_BLACK)
victory_text_rect = score_text.get_rect()
victory_text_rect.center = (450, 350)

# defeat text (when A.I. wins the game)
defeat_font = pygame.font.Font('../assets/PressStart2P.ttf', 100)
defeat_text = victory_font.render('GAME OVER', True, COLOR_WHITE, COLOR_BLACK)
defeat_text_rect = score_text.get_rect()
defeat_text_rect.center = (350, 350)

# sound effects
bounce_sound_effect = pygame.mixer.Sound('../assets/bounce.wav')
scoring_sound_effect = pygame.mixer.Sound('../assets/258020__kodack__arcade-bleep-sound.wav')

# player 1
player_1 = pygame.image.load('../assets/ronald.boadana_paddle.png')
player_1_y = 300
player_1_move_up = False
player_1_move_down = False

# 'A.I.'
ai_player = pygame.image.load('../assets/ronald.boadana_paddle.png')
ai_player_y = 300

# ball
ball = pygame.image.load('../assets/ronald.boadana_ball.png')
ball_x, ball_y = 640, 360
ball_speed_x = ball_speed_y = 5

# score
score_1 = ai_score = 0

# game loop
game_loop = True
game_clock = pygame.time.Clock()

while game_loop:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop = False

        # keystroke events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player_1_move_up = True
            if event.key == pygame.K_s:
                player_1_move_down = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                player_1_move_up = False
            if event.key == pygame.K_s:
                player_1_move_down = False

    # checking the victory condition
    if score_1 < SCORE_MAX and ai_score < SCORE_MAX:

        # clear screen
        screen.fill(COLOR_BLACK)
        # ball movement
        ball_x += ball_speed_x
        ball_y += ball_speed_y

        # ball collision with the wall
        if ball_y > 700:
            ball_speed_y *= -1
            bounce_sound_effect.play()
        elif ball_y <= 0:
            ball_speed_y *= -1
            bounce_sound_effect.play()

        # ball collision with the player 1 's paddle
        if (ball_x == 60) and (player_1_y < ball_y + 25) and (player_1_y + 150 > ball_y):
            ball_speed_x *= -1
            ball_speed_y = random.randrange(-15, 16)
            bounce_sound_effect.play()

        # ball collision with the player 2 's paddle
        if (ball_x == 1190) and (ai_player_y < ball_y + 25) and (ai_player_y + 150 > ball_y):
            ball_speed_x *= -1
            ball_speed_y = random.randrange(-15, 16)
            bounce_sound_effect.play()

        # player 2 scores points
        if ball_x < -50:
            ball_x = 640
            ball_y = 360
            ball_speed_y *= -1
            ball_speed_x *= -1
            ai_score += 1
            scoring_sound_effect.play()
        # player 1 scores point
        elif ball_x > 1280:
            ball_x = 640
            ball_y = 360
            ball_speed_y *= -1
            ball_speed_x *= -1
            score_1 += 1
            scoring_sound_effect.play()

        # player 1 up movement
        if player_1_move_up:
            player_1_y -= 10
        else:
            player_1_y += 0

        # player 1 down movement
        if player_1_move_down:
            player_1_y += 10
        else:
            player_1_y += 0

        # player 1 collides with upper wall
        if player_1_y <= 0:
            player_1_y = 0

        # player 1 collides with lower wall
        elif player_1_y >= 570:
            player_1_y = 570

        # "Artificial Intelligence" loss concentration sometimes
        if (ball_y < 0) or (ball_y < ai_player_y + 10) and random.randrange(31) == 10:
            ai_player_y = ball_y - 15
        if (ball_y > 0) or (ball_y > ai_player_y - 10) and random.randrange(31) == 10:
            ai_player_y = ball_y + 15

        # 'A.I.' collides with upper wall
        if ai_player_y <= 0:
            ai_player_y = 0

        # 'A.I.' collides with lover wall
        elif ai_player_y >= 570:
            ai_player_y = 570

        # update score hud
        score_text = score_font.render(str(score_1) + ' x ' + str(ai_score), True, COLOR_WHITE, COLOR_BLACK)

        # drawing objects
        screen.blit(ball, (ball_x, ball_y))
        screen.blit(player_1, (50, player_1_y))
        screen.blit(ai_player, (1200, ai_player_y))
        screen.blit(score_text, score_text_rect)
    else:
        # drawing victory
        screen.fill(COLOR_BLACK)
        # when the player wins
        if score_1 == 10:
            screen.blit(victory_text, victory_text_rect)
        # when the 'A.I.' wins
        elif ai_score == 10:
            screen.blit(defeat_text, defeat_text_rect)

    # update screen
    pygame.display.flip()
    game_clock.tick(90)

pygame.quit()
