import pygame
#create a config.py file and add constants, functions and globals variables. Ex.: SCREEN_LENGTH, BLOCK_SIZE, etc

#Screen "variables"
dimentions = (800, 600)
block_size = 32

game_clock = pygame.time.Clock()

#colors
black = (0, 0, 0)
royalblue = (65, 105, 225)
white = (255, 255, 255)


def font_(size):
    fnt = 'assets/PressStart2P.ttf'
    font = pygame.font.Font(fnt, size)
    return font
