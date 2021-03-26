import menu
import credits
import game

credits_obj = credits.Credits()
menu_obj = menu.Menu()
game_obj = game.Game()

while not menu.menu_options["in_game"] and not menu.menu_options["exit"]:
    if menu.menu_options["in_credits"]:
        credits_obj.display_all()
    else:
        menu_obj.display_all()

while menu.menu_options["in_game"]:
    game_obj.display_all()
