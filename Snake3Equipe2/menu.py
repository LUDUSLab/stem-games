import pygame
import button
import config

menu_button_dimension = (240, 50)
button_center_x = config.window.center[0] - menu_button_dimension[0] // 2

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

buttons = [play_button, credits_button, exit_button]

buttons[0].set_selected(True)

class Menu:
    game_title_font = config.font(64)
    surface = pygame.Surface(config.window.size)

    def __init__(self, bg_color: tuple = config.COLOR_BLACK):
        self.bg_color = bg_color

    def display_header(self, font_color):
        config.display_msg(self.surface, self.game_title_font, "MAD KOBRA", font_color,
                           (config.window.center[0] - self.game_title_font.size("MAD KOBRA")[0] // 2,
                            config.window.center[1] - 200))

    def display_buttons(self):
        for b in buttons:
            b.draw(self.surface)

    def update_surface(self):
        config.window.display_surface(self.surface)
        self.surface.fill(self.bg_color)
        pygame.display.update()

    def display_all(self):
        self.display_header(config.COLOR_LIGHT_GRAY)
        self.display_buttons()
        button.check_key(buttons)
        self.update_surface()

menu_obj = Menu()