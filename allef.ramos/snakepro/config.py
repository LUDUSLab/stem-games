import pygame
#create a config.py file and add constants, functions and globals variables. Ex.: SCREEN_LENGTH, BLOCK_SIZE, etc

screen_length, screen_height = 800, 600
block_size = 32

background = pygame.image.load('assets/allef.ramos_grass.png')
walls = pygame.image.load('assets/allef.ramos_brick.walls.png')

bg_x = 16
bg_y = 104

#colors
royalblue = (65, 105, 225)
white = (225, 225, 225)
#g_o_sound = pygame.mixer.Sound('assets/allef.ramos_game.over.wav')
#eat_apple = pygame.mixer.Sound('assets/allef.ramos.apple-crunch.wav')


def font_(size):
    font = pygame.font.Font('assets/PressStart2P.ttf', size)
    return font
