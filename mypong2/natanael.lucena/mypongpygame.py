import pygame
from random import uniform

pygame.init()


COLOR_LIGHT_GREY = (200, 200, 200)
COLOR_DARK_GREY = pygame.Color('gray12')

SCORE_MAX = 2

size = (1280, 720)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Pong")

player_score = 0
ia_score = 0

# score text
score_font = pygame.font.Font('../assets/PressStart2P.ttf', 40)

# victory text
victory_font = pygame.font.Font('../assets/PressStart2P.ttf', 100)

# sound effects
bounce_sound_effect = pygame.mixer.Sound('../assets/bounce.wav')
scoring_sound_effect = pygame.mixer.Sound('../assets/258020__kodack__arcade-bleep-sound.wav')

# player 1
player_1_img = pygame.image.load("../assets/natanael.lucena/natanael.lucena_paddle.png")
player_1 = player_1_img.get_rect()
player_1.x = 60
player_1.y = 300
player_1_move_up = False
player_1_move_down = False

# player 2 - robot
player_2_img = pygame.image.load("../assets/natanael.lucena/natanael.lucena_paddle.png")
player_2 = player_2_img.get_rect()
player_2.x = 1190
player_2.y = 300

# ball
ball_img = pygame.image.load("../assets/natanael.lucena/natanael.lucena_ball.png")
ball = ball_img.get_rect()
ball.x = 640
ball.y = 360
ball_dx = 5
ball_dy = uniform(-2.14, 2.14) * 5

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
    player_text = score_font.render(f"{player_score}", True, COLOR_LIGHT_GREY)
    ia_text = score_font.render(f"{ia_score}", True, COLOR_LIGHT_GREY)
    # checking the victory condition
    if player_score < SCORE_MAX and ia_score < SCORE_MAX:

        # clear screen
        screen.fill(COLOR_DARK_GREY)

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
                    ball_dy = uniform(1, 2.14) * 5
                elif player_1_move_up:
                    ball_dy = uniform(-2.14, -1) * 5
            if player_1.bottomright[1] / 3 <= ball.y <= player_1.bottomright[1] / 1.5:
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
                    ball_dy = uniform(1, 2.14) * 5
                elif player_1_move_up:
                    ball_dy = uniform(-2.14, -1) * 5
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
            ia_score += 1
            scoring_sound_effect.play()
        elif ball.x > 1320:
            ball.x = 640
            ball.y = 360
            ball_dy *= -1
            ball_dx *= -1
            player_score += 1
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

        # drawing objects
        screen.fill(COLOR_DARK_GREY)
        screen.blit(ball_img, ball)
        screen.blit(player_1_img, player_1)
        screen.blit(player_2_img, player_2)
        screen.blit(player_text, (530, 50))
        screen.blit(ia_text, (730, 50))
        pygame.draw.aaline(screen, (200, 200, 200), (640, 0), (640, 720))

    else:
        # drawing victory
        result = "VICTORY!"
        screen.fill(COLOR_DARK_GREY)
        if player_score < ia_score:
            result = "DEFEAT"
        victory_text = victory_font.render(result, True, COLOR_LIGHT_GREY)
        screen.blit(player_text, (530, 50))
        screen.blit(ia_text, (730, 50))
        screen.blit(victory_text, (360, 290))

    # update screen
    pygame.display.flip()
    game_clock.tick(60)

pygame.quit()
