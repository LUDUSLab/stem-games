import menu
import config
import pygame
import game
import score_menu

pygame.init()
menu = menu.Menu()
game_obj = game.Game()
score_menu_obj = score_menu.ScoreMenu(game_obj.hud, menu.header, menu.footer, menu.start_txt)
continue_playing = False
aux_flag = False


while True:
    config.window.screen.fill(config.COLOR_BLACK)
    for event in pygame.event.get():
        config.check_quit_event(event)
        if not menu.start_game or (game_obj.game_over and score_menu_obj.has_entered_nick):
            if (game_obj.game_over and score_menu_obj.has_entered_nick) or (not game_obj.game_over):
                menu.start_txt.blinker.check_blink_event(event)
                menu.check_game_enter(event)
            if menu.start_game and score_menu_obj.has_entered_nick:
                if game_obj.game_over:
                    aux_flag = True
                game_obj.game_over = False
                menu.start_game = False
        if not game_obj.game_over:
            if game_obj.players[game_obj.turns_aux % 2].scenario.ship is not None:
                if not game_obj.players[game_obj.turns_aux % 2].scenario.ship.running_death_animation:
                    game_obj.players[game_obj.turns_aux % 2].scenario.ship.check_ship_shoot(event)
        if not score_menu_obj.has_entered_nick and game_obj.game_over:
            if event.type == pygame.KEYDOWN:
                score_menu_obj.write_nick(pygame.key.name(event.key))

    if (not menu.start_game) and (not continue_playing) and (not score_menu_obj.has_entered_nick):
        menu.display()
    elif not game_obj.game_over:
        if continue_playing and aux_flag:
            game_obj = game.Game()
            continue_playing = True
            aux_flag = False
            score_menu_obj = score_menu.ScoreMenu(game_obj.hud, menu.header, menu.footer, menu.start_txt)
        game_obj.pvp_mode = menu.pvp_mode
        game_obj.display()
        is_key_pressed = pygame.key.get_pressed()
        if game_obj.players[game_obj.turns_aux % 2].scenario.ship is not None:
            if not game_obj.players[game_obj.turns_aux % 2].scenario.ship.running_death_animation:
                game_obj.players[game_obj.turns_aux % 2].scenario.ship.check_ship_keys(is_key_pressed)
    else:
        menu.start_game = False
        continue_playing = True
        score_menu_obj.pvp_mode = game_obj.pvp_mode
        score_menu_obj.display()

    pygame.display.flip()
    config.clock.tick(config.framerate)
