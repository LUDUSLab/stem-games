import pygame

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
player_1_img = pygame.image.load("../assets/natanael.lucena_paddle.png")
player_1 = player_1_img.get_rect()
player_1.x = 70
player_1.y = 310
player_1_move_up = False
player_1_move_down = False

# player 2 - robot
player_2_img = pygame.image.load("../assets/natanael.lucena_paddle.png")
player_2 = player_2_img.get_rect()
player_2.x = 1180
player_2.y = 310

# ball
ball = pygame.image.load("../assets/natanael.lucena_ball.png")
ball_x = 640
ball_y = 360
ball_dx = 5
ball_dy = 5

# score
score_1 = 0
score_2 = 0

# game loop
game_loop = True
game_clock = pygame.time.Clock()

while game_loop:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop = False

        #  keystroke events
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
    if score_1 < SCORE_MAX and score_2 < SCORE_MAX:

        # clear screen
        screen.fill(COLOR_BLACK)

        # ball collision with the wall
        if ball_y > 700:
            ball_dy *= -1
            bounce_sound_effect.play()
        elif ball_y <= 0:
            ball_dy *= -1
            bounce_sound_effect.play()

        # ball collision with the player 1 's paddle
        if 100 > ball_x > 70:
            if player_1.y < ball_y + 30:
                if player_1.y + 150 > ball_y:
                    ball_dx *= -1
                    bounce_sound_effect.play()

        # ball collision with the player 2 's paddle
        if 1190 > ball_x > 1160:
            if player_2.y < ball_y + 30:
                if player_2.y + 150 > ball_y:
                    ball_dx *= -1
                    bounce_sound_effect.play()

        # scoring points
        if ball_x < -50:
            ball_x = 640
            ball_y = 360
            ball_dy *= -1
            ball_dx *= -1
            score_2 += 1
            scoring_sound_effect.play()
        elif ball_x > 1320:
            ball_x = 640
            ball_y = 360
            ball_dy *= -1
            ball_dx *= -1
            score_1 += 1
            scoring_sound_effect.play()

        # ball movement
        ball_x = ball_x + ball_dx
        ball_y = ball_y + ball_dy

        # player 1 up movement
        if player_1_move_up:
            player_1.y -= 5
        else:
            player_1.y += 0

        # player 1 down movement
        if player_1_move_down:
            player_1.y += 5
        else:
            player_1.y += 0

        # player 1 collides with upper wall
        if player_1.y <= 0:
            player_1.y = 0

        # player 1 collides with lower wall
        elif player_1.y >= 570:
            player_1.y = 570

        # player 2 "Artificial Intelligence"
        player_2.y = ball_y
        if player_2.y <= 0:
            player_2.y = 0
        elif player_2.y >= 570:
            player_2.y = 570

        # update score hud
        score_text = score_font.render(str(score_1) + ' x ' + str(score_2), True, COLOR_WHITE, COLOR_BLACK)

        # drawing objects
        screen.blit(ball, (ball_x, ball_y))
        screen.blit(player_1_img, player_1)
        screen.blit(player_2_img, player_2)
        screen.blit(score_text, score_text_rect)
    else:
        # drawing victory
        screen.fill(COLOR_BLACK)
        screen.blit(score_text, score_text_rect)
        screen.blit(victory_text, victory_text_rect)

    # update screen
    pygame.display.flip()
    game_clock.tick(60)

pygame.quit()
