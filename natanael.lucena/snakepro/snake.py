from config import img, BLOCK_SIZE, window, game_over_treatment, set_obj_coordinates, screen
import pygame

# Snake properties
snake_colors = ["red", "yellow", "purple", "green"]
snake_imgs = []


def reset_snake_images():
    global snake_imgs
    snake_imgs = []
    for i in range(4):
        aux = []
        for j in range(3):
            aux.append(img("snake_" + snake_colors[i] + str(j + 1)))
        snake_imgs.append(aux)

reset_snake_images()
snake = snake_imgs[0][0].get_rect()
snake_pos = [(window[0] // 2, window[1] // 2)]
snake_len = 1
x_move = 0
y_move = 0
snake_head = (snake.x, snake.y)

def reset_snake():
    global snake, snake_pos, snake_len, x_move, y_move
    reset_snake_images()
    snake = snake_imgs[0][0].get_rect()
    snake_pos = [(window[0] // 2, window[1] // 2)]
    snake_len = 1
    x_move = 0
    y_move = 0
    set_obj_coordinates(snake, (window[0] - BLOCK_SIZE) // 2, (window[1] - BLOCK_SIZE) // 2 - 28)


# Rotates the snake image by the given angle
def rotate_imgs(angle, current_snake):
    for k in range(3):
        snake_imgs[current_snake][k] = pygame.transform.rotate(snake_imgs[current_snake][k], angle)

def check_snake_moves(event, random_ind1):
    global x_move, y_move
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_a and x_move <= 0:
            if y_move <= 0 and x_move == 0:
                rotate_imgs(90, random_ind1)
            elif y_move > 0:
                rotate_imgs(-90, random_ind1)
            x_move = -BLOCK_SIZE
            y_move = 0
        elif event.key == pygame.K_d and x_move >= 0:
            if y_move <= 0 and x_move == 0:
                rotate_imgs(-90, random_ind1)
            elif y_move > 0:
                rotate_imgs(90, random_ind1)
            x_move = BLOCK_SIZE
            y_move = 0
        elif event.key == pygame.K_w and y_move <= 0:
            if x_move > 0 and y_move == 0:
                rotate_imgs(90, random_ind1)
            elif x_move < 0:
                rotate_imgs(-90, random_ind1)
            y_move = -BLOCK_SIZE
            x_move = 0
        elif event.key == pygame.K_s and y_move >= 0:
            if x_move > 0 and y_move == 0:
                rotate_imgs(-90, random_ind1)
            elif x_move < 0:
                rotate_imgs(90, random_ind1)
            elif x_move == 0 and y_move == 0:
                rotate_imgs(180, random_ind1)
            y_move = BLOCK_SIZE
            x_move = 0

def snake_moves():
    global snake_head
    snake.x += x_move
    snake.y += y_move
    snake_head = (snake.x, snake.y)
    snake_pos.insert(0, snake_head)
    # Snake body "moves"
    if len(snake_pos) > snake_len:
        del snake_pos[len(snake_pos) - 1]

# The snake collides with herself
def check_snake_collide_herself():
    for x in snake_pos[1:]:
        if x == snake_head:
            game_over_treatment()


def draw_snake(random_ind1):
    for pos in snake_pos:
        if pos == snake_pos[0]:
            screen.blit(snake_imgs[random_ind1][0], (pos[0], pos[1]))
        elif pos == snake_pos[len(snake_pos) - 1]:
            screen.blit(snake_imgs[random_ind1][2], (pos[0], pos[1]))
        else:
            screen.blit(snake_imgs[random_ind1][1], (pos[0], pos[1]))

def snake_wall_collide():
    if snake.y < 116 or snake.y > window[1] - 25 or snake.x < 4 * BLOCK_SIZE or \
            snake.x > window[0] - 5 * BLOCK_SIZE:
        game_over_treatment()

def snake_colors_reset(random_ind1):
    if x_move < 0:
        rotate_imgs(90, random_ind1)
    if x_move > 0:
        rotate_imgs(-90, random_ind1)
    if y_move > 0:
        rotate_imgs(180, random_ind1)
    if y_move < 0:
        pass