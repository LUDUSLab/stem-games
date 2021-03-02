import pygame
from random import randrange, randint
from itertools import cycle

pygame.init()

# Colors
COLOR_LIGHT_GREY = (230, 230, 230)
COLOR_LIGHT_BLUE = (51, 153, 255)

# Window
window = (960, 720)
center = (window[0] // 2, window[1] // 2)
screen = pygame.display.set_mode(window)
pygame.display.set_caption("PySnake")

# Loop variables
game_clock = pygame.time.Clock()
player_record = 0


# Fonts
def font(fontsize):
    font_path = "./assets/PressStart2P.ttf"
    return pygame.font.Font(font_path, fontsize)


game_over_font = font(64)
continue_msg = font(25)


# Create image
def img(name):
    img_path = "./assets/natanael.lucena_" + name + ".png"
    return pygame.image.load(img_path).convert_alpha()


# Set object coordinates
def set_obj_coordinates(obj, x, y):
    obj.x = x
    obj.y = y


# Display message on screen
def msg(fnt, message, pos):
    txt = fnt.render(message, True, COLOR_LIGHT_GREY)
    screen.blit(txt, pos)


# Snake properties
snake_colors = ["red", "yellow", "purple", "green"]
snake_imgs = []
for i in range(4):
    aux = []
    for j in range(3):
        aux.append(img("snake_" + snake_colors[i] + str(j + 1)))
    snake_imgs.append(aux)
snake = snake_imgs[0][0].get_rect()

# Fruits properties
fruits_imgs = [[] for x in range(4)]
general_fruit = img("apple1").get_rect()
general_fruit_x, general_fruit_y = 0, 0
img_names = ["apple", "banana", "grape", "avocado"]
for i in range(len(fruits_imgs)):
    for j in range(3):
        fruits_imgs[i].insert(j, img(img_names[i] + str(j + 1)))


# Rotates the snake image by the given angle
def rotate_imgs(angle, current_snake):
    global snake_imgs
    for k in range(3):
        snake_imgs[current_snake][k] = pygame.transform.rotate(snake_imgs[current_snake][k], angle)


# Does what needs to be done when game is over
def game_over_treatment():
    game_over_sound.play()
    pygame.mixer.music.stop()
    return True


# Sounds
apple_sound = pygame.mixer.Sound('./assets/natanael.lucena.apple_crunch.wav')
game_over_sound = pygame.mixer.Sound('./assets/natanael.lucena.game_over.wav')
pygame.mixer.music.load('./assets/natanael.lucena.background_music.mp3')


# Function to randomly spawn a fruit so that it will not be in the same position as the snake
def random_fruit(body_pos):
    global general_fruit_x, general_fruit_y  # Fruit rectangle coordinates
    while True:
        general_fruit_x = randrange(window[0] // snake.w) * snake.w
        general_fruit_y = randrange(window[1] // snake.h) * snake.h
        if not any(pos == (general_fruit_x, general_fruit_y) for pos in
                   body_pos):  # Checks if the fruit spawn position is not the same as the snake's body
            break
    set_obj_coordinates(general_fruit, general_fruit_x, general_fruit_y)  # set fruit random position


# Blink text effect variables
BLINK_EVENT = pygame.USEREVENT + 0
on_text_surface = continue_msg.render("Q-Quit/E-Play again", True, COLOR_LIGHT_GREY)
blink_rect = on_text_surface.get_rect()
blink_rect.center = screen.get_rect().center
off_text_surface = pygame.Surface(blink_rect.size)
off_text_surface.fill(COLOR_LIGHT_BLUE)
blink_surfaces = cycle([on_text_surface, off_text_surface])
pygame.time.set_timer(BLINK_EVENT, 580)


# Main game loop
def game_loop():
    global general_fruit_x, general_fruit_y, player_record, snake_imgs
    set_obj_coordinates(snake, center[0] - snake.w, center[1] - snake.h)
    game_close, game_over = False, False
    pygame.mixer.music.play(-1)
    x_move, y_move = 0, 0
    snake_pos = [(window[0] // 2, window[1] // 2)]
    snake_len = 1
    random_ind1 = randint(0, 3)
    random_ind2 = randint(0, 3)
    frame_aux = 0
    for n in range(4):
        aux1 = []
        for m in range(3):
            aux1.append(img("snake_" + snake_colors[n] + str(m + 1)))
        snake_imgs[n] = aux1
    random_fruit(snake_pos)
    blink_surface = next(blink_surfaces)
    # The game is not closed, so we either play again or leave the game
    while not game_close:
        while game_over:  # When the snake collides with herself or with the wall, the game is over
            screen.fill(COLOR_LIGHT_BLUE)
            if snake_len - 1 > player_record:
                player_record = snake_len - 1
            msg(continue_msg, "Your record: {}".format(player_record),
                (center[0] - continue_msg.size("Your record: *")[0] / 2, snake.w))
            msg(game_over_font, "Game Over",
                (center[0] - game_over_font.size("Game Over")[0] / 2, center[1] - window[1] // 4))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        quit()
                    if event.key == pygame.K_e:
                        game_loop()
                if event.type == BLINK_EVENT:
                    blink_surface = next(blink_surfaces)

            # Displays blink message on the screen
            screen.blit(blink_surface, blink_rect)
            pygame.display.flip()
            if blink_surface == on_text_surface:
                pygame.time.wait(300)
            game_clock.tick(60)
        game_clock.tick(10)
        screen.fill(COLOR_LIGHT_BLUE)
        screen.blit(fruits_imgs[random_ind2][frame_aux], general_fruit)
        # Displays score on the game screen
        msg(continue_msg, "Score: {}".format(snake_len - 1),
            (center[0] - continue_msg.size("Score: *")[0] / 2, snake.w))
        # Auxiliary variables
        frame_aux += 1
        if frame_aux > 2:
            frame_aux = 0
        fruit_eated = (snake.x == general_fruit_x and snake.y == general_fruit_y)
        # Listen to players key and rotate the snake image to the respective direction
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_close = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a and x_move <= 0:
                    if y_move <= 0 and x_move == 0:
                        rotate_imgs(90, random_ind1)
                    elif y_move > 0:
                        rotate_imgs(-90, random_ind1)
                    x_move = -snake.w
                    y_move = 0
                elif event.key == pygame.K_d and x_move >= 0:
                    if y_move <= 0 and x_move == 0:
                        rotate_imgs(-90, random_ind1)
                    elif y_move > 0:
                        rotate_imgs(90, random_ind1)
                    x_move = snake.w
                    y_move = 0
                elif event.key == pygame.K_w and y_move <= 0:
                    if x_move > 0 and y_move == 0:
                        rotate_imgs(90, random_ind1)
                    elif x_move < 0:
                        rotate_imgs(-90, random_ind1)
                    y_move = -snake.w
                    x_move = 0
                elif event.key == pygame.K_s and y_move >= 0:
                    if x_move > 0 and y_move == 0:
                        rotate_imgs(-90, random_ind1)
                    elif x_move < 0:
                        rotate_imgs(90, random_ind1)
                    elif x_move == 0 and y_move == 0:
                        rotate_imgs(180, random_ind1)
                    y_move = snake.w
                    x_move = 0
        # Snake moves
        snake.x += x_move
        snake.y += y_move
        snake_head = (snake.x, snake.y)
        snake_pos.insert(0, snake_head)
        # Snake body "moves"
        if len(snake_pos) > snake_len:
            del snake_pos[len(snake_pos) - 1]

        # The snake collides with the wall
        if snake.y < 0 or snake.y > window[1] - snake.height or snake.x < 0 or \
                snake.x > window[0] - snake.width:
            game_over = game_over_treatment()
        # The snake collides with herself
        for x in snake_pos[1:]:
            if x == snake_head:
                game_over = game_over_treatment()

        # Draw snake
        for x in snake_pos:
            if x == snake_pos[0]:
                screen.blit(snake_imgs[random_ind1][0], (x[0], x[1]))
            elif x == snake_pos[len(snake_pos) - 1]:
                screen.blit(snake_imgs[random_ind1][2], (x[0], x[1]))
            else:
                screen.blit(snake_imgs[random_ind1][1], (x[0], x[1]))

        # Fruit eated
        if fruit_eated:
            random_ind1 = random_ind2
            snake_len += 1
            apple_sound.play()
            random_fruit(snake_pos)
            for m in range(3):
                snake_imgs[random_ind1][m] = img("snake_" + snake_colors[random_ind1] + str(m + 1))  # Reset snake image
            random_ind2 = randint(0, 3)
            if x_move < 0:
                rotate_imgs(90, random_ind1)
            if x_move > 0:
                rotate_imgs(-90, random_ind1)
            if y_move > 0:
                rotate_imgs(180, random_ind1)
            if y_move < 0:
                pass
        pygame.display.flip()
    pygame.quit()
    quit()


game_loop()  # Main function called
