import pygame
from menu import MainMenu
import config

if __name__ == "__main__":
    config.music_menu.play()
    pygame.init()
    pygame.display.set_caption('SnakeAI')
    MainMenu(640, 1280, 'Snake 3')
    pygame.quit()
    quit()
