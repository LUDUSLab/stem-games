import menu
import config
import pygame

pygame.init()

while not menu.menu_obj.start_game:
    config.check_quit_event()
    # menu.menu_obj.check_game_enter()
    config.window.display_surface(menu.menu_obj.get_surface())
