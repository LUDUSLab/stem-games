import pygame
from random import uniform

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
player_1.y = 300
player_1_move_up = False
player_1_move_down = False

# player 2 - robot
player_2_img = pygame.image.load("../assets/natanael.lucena_paddle.png")
player_2 = player_2_img.get_rect()
player_2.x = 1180
player_2.y = 300

# ball
ball_img = pygame.image.load("../assets/natanael.lucena_ball.png")
ball = ball_img.get_rect()
ball.x = 640
ball.y = 360
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
        if ball.y > 700:
            ball_dy *= -1
            bounce_sound_effect.play()
        elif ball.y <= 0:
            ball_dy *= -1
            bounce_sound_effect.play()

        collision_tolerance = 10
        if ball.colliderect(player_1) and ball_dx < 0:
            if abs(player_1.top - ball.bottom) < collision_tolerance and ball_dy > 0:
                ball_dy *= -1
            if abs(player_1.bottom - ball.top) < collision_tolerance and ball_dy < 0:
                ball_dy *= -1
            if abs(player_1.right - ball.left) < collision_tolerance:
                if player_1_move_down:
                    ball_dy = uniform(1, 2.14)*5
                elif player_1_move_up:
                    ball_dy = uniform(-2.14, -1)*5
            if player_1.bottomright[1]/3 <= ball.y <= player_1.bottomright[1]/1.5:
                ball_dx = uniform(5, 6)
            else:
                ball_dx = uniform(5, 10)
            bounce_sound_effect.play()

        # ball collision with the player 2 's paddle
        if ball.colliderect(player_2) and ball_dx > 0:
            if abs(player_2.top - ball.bottom) < collision_tolerance and ball_dy > 0:
                ball_dy *= -1
            if abs(player_2.bottom - ball.top) < collision_tolerance and ball_dy < 0:
                ball_dy *= -1
            if abs(player_2.left - ball.right) < collision_tolerance:
                if player_1_move_down:
                    ball_dy = uniform(1, 2.14)*5
                elif player_1_move_up:
                    ball_dy = uniform(-2.14, -1)*5
            if player_2.bottomright[1] / 3 <= ball.y <= player_2.bottomright[1] / 1.5:
                ball_dx = uniform(-6, -5)
            else:
                ball_dx = uniform(-10, -5)
            bounce_sound_effect.play()

        # scoring points
        if ball.x < -50:
            ball.x = 640
            ball.y = 360
            ball_dy *= -1
            ball_dx *= -1
            score_2 += 1
            scoring_sound_effect.play()
        elif ball.x > 1320:
            ball.x = 640
            ball.y = 360
            ball_dy *= -1
            ball_dx *= -1
            score_1 += 1
            scoring_sound_effect.play()

        # ball movement
        ball.x = ball.x + ball_dx
        ball.y = ball.y + ball_dy

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
        player_2.y = ball.y
        if player_2.y <= 0:
            player_2.y = 0
        elif player_2.y >= 570:
            player_2.y = 570

        # update score hud
        score_text = score_font.render(str(score_1) + ' x ' + str(score_2), True, COLOR_WHITE, COLOR_BLACK)

        # drawing objects
        screen.blit(ball_img, ball)
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
