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
    font_1 = config.font(25)
    font_2 = config.font(15)

    def display_credits(self, font_color):
        config.display_msg(self.surface, self.font_1, "Created by:", font_color,
                           (config.window.center[0] - self.font_1.size("Created by")[0] // 2,
                            config.window.center[1] - 300))
        config.display_msg(self.surface, self.font_1, "Matheus Nielsen", font_color,
                           (config.window.center[0] - self.font_1.size("Matheus Nielsen")[0] // 2,
                            config.window.center[1] - 250))
        config.display_msg(self.surface, self.font_1, "Natanael Lucena", font_color,
                           (config.window.center[0] - self.font_1.size("Natanael Lucena")[0] // 2,
                            config.window.center[1] - 200))
        config.display_msg(self.surface, self.font_1, "Josué Alves", font_color,
                           (config.window.center[0] - self.font_1.size("Josué Alves")[0] // 2,
                            config.window.center[1] - 150))
        config.display_msg(self.surface, self.font_1, "Ronald Boadana", font_color,
                           (config.window.center[0] - self.font_1.size("Ronald Boadana")[0] // 2,
                            config.window.center[1] - 100))
        config.display_msg(self.surface, self.font_2, "Font:'Press Start 2P' https://www.fontspace.com/code88man38"
                                                      "/press-start-2pa", font_color,
                           (config.window.center[0] - self.font_2.size("Font:'Press Start 2P' "
                                                                       "https://www.fontspace.com/code88man38/press"
                                                                       "-start-2pa")[0] + 555,
                            config.window.center[1] - 25))
        config.display_msg(self.surface, self.font_2, "Sounds:", font_color,
                           (config.window.center[0] - self.font_2.size("Sounds:")[0] - 465,
                            config.window.center[1]))
        config.display_msg(self.surface, self.font_2, "Menu sound: https://freesound.org/people/furbyguy"
                                                      "/sounds/368068/", font_color,
                           (config.window.center[0] - self.font_2.size("Menu sound: https://freesound.org/people"
                                                                       "/furbyguy/sounds/368068/")[0] + 390,
                            config.window.center[1] + 25))
        config.display_msg(self.surface, self.font_2, "Eating sound: https://freesound.org/people/Clearwavsound"
                                                      "/sounds/524607/", font_color,
                           (config.window.center[0] -
                            self.font_2.size("Eating sound: https://freesound.org/people"
                                             "/Clearwavsound/sounds/524607/")[0] + 495,
                            config.window.center[1] + 50))
        config.display_msg(self.surface, self.font_2, "Game sound: https://freesound.org/people"
                                                      "/ValentinSosnitskiy/sounds/510823/", font_color,
                           (config.window.center[0] -
                            self.font_2.size("Game sound: https://freesound.org/people"
                                             "/ValentinSosnitskiy/sounds/510823")[0] + 525,
                            config.window.center[1] + 75))

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
