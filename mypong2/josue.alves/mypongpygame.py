import pygame
import random
import math

aux = [30, 45, 60, -30, -45, -60]

pygame.init()

COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)

SCORE_MAX = 2

size = (1280, 700)
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
player_1 = pygame.image.load("../assets/josue.alves_paddle.png")
player_1_y = 300
player_1_move_up = False
player_1_move_down = False

# player 2 - robot
player_2 = pygame.image.load("../assets/josue.alves_paddle.png")
player_2_y = 360

# ball
ball = pygame.image.load("../assets/josue.alves_ball.png")
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


def scoring_points():
    global ball_x, ball_y, ball_dy, ball_dx
    ball_x = 640
    ball_y = 360
    ball_dy *= -1
    ball_dx *= -1
    scoring_sound_effect.play()


def draw():
    screen.blit(ball, (ball_x, ball_y))
    screen.blit(player_1, (50, player_1_y))
    screen.blit(player_2, (1180, player_2_y))
    screen.blit(score_text, score_text_rect)


def draw_victory():
    screen.fill(COLOR_BLACK)
    screen.blit(score_text, score_text_rect)
    screen.blit(victory_text, victory_text_rect)


def ball_collision_with_paddle():
    global ball_dx, ball_dy
    ball_dx *= -1
    ball_dy *= -1
    bounce_sound_effect.play()


while game_loop:

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

    # checking the victory condition
    if score_1 < SCORE_MAX and score_2 < SCORE_MAX:

        # clear screen
        screen.fill(COLOR_BLACK)

        # ball collision with the wall
        if ball_y >= 700:
            ball_dy *= -1
            bounce_sound_effect.play()
        elif ball_y <= 0:
            ball_dy *= -1
            bounce_sound_effect.play()

        # ball collision with the player 1 's paddle
        if 90 > ball_x > 50 and player_1_y < ball_y + 25 and player_1_y + 150 > ball_y:
            if (player_1_y + 30 >= ball_y >= player_1_y - 20) or (player_1_y + 110 >= ball_y >= player_1_y + 150):
                ball_dx *= -1
                ball_dy *= -math.tan(math.radians(random.choice(aux)))
                bounce_sound_effect.play()
            else:
                ball_collision_with_paddle()

        # ball collision with the player 2 's paddle
        if 1150 < ball_x < 1190 and player_2_y < ball_y + 25 and player_2_y + 150 > ball_y:
            if (player_2_y + 30 >= ball_y >= player_2_y - 20) or (player_2_y + 110 >= ball_y >= player_2_y + 150):
                ball_dx *= -1
                ball_dy *= -math.tan(math.radians(random.choice(aux)))
                bounce_sound_effect.play()
            else:
                ball_collision_with_paddle()

        # scoring points
        if ball_x <= 0:
            scoring_points()
            score_2 += 1
        elif ball_x >= 1320:
            scoring_points()
            score_1 += 1

        # ball movement
        ball_x = ball_x + ball_dx
        ball_y = ball_y + ball_dy

        # player 1 up movement
        if player_1_move_up:
            player_1_y -= 7
        else:
            player_1_y += 0

        # player 1 down movement
        if player_1_move_down:
            player_1_y += 7
        else:
            player_1_y += 0

        # player 1 collides with upper wall
        if player_1_y <= 0:
            player_1_y = 0

        # player 1 collides with lower wall
        elif player_1_y >= 560:
            player_1_y = 560

        # AI
        if player_2_y > ball_y:
            player_2_y -= 7

        if player_2_y + 160 < ball_y:
            player_2_y += 7

        # player 2 collides with upper wall
        if player_2_y <= 0:
            player_2_y = 0

        # player 2 collides with lower wall
        elif player_2_y >= 560:
            player_2_y = 560

        # update score hud
        score_text = score_font.render(str(score_1) + ' x ' + str(score_2), True, COLOR_WHITE, COLOR_BLACK)

        # drawing objects
        draw()

    else:
        # drawing victory
        draw_victory()

    # update screen
    pygame.display.flip()
    game_clock.tick(60)

pygame.quit()
