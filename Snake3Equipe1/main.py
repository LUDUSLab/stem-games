import pygame
from menu import MainMenu
import config

if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption('SnakeAI')
    MainMenu(config.screen_dimensions, 'Snake 3')
    pygame.quit()
    quit()
