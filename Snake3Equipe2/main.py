import menu
import credits
import game


while not menu.menu_options["in_game"] and not menu.menu_options["exit"]:
    if menu.menu_options["in_credits"]:
        credits.credits_obj.display_all()
    else:
        menu.menu_obj.display_all()

while menu.menu_options["in_game"]:
    game.game_obj.display_all()
