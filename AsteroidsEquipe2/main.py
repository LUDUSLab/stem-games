import menu
import config
import pygame
import game

pygame.init()
menu = menu.Menu()
game = game.Game()

saving_score = False

while True:
    config.window.screen.fill(config.COLOR_BLACK)
    for event in pygame.event.get():
        config.check_quit_event(event)
        menu.start_txt.blinker.check_blink_event(event)
        if not menu.start_game:
            menu.check_game_enter(event)
    if not menu.start_game:
        menu.display()
    elif not saving_score:
        game.display()
    else:
        pass

    pygame.display.flip()
    config.clock.tick(config.framerate)
