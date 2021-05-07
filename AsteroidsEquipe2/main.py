import menu
import config
import pygame

pygame.init()
menu = menu.Menu()
while not menu.start_game:
    config.check_quit_event()
    config.clock.tick(config.framerate)
    config.window.screen.fill(config.COLOR_BLACK)
    menu.display_bg_animation()
    pygame.display.flip()
    # menu.menu_obj.check_game_enter()
