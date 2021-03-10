from config import img, window, screen, set_obj_coordinates
from random import randrange
from fruit import general_fruit
from snake import x_move, y_move

wall_imgs = []
stone_block_img = img("stone-block")
blocks = [stone_block_img.get_rect()]


def create_wall_img():
    for i in range(3):
        wall_imgs.insert(i, img("stone-wall" + str(i+1)))


def draw_wall():
    general_wall = wall_imgs[0].get_rect()
    aux = 0
    general_wall.x = general_wall.w
    while general_wall.x < window[0] - general_wall.w:
        general_wall.y = 104
        screen.blit(wall_imgs[aux], general_wall)
        general_wall.y = window[1] - general_wall.h
        screen.blit(wall_imgs[aux], general_wall)
        general_wall.x += general_wall.w
        aux += 1
        if aux > 2:
            aux = 0
    general_wall.y = general_wall.h*5
    while general_wall.y < window[1] - general_wall.h:
        general_wall.x = general_wall.w
        screen.blit(wall_imgs[aux], general_wall)
        general_wall.x = window[0] - general_wall.w - general_wall.w
        screen.blit(wall_imgs[aux], general_wall)
        general_wall.y += general_wall.h
        aux += 1
        if aux > 2:
            aux = 0


def random_block(body_pos, player_score):
    if player_score % 10 == 0 and player_score != 0:
        blocks.append(stone_block_img.get_rect())
    for block in blocks:
        while True:
            block.x = randrange(1, (window[0] // block.w) - 1) * block.w
            block.y = randrange(3, (window[1] // block.h) - 1) * block.h
            if not any(pos == (block.x, block.y) for pos in
                       body_pos):  # Checks if
                if not (block.x == general_fruit.x and block.y == general_fruit.y):
                    if block.y == body_pos[0][1]:
                        if x_move > 0:
                            if not (block.x - body_pos[0][0] < 5 * 32):
                                break
                        else:
                            if not (body_pos[0][0] - block.x < 5 * 32):
                                break
                    elif block.x == body_pos[0][0]:
                        if y_move > 0:
                            if not (block.y - body_pos[0][0] < 5 * 32):
                                break
                        else:
                            if not (body_pos[0][0] - block.y < 5 * 32):
                                break
                    else:
                        break
        set_obj_coordinates(block, block.x, block.y)  # set fruit random position
