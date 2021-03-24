import pygame

import config

menu_surf = pygame.Surface(config.window_size)


class Menu:
    game_title_font = config.font(64)

    def __init__(self, buttons: list, surface: pygame.Surface = menu_surf, bg_color: tuple = config.COLOR_BLACK):
        self.surface = surface
        self.bg_color = bg_color
        self.buttons = buttons

    def draw_header(self, font_color):
        config.display_msg(self.surface, self.game_title_font, "MAD KOBRA", font_color,
                           (config.center[0] - self.game_title_font.size("MAD KOBRA")[0] // 2, config.center[1] - 200))

    def draw_buttons(self):
        for button in self.buttons:
            button.draw(self.surface)


menu_button_dimension = (240, 50)
button_center_x = config.center[0] - menu_button_dimension[0] // 2

play_button = config.Button(menu_button_dimension, (button_center_x, 300), menu_button_dimension, "Play")
credits_button = config.Button(menu_button_dimension, (button_center_x, 400), menu_button_dimension, "Credits")
exit_button = config.Button(menu_button_dimension, (button_center_x, 500), menu_button_dimension, "Exit")
menu_buttons = [play_button, credits_button, exit_button]

menu = Menu(menu_buttons)

selected_index = 0

def display_menu():
    global selected_index
    for event in pygame.event.get():
        config.check_quit_event(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                menu.buttons[selected_index].set_selected(False)
                selected_index -= 1
            elif event.key == pygame.K_s:
                menu.buttons[selected_index].set_selected(False)
                selected_index += 1
            if event.key == pygame.K_RETURN:
                config.in_menu = False
                config.options[config.options_key[selected_index]] = True
                menu_surf.fill((0, 0, 0))
    config.display_msg(menu_surf, menu.game_title_font, "MAD KOBRA", config.COLOR_LIGHT_GRAY,
                       (config.center[0] - menu.game_title_font.size("MAD KOBRA")[0] // 2, config.center[1] - 200))
    config.screen.blit(menu_surf, (0, 0))

    if selected_index > len(menu.buttons) - 1:
        selected_index = 0
    elif selected_index < 0:
        selected_index = len(menu.buttons) - 1
    menu.buttons[selected_index].set_selected(True)
    for button in [play_button, credits_button, exit_button]:
        button.draw(menu_surf)
    pygame.display.update()
