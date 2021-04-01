import menu
import credits
import game
import config
import pygame

pygame.init()

while not menu.menu_options["in_game"] and not menu.menu_options["exit"]:
    config.menu_sound.play()
    if menu.menu_options["in_credits"]:
        credits.credits_obj.display_all()
    else:
        menu.menu_obj.display_all()

if menu.menu_options["in_game"]:
    pygame.mixer.music.play(-1)

while menu.menu_options["in_game"]:
    config.menu_sound.stop()
    game.game_obj.display_all()
