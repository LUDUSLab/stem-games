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
        if not menu.start_game:
            menu.start_txt.blinker.check_blink_event(event)
            menu.check_game_enter(event)
    if not menu.start_game:
        menu.display()
    elif not saving_score:
        game.display()
        is_key_pressed = pygame.key.get_pressed()
        game.players[game.turns_aux % 2].scenario.ship.check_ship_keys(is_key_pressed)
    else:
        pass

    pygame.display.flip()
    config.clock.tick(config.framerate)
