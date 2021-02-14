import pygame

pygame.init()

COLOR_BLACK = (20, 20, 20)
COLOR_WHITE = (255, 255, 255)

SCORE_MAX = 2

size = (1280, 720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("MyPong - PyGame Edition - Matheus Nielsen - Versão 0.2.1")

# score text
score_font = pygame.font.Font('D:/Meus Documentos/Documentos/GitHub/stem-games/mypong2/assets/PressStart2P.ttf', 44)
score_text = score_font.render('00 x 00', False, COLOR_WHITE)
score_text_rect = score_text.get_rect()
score_text_rect.center = (680, 50)

# sound effects
bounce_sound_effect = pygame.mixer.Sound('D:/Meus Documentos/Documentos/GitHub/stem-games/mypong2/assets/bounce.wav')
scoring_sound_effect = pygame.mixer.Sound('D:/Meus Documentos/Documentos/GitHub/stem-games/mypong2/assets/258020__'
                                          'kodack__arcade-bleep-sound.wav')

# player 1
player_1 = pygame.image.load("D:/Meus Documentos/Documentos/GitHub/stem-games/mypong2/assets/"
                             "matheus.nielsen_Paddle_Player.png")
player_1_y = 300
player_1_move_up = False
player_1_move_down = False

# player 2 - robot
player_2 = pygame.image.load("D:/Meus Documentos/Documentos/GitHub/stem-games/mypong2/assets/"
                             "matheus.nielsen_Paddle_AI.png")
player_2_y = 300

# ball
ball_ai = "D:/Meus Documentos/Documentos/GitHub/stem-games/mypong2/assets/matheus.nielsen_Ball_AI.png"
ball_player = "D:/Meus Documentos/Documentos/GitHub/stem-games/mypong2/assets/matheus.nielsen_Ball_Player.png"
ball = pygame.image.load(ball_ai)
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


def endgame(text):
    # game result text printing
    victory_font = pygame.font.Font('D:/Meus Documentos/Documentos/GitHub/stem-games/mypong2/assets/PressStart2P.ttf',
                                    100)
    victory_text = victory_font.render(text, True, COLOR_WHITE, COLOR_BLACK)
    victory_text_rect = score_text.get_rect()
    victory_text_rect.center = (450, 350)
    screen.fill(COLOR_BLACK)
    screen.blit(score_text, score_text_rect)
    screen.blit(victory_text, victory_text_rect)


while game_loop:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop = False

        #  keystroke events não mexa!!!!
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
        if ball_y > 700 or ball_y <= 0:
            ball_dy *= -1
            bounce_sound_effect.play()

        # ball collision with the player 1's paddle
        if ball_x < 100:
            if player_1_y < ball_y + 25:
                if player_1_y + 150 > ball_y:
                    ball = pygame.image.load(ball_player)
                    ball_dx *= -1
                    bounce_sound_effect.play()

        # ball collision with the player 2 's paddle
        if ball_x > 1160:
            if player_2_y < ball_y + 25:
                if player_2_y + 150 > ball_y:
                    ball = pygame.image.load(ball_ai)
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

        # player 2's "Artificial Intelligence"

        # player 1 up movement
        if player_1_move_up:
            player_1_y -= 5

        # player 1 down movement
        if player_1_move_down:
            player_1_y += 5

        # player 1 collides with upper wall
        if player_1_y <= 0:
            player_1_y = 0

        # player 1 collides with lower wall
        elif player_1_y >= 570:
            player_1_y = 570

        # update score hud
        score_text = score_font.render(str(score_1) + ' x ' + str(score_2), True, COLOR_WHITE, COLOR_BLACK)

        # drawing objects
        screen.blit(ball, (ball_x, ball_y))
        screen.blit(player_1, (50, player_1_y))
        screen.blit(player_2, (1180, player_2_y))
        screen.blit(score_text, score_text_rect)
    else:

        # drawing victory
        if score_1 == SCORE_MAX:
            endgame("VICTORY")

        if score_2 == SCORE_MAX:
            endgame("DEFEAT")

    # update screen
    pygame.display.flip()
    game_clock.tick(60)

    # Debugging
    print("Ball position = {0} and {1}".format(ball_x, ball_y))
    # print(pygame.time.get_ticks())
    print(player_2_y)
pygame.quit()
