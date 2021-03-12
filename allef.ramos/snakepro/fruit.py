from pygame import image
from random import randrange
from config import block_size


def apple_pos(xo, xf, yo, yf):
    pos_x = randrange(xo, xf, block_size)
    pos_y = randrange(yo, yf, block_size)
    return [pos_x, pos_y]


apple = image.load('assets/allef.ramos_apple.png')

apple_cord = apple_pos(48+32, 800-49, 168+32, 600-49)
