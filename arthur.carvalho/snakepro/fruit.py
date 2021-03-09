from config import *
from snakebody import snake_position
from random import choice


def fruit_position():
    global fruit_pos

    if snake_position[0] != fruit_pos:
        return fruit_pos

    else:
        x = []
        y = []

        for c in range(0, 800, 32):
            x.append(c)

        for c in range(0, 640, 32):
            y.append(c)

        snake_position.append((800, 600))

        fruit_pos = (choice(x), choice(y))

        return fruit_pos


def fruit_draw():
    apple_sprite = pygame.image.load('assets/apple_sprite.png')

    screen.blit(apple_sprite, fruit_position())


fruit_pos = (128, 128)
