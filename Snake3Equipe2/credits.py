import config
import menu
import pygame

credits_options_key = ["back_to_menu"]
credits_options = {k: False for k in credits_options_key}

def go_back_to_menu():
    credits_options[credits_options_key[0]] = True

class Credits(object):
    back_button = config.Button(menu.menu_button_dimension, (menu.button_center_x, 500),
                                menu.menu_button_dimension, "Back",
                                go_back_to_menu())
    back_button.set_selected(True)
    surface = pygame.Surface(config.window_size)

    def display_button(self):
        self.back_button.draw(self.surface)

    def update_surface(self):
        config.screen.blit(self.surface, (0, 0))
        pygame.display.update()

    def display_all(self):
        self.display_button()
        config.check_key([self.back_button])
        self.update_surface()
