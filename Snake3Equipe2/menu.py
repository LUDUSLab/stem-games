import pygame
import button
import config

menu_button_dimension = (240, 50)
button_center_x = config.window.center[0] - 600

menu_options_key = ["in_game", "in_credits", "exit"]
menu_options = {k: False for k in menu_options_key}


def go_to_credits():
    menu_options["in_credits"] = True


def go_to_game():
    menu_options["in_game"] = True


def create_menu_button(y_axis, content, action):
    return button.Button(menu_button_dimension, (button_center_x, y_axis), content, action)


play_button = create_menu_button(300, "Play", go_to_game)
credits_button = create_menu_button(400, "Credits", go_to_credits)
exit_button = create_menu_button(500, "Exit", config.exit_game)


class Menu:
    surface = config.window.create_surface()

    def __init__(self, buttons: list, bg_color: tuple = config.COLOR_BLACK):
        self.bg_color = bg_color
        self.buttons = buttons
        self.buttons[0].set_selected(True)

    def display_header(self):
        pygame.Surface.blit(self.surface, config.menu_image, (0, 0))

    def display_buttons(self):
        for b in self.buttons:
            b.draw(self.surface)

    def update_surface(self):
        config.window.display_surface(self.surface)
        self.surface.fill(self.bg_color)
        pygame.display.update()

    def display_all(self):
        self.display_header()
        self.display_buttons()
        button.check_key(self.buttons)
        self.update_surface()


menu_obj = Menu([play_button, credits_button, exit_button])
