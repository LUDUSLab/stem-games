from config import img, window, screen, set_obj_coordinates
from random import randrange
from fruit import general_fruit
from snake import x_move, y_move

wall_imgs = []
stone_block_img = img("stone-block")
general_block = stone_block_img.get_rect()


def create_wall_img():
    for i in range(3):
        wall_imgs.insert(i, img("stone-wall" + str(i+1)))


def draw_wall():
    general_wall = wall_imgs[0].get_rect()
    aux = 0
    while general_wall.x < window[0]:
        general_wall.y = 72
        screen.blit(wall_imgs[aux], general_wall)
        general_wall.y = window[1] - general_wall.h
        screen.blit(wall_imgs[aux], general_wall)
        general_wall.x += general_wall.w
        aux += 1
        if aux > 2:
            aux = 0
    general_wall.y = general_wall.h*4
    while general_wall.y < window[1] - general_wall.h:
        general_wall.x = 0
        screen.blit(wall_imgs[aux], general_wall)
        general_wall.x = window[0] - general_wall.w
        screen.blit(wall_imgs[aux], general_wall)
        general_wall.y += general_wall.h
        aux += 1
        if aux > 2:
            aux = 0


def random_block(body_pos):
    while True:
        general_block.x = randrange(1, (window[0] // general_block.w) - 1) * general_block.w
        general_block.y = randrange(3, (window[1] // general_block.h) - 1) * general_block.h
        if not any(pos == (general_block.x, general_block.y) for pos in
                   body_pos):  # Checks if
            if not (general_block.x == general_fruit.x and general_block.y == general_block.y):
                if y_move == 0:
                    if not (abs(general_block.x - body_pos[0][0]) < 5 * 32):
                        break
                elif x_move == 0:
                    if not (abs(general_block.x - body_pos[0][0]) < 5*32):
                        break

    set_obj_coordinates(general_block, general_block.x, general_block.y)  # set fruit random position
