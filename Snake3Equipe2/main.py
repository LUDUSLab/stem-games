import menu
import config
import credits

while not config.options["in_game"] and not config.options["exit"]:
    menu.display_menu()

    if config.options["in_credits"]:
        credits.display_credits()


# game.display_game()
