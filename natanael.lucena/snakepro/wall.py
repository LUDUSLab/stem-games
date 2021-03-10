from config import img, window, screen, set_obj_coordinates, BLOCK_SIZE
from random import randrange
from fruit import general_fruit
from snake import x_move, y_move

# Wall variables
wall_imgs = []
stone_block_img = img("stone-block")
blocks = [stone_block_img.get_rect()]


# Create wall image
def create_wall_img():
    for i in range(3):
        wall_imgs.insert(i, img("stone-wall" + str(i+1)))


# Draw the wall on screen
def draw_wall():
    general_wall = wall_imgs[0].get_rect()
    aux = 0
    general_wall.x = 3*BLOCK_SIZE
    while general_wall.x < window[0] - 3*BLOCK_SIZE:
        general_wall.y = BLOCK_SIZE * 3 + 8
        screen.blit(wall_imgs[aux], general_wall)
        general_wall.y = window[1] - general_wall.h
        screen.blit(wall_imgs[aux], general_wall)
        general_wall.x += BLOCK_SIZE
        aux += 1
        if aux > 2:
            aux = 0
    general_wall.y = general_wall.h*5
    while general_wall.y < window[1] - general_wall.h:
        general_wall.x = 3*BLOCK_SIZE
        screen.blit(wall_imgs[aux], general_wall)
        general_wall.x = window[0] - 4*BLOCK_SIZE
        screen.blit(wall_imgs[aux], general_wall)
        general_wall.y += general_wall.h
        aux += 1
        if aux > 2:
            aux = 0


# Define the right location for obstacle's spawn
def random_block(body_pos, player_score):
    if player_score % 10 == 0 and player_score != 0:
        blocks.append(stone_block_img.get_rect())
    for block in blocks:
        while True:
            block.x = randrange(4, (window[0] // BLOCK_SIZE) - 4) * BLOCK_SIZE
            block.y = randrange(4, (window[1] // BLOCK_SIZE)) * BLOCK_SIZE
            # Check if the obstacle spawn position is not the same as the snake's body
            if not any(pos == (block.x, block.y) for pos in body_pos):
                # Check if the obstacle spawn position is not the same as the snake's body
                if not (block.x == general_fruit.x and block.y == general_fruit.y):
                    # Check if the obstacle spawn position is not too close of snakes head if it is moving horizontally
                    if block.y == body_pos[0][1]:
                        if x_move > 0 and not (block.x - body_pos[0][0] < 5 * BLOCK_SIZE):
                            break
                        elif x_move < 0 and not (body_pos[0][0] - block.x < 5 * BLOCK_SIZE):
                            break
                    # Check if the obstacle spawn position is not too close of snakes head if it is moving vertically
                    elif block.x == body_pos[0][0]:
                        if y_move > 0 and not (block.y - body_pos[0][0] < 5 * BLOCK_SIZE):
                            break
                        elif y_move < 0 and not (body_pos[0][0] - block.y < 5 * BLOCK_SIZE):
                            break
                    else:
                        break
        set_obj_coordinates(block, block.x, block.y)  # set fruit random position
