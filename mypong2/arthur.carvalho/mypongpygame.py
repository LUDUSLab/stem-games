import pygame


def score_points():
    global ball_x, ball_y, ball_dx, ball_dy, score_1, score_2, score_text
    score_text = score_font.render(str(score_1) + ' x ' + str(score_2), True, white, black)

    if ball_x == 0:
        score_2 += 1
        ball_dy *= -1
        ball_dx *= -1
        ball_x, ball_y = 510, 320

    elif ball_x == 1020:
        score_1 += 1
        ball_dy *= -1
        ball_dx *= -1
        ball_x, ball_y = 510, 320


def draw_objects():
    screen.blit(ball, (ball_x, ball_y))
    screen.blit(player_1, (20, player_1_y))
    screen.blit(player_2, (980, player_2_y))
    screen.blit(score_text, score_text_rect)

    pygame.display.update()


def move_n_collision_ball():
    global ball_x, ball_y, ball_dx, ball_dy
    ball_x += ball_dx
    ball_y += ball_dy

    if (ball_y < 0) or (ball_y > 640):
        ball_dy *= -1

    else:
        if (ball_x == 30 and player_1_y + 150 > ball_y > player_1_y) or (ball_x == 970 and player_2_y + 150 > ball_y > player_2_y):
            ball_dx *= -1

    draw_objects()


def artificial_intelligence():
    global player_2_y
    if ball_dx > 0:
        if (ball_dy < 0 and ball_y > player_2_y + 75) or (ball_dy > 0 and ball_y > player_2_y + 75):
            player_2_y += 1

        elif (ball_dy < 0 and ball_y < player_2_y + 75) or (ball_dy > 0 and ball_y < player_2_y + 75):
            player_2_y -= 1

        if player_2_y <= 0:
            player_2_y = 0

        if player_2_y >= 490:
            player_2_y = 490


pygame.init()

black, white = (0, 0, 0), (255, 255, 255)
score_max = 10
score_1 = score_2 = 0

# Creation screen
size = (1020, 640)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('MyPong - Pygame Edition')

# players configuration
player_1 = pygame.image.load("C:/Users/arthu/Documents/STEM/stem-games/mypong2/assets/arthur.carvalho_paddle.png")
player_2 = pygame.image.load("C:/Users/arthu/Documents/STEM/stem-games/mypong2/assets/arthur.carvalho_paddle.png")
player_1_y = player_2_y = 270
player_1_move_up = player_1_move_down = False

# ball configuration
ball = pygame.image.load("C:/Users/arthu/Documents/STEM/stem-games/mypong2/assets/arthur.carvalho_ball.png")
ball_x, ball_y = 510, 320
ball_dx = ball_dy = 2

# score text
score_font = pygame.font.Font('C:/Users/arthu/Documents/STEM/stem-games/mypong2/assets/PressStart2P.ttf', 44)
score_text = score_font.render('00 x 00', True, white, black)
score_text_rect = score_text.get_rect()
score_text_rect.center = (550, 30)

# victory text
victory_font = pygame.font.Font('C:/Users/arthu/Documents/STEM/stem-games/mypong2/assets/PressStart2P.ttf', 70)
victory_text = victory_font .render('VICTORY', True, white, black)
victory_text_rect = score_text.get_rect()
victory_text_rect.center = (430, 300)


game_loop = True

while game_loop:
    screen.fill(black)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop = False

        # map keys
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_1_move_up = True

            elif event.key == pygame.K_DOWN:
                player_1_move_down = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player_1_move_up = False

            elif event.key == pygame.K_DOWN:
                player_1_move_down = False

    if score_1 < score_max and score_2 < score_max:
        artificial_intelligence()
        move_n_collision_ball()
        score_points()

        # player 1 up and down movement
        if player_1_move_up:
            player_1_y -= 1

            # player 1 collides with upper wall
            if player_1_y <= 0:
                player_1_y = 0

        elif player_1_move_down:
            player_1_y += 1

            # player 1 collides with lower wall
            if player_1_y >= 490:
                player_1_y = 490

    else:
        screen.blit(victory_text, victory_text_rect)
        pygame.display.update()

pygame.quit()
