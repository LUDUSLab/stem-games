import pygame


def score_points():
    global ball_x, ball_y, ball_dx, ball_dy, score_1, score_2
    if ball_x == 0:
        ball_x, ball_y = 510, 320
        ball_dy *= -1
        ball_dx *= -1
        score_2 += 1
    elif ball_x == 1020:
        ball_x, ball_y = 510, 320
        ball_dy *= -1
        ball_dx *= -1
        score_1 += 1


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

    if (ball_x > 1020) or (ball_x < 0):
        ball_dx *= -1


pygame.init()

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
ball_dx = ball_dy = 1

# score text
score_font = pygame.font.Font('C:/Users/arthu/Documents/STEM/stem-games/mypong2/assets/PressStart2P.ttf', 44)
score_text = score_font.render('00 x 00', True, (255, 255, 255), (0, 0, 0))
score_text_rect = score_text.get_rect()
score_text_rect.center = (550, 30)

# victory text
victory_font = pygame.font.Font('C:/Users/arthu/Documents/STEM/stem-games/mypong2/assets/PressStart2P.ttf', 70)
victory_text = victory_font .render('VICTORY', True, (255, 255, 255), (0, 0, 0))
victory_text_rect = score_text.get_rect()
victory_text_rect.center = (430, 300)


game_loop = True

while game_loop:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop = False

        # map keys
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

    # player 1 up and down movement
    if player_1_move_up:
        player_1_y -= 1

    if player_1_move_down:
        player_1_y += 1

    # player 1 collides with upper wall
    if player_1_y <= 0:
        player_1_y = 0

    # player 1 collides with lower wall
    elif player_1_y >= 490:
        player_1_y = 490

    if score_1 < score_max and score_2 < score_max:
        move_n_collision_ball()
        score_points()
        draw_objects()
        score_text = score_font.render(str(score_1) + ' x ' + str(score_2), True, (255, 255, 255), (0, 0, 0))
    else:
        screen.fill((0, 0, 0))
        screen.blit(score_text, score_text_rect)
        screen.blit(victory_text, victory_text_rect)
        pygame.display.update()

pygame.quit()
