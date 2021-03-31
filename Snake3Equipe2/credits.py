import config
import menu
import button
import pygame

credits_options_key = ["back_to_menu"]
credits_options = {k: False for k in credits_options_key}


def go_back_to_menu():
    credits_options[credits_options_key[0]] = True
    menu.menu_options["in_credits"] = False


class Credits(object):
    back_button = button.Button(menu.menu_button_dimension, (menu.button_center_x, 500), "Back", go_back_to_menu)
    back_button.set_selected(True)
    surface = pygame.Surface(config.window.size)
    font = config.font(25)

    def display_credits(self, font_color):
        config.display_msg(self.surface, self.font, "Created by:", font_color,
                           (config.window.center[0] - self.font.size("Created by")[0] // 2,
                            config.window.center[1] - 250))
        config.display_msg(self.surface, self.font, "Matheus Nielsen", font_color,
                           (config.window.center[0] - self.font.size("Matheus Nielsen")[0] // 2,
                            config.window.center[1] - 200))
        config.display_msg(self.surface, self.font, "Natanael Lucena", font_color,
                           (config.window.center[0] - self.font.size("Natanael Lucena")[0] // 2,
                            config.window.center[1] - 150))
        config.display_msg(self.surface, self.font, "Josué Alves", font_color,
                           (config.window.center[0] - self.font.size("Josué Alves")[0] // 2,
                            config.window.center[1] - 100))
        config.display_msg(self.surface, self.font, "Ronald Boadana", font_color,
                           (config.window.center[0] - self.font.size("Ronald Boadana")[0] // 2,
                            config.window.center[1] - 50))

    def display_button(self):
        self.back_button.draw(self.surface)

    def update_surface(self):
        config.window.display_surface(self.surface)
        pygame.display.update()

    def display_all(self):
        self.display_credits(config.COLOR_LIGHT_GRAY)
        self.display_button()
        button.check_key([self.back_button])
        self.update_surface()


credits_obj = Credits()
