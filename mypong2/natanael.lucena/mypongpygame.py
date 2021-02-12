import pygame
from random import uniform

pygame.init()

COLOR_LIGHT_GREY = (200, 200, 200)
COLOR_DARK_GREY = pygame.Color('gray12')


def font(fontsize):
    font_path = '../assets/PressStart2P.ttf'
    return pygame.font.Font(font_path, fontsize)


SCORE_MAX = 2

size = (1280, 720)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Pong")

score_font = font(42)
result_font = font(100)


# sound effects
def sound(name):
    sound_path = "../assets/258020__kodack__arcade-bleep-sound.wav"
    if name == "bounce":
        sound_path = "../assets/bounce.wav"
    return pygame.mixer.Sound(sound_path)


bounce_sound_effect = sound("bounce")
scoring_sound_effect = sound("score")


def image(name):
    image_path = "../assets/natanael.lucena/natanael.lucena_paddle.png"
    if name == "ball":
        image_path = "../assets/natanael.lucena/natanael.lucena_ball.png"
    return pygame.image.load(image_path)


def set_obj_coordinates(obj, x, y):
    obj.x = x
    obj.y = y


# player 1
player_1_img = image("paddle")
player_1 = player_1_img.get_rect()
set_obj_coordinates(player_1, 60, (size[1] - player_1.height) / 2)
player_1_move_up = False
player_1_move_down = False
player_score = 0

# player 2 - robot
ai_img = image("paddle")
ai = ai_img.get_rect()
set_obj_coordinates(ai, size[0] - ai.width - player_1.x, (size[1] - ai.height) / 2)
ai_score = 0
ai_move_up = False
ai_move_down = False
ai_difficult = {"easy": False, "normal": False, "hard": False, "impossible": True}
# ia_dy = 5

# ball
ball_img = image("ball")
ball = ball_img.get_rect()
set_obj_coordinates(ball, size[0] / 2, size[1] / 2)
ball_dx = 5
ball_dy = uniform(-2.14, 2.14) * 5

# game loop
game_loop = True
game_clock = pygame.time.Clock()


def check_key(b):
    global player_1_move_up, player_1_move_down, event
    if event.key == pygame.K_w:
        player_1_move_up = b
    if event.key == pygame.K_s:
        player_1_move_down = b


def event_conditional():
    global game_loop, event
    if event.type == pygame.QUIT:
        game_loop = False
    elif event.type == pygame.KEYDOWN:
        check_key(True)
    elif event.type == pygame.KEYUP:
        check_key(False)


def text_render(score_text):
    return score_font.render(f"{score_text}", True, COLOR_LIGHT_GREY)


def random_angle(b1, b2):
    if b1:
        num = uniform(1, 2.14) * 5
    elif b2:
        num = uniform(-2.14, -1) * 5
    else:
        num = 5
    return num


def random_speed(paddle):
    aux = 1
    if paddle == ai:
        aux *= -1
    if paddle.bottomright[1] / 3 <= ball.y <= paddle.bottomright[1] / 1.5:
        num = uniform(5 * aux, 6 * aux)
    else:
        num = uniform(5 * aux, 10 * aux)
    return num


def paddle_collision(paddle):
    global ball_dy, ball_dx, ai_move_up, ai_move_down
    expression = "< 0"
    b1, b2 = player_1_move_down, player_1_move_up
    if paddle == ai:
        expression = "> 0"
        if ai_difficult["impossible"]:
            if ball_dy < 0:
                ai_move_up = True
            else:
                ai_move_down = True
        b1, b2 = ai_move_down, ai_move_up
    if ball.colliderect(paddle) and eval("ball_dx " + expression):
        if (abs(paddle.top - ball.bottom) < collision_tolerance and ball_dy > 0) or (
                abs(paddle.bottom - ball.top) < collision_tolerance and ball_dy < 0):
            ball_dy *= -1
        if abs(paddle.right - ball.left) < collision_tolerance:
            ball_dy = random_angle(b1, b2)
        ball_dx = random_speed(paddle)
        bounce_sound_effect.play()


def score_point_treatment():
    global ball_dy, ball_dx
    ball.x = size[0] / 2
    ball.y = size[1] / 2
    ball_dy *= -1
    ball_dx *= -1
    scoring_sound_effect.play()


def paddle_wall_collision(paddle):
    if paddle.y <= 0:
        paddle.y = 0
    elif paddle.y >= size[1] - player_1.height:
        paddle.y = size[1] - player_1.height


def draw_scenario():
    screen.fill(COLOR_DARK_GREY)
    screen.blit(player_text, (size[0] / 2 - 110, 50))
    screen.blit(ia_text, (size[0] * 9 / 16, 50))


while game_loop:
    for event in pygame.event.get():
        event_conditional()
    player_text = text_render(player_score)
    ia_text = text_render(ai_score)
    # checking the victory condition
    if player_score < SCORE_MAX and ai_score < SCORE_MAX:

        # clear screen
        screen.fill(COLOR_DARK_GREY)

        # ball collision with the wall
        if ball.y >= size[1] - ball.height or ball.y <= 0:
            ball_dy *= -1
            bounce_sound_effect.play()

        collision_tolerance = 10
        paddle_collision(player_1)
        paddle_collision(ai)

        # scoring points
        if ball.x < -50:
            score_point_treatment()
            ai_score += 1
        elif ball.x > size[0] + 50:
            score_point_treatment()
            player_score += 1

        # ball movement
        ball.x += ball_dx
        ball.y += ball_dy

        # player 1 up movement
        if player_1_move_up:
            player_1.y -= 5

        # player 1 down movement
        if player_1_move_down:
            player_1.y += 5
        paddle_wall_collision(player_1)

        # player 2 "Artificial Intelligence"
        ai.y = ball.y
        paddle_wall_collision(ai)

        # drawing objects
        draw_scenario()
        pygame.draw.aaline(screen, COLOR_LIGHT_GREY, (size[0] / 2, 0), (size[0] / 2, size[1]))
        screen.blit(ball_img, ball)
        screen.blit(player_1_img, player_1)
        screen.blit(ai_img, ai)

    else:
        # drawing victory
        result = "VICTORY!"
        text_position = (size[1] / 2 - 70, size[1] / 2 - 70)
        if player_score < ai_score:
            text_position = (size[1] / 2, text_position[1])
            result = "DEFEAT"
        result_text = result_font.render(result, True, COLOR_LIGHT_GREY)
        draw_scenario()
        screen.blit(result_text, text_position)

    # update screen
    pygame.display.flip()
    game_clock.tick(60)

pygame.quit()
