import pygame
from menu import MainMenu
import config

if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption('SnakeAI')
    MainMenu(720, 1280, 'Snake 3')
    pygame.quit()
    quit()
