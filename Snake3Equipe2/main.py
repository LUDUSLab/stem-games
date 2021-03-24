import menu
import config
import credits
import game

while not config.options["in_game"] and not config.options["exit"]:
    menu.display_menu()

    if config.options["in_credits"]:
        credits.display_credits()

while config.options["in_game"]:
    game.display_game()
