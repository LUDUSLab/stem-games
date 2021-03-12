import pygame
import random
import config


def random_head_pos():
    pos_x = random.randint(0, 24) * config.block_size + 16
    pos_y = random.randint(0, 15) * config.block_size + 136
    return [pos_x, pos_y]
    #gerar posição diferente dos obstaculos


def turn_img(image, angle):
    aux = pygame.transform.rotate(image, angle)
    return aux


#Initial movement
direction_x = 0
direction_y = -1

head_pos = random_head_pos()

snake_pos = list()
snake_pos.append(head_pos)

head = pygame.image.load('assets/allef.ramos_snake.head.png')

snake_img = list()
snake_img.append(head)

