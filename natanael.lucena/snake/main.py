import pygame
from random import randrange, randint

pygame.init()

# Colors
COLOR_LIGHT_GREY = (230, 230, 230)
COLOR_LIGHT_BLUE = (51, 153, 255)
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


game_over_font = font(64)
continue_msg = font(25)

# Snake
snake_img1 = img("snake1")
snake_img2 = img("snake2")
snake_img3 = img("snake3")
snake = snake_img1.get_rect()
snake_len = 1
# Apple
apple_imgs, banana_imgs, grape_imgs, avocado_imgs = [pygame.surface, pygame.surface, pygame.surface], \
    [pygame.surface, pygame.surface, pygame.surface], [pygame.surface, pygame.surface, pygame.surface],\
    [pygame.surface, pygame.surface, pygame.surface]
fruits_imgs = [apple_imgs, banana_imgs, grape_imgs, avocado_imgs]
general_fruit = img("apple1").get_rect()
general_fruit_x = 0
general_fruit_y = 0


def make_snake(snk_lst):
    for x in snk_lst:
        if x == snk_lst[0]:
            screen.blit(snake_img1, (x[0], x[1]))
        elif x == snk_lst[len(snk_lst)-1]:
            screen.blit(snake_img3, (x[0], x[1]))
        else:
            screen.blit(snake_img2, (x[0], x[1]))

def random_fruit(pos):
    global general_fruit_x, general_fruit_y
    while True:
        general_fruit_x = randrange(window[0] // snake.w) * snake.w
        general_fruit_y = randrange(window[1] // snake.h) * snake.h
        if len(list(filter(lambda z: pos == (general_fruit_x, general_fruit_y), pos))) > 0:
            continue
        else:
            break
    set_obj_coordinates(general_fruit, general_fruit_x, general_fruit_y)


img_names = ["apple", "banana", "grape", "avocado"]
for i in range(len(fruits_imgs)):
    for j in range(3):
        fruits_imgs[i][j] = img(img_names[i] + str(j + 1))

def draw_fruits(rand_num, aux):

    screen.blit(fruits_imgs[rand_num][aux], general_fruit)

def game_loop():
    global x_move, y_move, game_close, snake_len, general_fruit_x, general_fruit_y
    set_obj_coordinates(snake, center[0] - snake.w, center[1] - snake.h)
    game_close = False
    game_over = False
    x_move = 0
    y_move = 0
    snake_pos = []
    snake_len = 1
    random_ind = randint(0, 3)
    frame_aux = 0
    random_fruit(snake_pos)

    while not game_close:
        while game_over:
            screen.fill(COLOR_LIGHT_BLUE)
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
        game_clock.tick(10)
        screen.fill(COLOR_LIGHT_BLUE)
        # blit fruit
        draw_fruits(random_ind, frame_aux)
        frame_aux += 1
        if frame_aux > 2:
            frame_aux = 0

        for event in pygame.event.get():
            check_player_key(event)
        if snake.y < 0 or snake.y > window[1] - snake.height or snake.x < 0 or \
                snake.x > window[0] - snake.width:
            game_over = True
        snake.x += x_move
        snake.y += y_move
        snake_head = (snake.x, snake.y)
        snake_pos.insert(0, snake_head)

        if len(snake_pos) > snake_len:
            del snake_pos[len(snake_pos)-1]

        for x in snake_pos[1:]:
            if x == snake_head:
                game_over = True

        make_snake(snake_pos)

        if snake.x == general_fruit_x and snake.y == general_fruit_y:
            random_fruit(snake_pos)
            random_ind = randint(0, 3)
            snake_len += 1
        pygame.display.update()
        # Update screen
        pygame.time.delay(70)

    pygame.quit()
    quit()


game_loop()
