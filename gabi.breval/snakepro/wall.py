import pygame
import random
import config
import game
from pygame.locals import *
from tkinter.messagebox import showinfo

# Lines ---------------------------------------------------------------------------------------------- #
pygame.draw.line(config.screen, game.COLOR_WHITE, [5, 50], [595, 50], 1)
pygame.draw.line(config.screen, game.COLOR_WHITE, [5, 50], [5, 550], 1)
pygame.draw.line(config.screen, game.COLOR_WHITE, [595, 50], [595, 550], 1)
pygame.draw.line(config.screen, game.COLOR_WHITE, [5, 550], [595, 550], 1)