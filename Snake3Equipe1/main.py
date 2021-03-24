import pygame
from menu import MainMenu

if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption('SnakeAI')
    MainMenu(600, 1200, 'Snake 3')
    pygame.quit()
    quit()
