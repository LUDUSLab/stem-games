import pygame

import config

menu = pygame.Surface(config.window_size)
game_title_font = config.font(64)
menu_button_dimension = (240, 50)
button_center_x = config.center[0] - menu_button_dimension[0] // 2


class Button(object):
    __selected = False
    __button_font = config.font(32)
    __button_font_color = config.COLOR_LIGHT_GRAY
    __button_rect = ()

    def __init__(self, pos: tuple, rect: tuple, content: str, color=config.COLOR_BLACK):
        self.pos = pos
        self.color = color
        self.rect = rect
        self.content = content
        self.button_rect = pos + rect

    def draw(self, surface):
        if self.__selected:
            self.__button_font_color = config.COLOR_BLACK
            self.color = config.COLOR_LIGHT_GRAY
        else:
            self.__button_font_color = config.COLOR_LIGHT_GRAY
            self.color = config.COLOR_BLACK
        pygame.draw.rect(surface, self.color, self.pos + self.rect)
        if self.content[:2] == './':
            config.display_img(surface, self.content, (self.pos[0] + 10, self.pos[1] + 10))
        else:
            config.display_msg(surface, self.__button_font, self.content, self.__button_font_color,
                               (self.pos[0] + (menu_button_dimension[0] - self.__button_font.size(self.content)[0])//2,
                                self.pos[1] + (menu_button_dimension[1] - self.__button_font.size(self.content)[1])//2))

    def get_selected(self):
        return self.__selected

    def set_selected(self, is_selected):
        self.__selected = is_selected

    def get_color(self):
        return self.color

    def set_color(self, new_color):
        self.color = new_color

    def get_button_rect(self):
        return self.__button_rect

    def get_content(self):
        return self.content


play_button = Button((button_center_x, 300), menu_button_dimension, "Play")
credits_button = Button((button_center_x, 400), menu_button_dimension, "Credits")
exit_button = Button((button_center_x, 500), menu_button_dimension, "Exit")
buttons = [play_button, credits_button, exit_button]
selected_index = 0


def display_menu():
    global selected_index
    for event in pygame.event.get():
        config.check_quit_event(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                buttons[selected_index].set_selected(False)
                selected_index -= 1
            elif event.key == pygame.K_s:
                buttons[selected_index].set_selected(False)
                selected_index += 1
            if event.key == pygame.K_RETURN:
                config.in_menu = False
                config.options[config.options_key[selected_index]] = True
                menu.fill((0, 0, 0))
    config.display_msg(menu, game_title_font, "MAD KOBRA", config.COLOR_LIGHT_GRAY,
                       (config.center[0] - game_title_font.size("MAD KOBRA")[0] // 2, config.center[1] - 200))
    config.screen.blit(menu, (0, 0))

    if selected_index > len(buttons) - 1:
        selected_index = 0
    elif selected_index < 0:
        selected_index = len(buttons) - 1
    buttons[selected_index].set_selected(True)
    for button in [play_button, credits_button, exit_button]:
        button.draw(menu)
    pygame.display.update()
