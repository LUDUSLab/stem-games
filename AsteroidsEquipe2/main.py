import menu
import config
import pygame
import game
import score_menu

pygame.init()
menu = menu.Menu()
game = game.Game()
score_menu = score_menu.ScoreMenu()

while True:
    config.window.screen.fill(config.COLOR_BLACK)
    for event in pygame.event.get():
        config.check_quit_event(event)
        if not menu.start_game:
            menu.start_txt.blinker.check_blink_event(event)
            menu.check_game_enter(event)
        if not game.game_over:
            if game.players[game.turns_aux % 2].scenario.ship is not None:
                if not game.players[game.turns_aux % 2].scenario.ship.running_death_animation:
                    game.players[game.turns_aux % 2].scenario.ship.check_ship_shoot(event)
    if not menu.start_game:
        menu.display()
    elif not game.game_over:
        game.pvp_mode = menu.pvp_mode
        game.display()
        is_key_pressed = pygame.key.get_pressed()
        if game.players[game.turns_aux % 2].scenario.ship is not None:
            if not game.players[game.turns_aux % 2].scenario.ship.running_death_animation:
                game.players[game.turns_aux % 2].scenario.ship.check_ship_keys(is_key_pressed)
    else:
        score_menu.display()

    pygame.display.flip()
    config.clock.tick(config.framerate)
