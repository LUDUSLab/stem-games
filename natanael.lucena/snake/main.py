import pygame
from random import randrange

pygame.init()

# Colors
COLOR_LIGHT_GREY = (200, 200, 200)
COLOR_DARK_GREY = pygame.Color('gray12')

# Window
window = (960, 720)
center = (window[0] // 2, window[1] // 2)
screen = pygame.display.set_mode(window)
pygame.display.set_caption("Snake")

game_clock = pygame.time.Clock()
game_close = False


# Create font
def font(fontsize):
    font_path = "./assets/PressStart2P.ttf"
    return pygame.font.Font(font_path, fontsize)


# Create image
def img(name):
    img_path = "./assets/natanael.lucena_" + name + ".png"
    return pygame.image.load(img_path).convert_alpha()


# Set object coordinates
def set_obj_coordinates(obj, x, y):
    obj.x = x
    obj.y = y


def msg(fnt, message, pos):
    txt = fnt.render(message, True, COLOR_LIGHT_GREY)
    screen.blit(txt, pos)


# Check player key press
x_move = 0
y_move = 0


def check_player_key(ev):
    global x_move, y_move, game_close
    if ev.type == pygame.QUIT:
        game_close = True
    elif ev.type == pygame.KEYDOWN:
        if ev.key == pygame.K_a and x_move <= 0:
            x_move = -snake.w
            y_move = 0
        elif ev.key == pygame.K_d and x_move >= 0:
            x_move = snake.w
            y_move = 0
        elif ev.key == pygame.K_w and y_move <= 0:
            y_move = -snake.w
            x_move = 0
        elif ev.key == pygame.K_s and y_move >= 0:
            y_move = snake.w
            x_move = 0


score_font = font(36)
game_over_font = font(64)
continue_msg = font(25)
# Render score text
# def text_render(a_score_text):
#    return score_font.render(f"{a_score_text}", True, COLOR_LIGHT_GREY)


# Check if the snake collided and the game is over


# Snake
snake_img = img("snake")
snake = snake_img.get_rect()
snake_len = 1
# Apple
apple_img = img("apple")
apple = apple_img.get_rect()
apple_eaten = False

def make_snake(snk_lst):

    for x in snk_lst:
        screen.blit(snake_img, (x[0], x[1]))


def game_loop():
    global x_move, y_move, game_close, snake_len
    set_obj_coordinates(snake, center[0] - snake.w, center[1] - snake.h)
    game_close = False
    game_over = False
    x_move = 0
    y_move = 0
    snake_pos = []
    snake_len = 1
    food_x = round(randrange(0, window[0] - snake.w)/30)*30
    food_y = round(randrange(0, window[1] - snake.h)/30)*30
    set_obj_coordinates(apple, food_x, food_y)
    while not game_close:
        while game_over:
            screen.fill(COLOR_DARK_GREY)
            msg(game_over_font, "Game Over",
                (center[0] - game_over_font.size("Game Over")[0] / 2, center[1] - window[1] // 4))
            msg(continue_msg, "Q-Quit/E-Play again",
                (center[0] - continue_msg.size("Q-Quit/E-Play Again")[0] / 2, center[1]))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        quit()
                    if event.key == pygame.K_e:
                        game_loop()
                if event.type == pygame.QUIT:
                    quit()
        # Main game loop
        # score_text = text_render(snake_score)
        screen.fill(COLOR_DARK_GREY)
        screen.blit(apple_img, apple)
        for event in pygame.event.get():
            check_player_key(event)
        if snake.y < 0 or snake.y > window[1] - snake.height or snake.x < 0 or \
                snake.x > window[0] - snake.width:
            game_over = True
        snake.x += x_move
        snake.y += y_move
        snake_head = (snake.x, snake.y)
        snake_pos.append(snake_head)

        if len(snake_pos) > snake_len:
            del snake_pos[0]

        for x in snake_pos[:-1]:
            if x == snake_head:
                game_over = True

        make_snake(snake_pos)

        pygame.display.update()
        if snake.x == food_x and snake.y == food_y:
            food_x = round(randrange(0, window[0] - snake.w) / snake.w) * snake.w
            food_y = round(randrange(0, window[1] - snake.h) / snake.w) * snake.w
            snake_len += 1
            set_obj_coordinates(apple, food_x, food_y)
        # Update screen

        game_clock.tick(15)

    pygame.quit()
    quit()


game_loop()
