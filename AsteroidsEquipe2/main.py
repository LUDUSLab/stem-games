import menu
import config
import pygame

pygame.init()
menu = menu.Menu()

while True:
    for event in pygame.event.get():
        config.check_quit_event(event)
        menu.start_txt.blinker.check_blink_event(event)
        if not menu.start_game:
            menu.check_game_enter(event)
    config.window.screen.fill(config.COLOR_BLACK)
    if not menu.start_game:
        menu.display_bg_animation()
        # menu.menu_obj.check_enter_game()
    pygame.display.flip()
    config.clock.tick(config.framerate)


