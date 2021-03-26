import config
import pygame

class Button:
    __selected = False
    __button_font = config.font(32)
    __button_font_color = config.COLOR_LIGHT_GRAY

    def __init__(self, dimension: tuple, pos: tuple, content, event, color=config.COLOR_BLACK):
        self.__dimension = dimension
        self.pos = pos
        self.__rect = pos + dimension
        self.content = content
        self.event = event
        self.color = color

    def execute_action(self):
        self.event()

    def draw(self, surface):

        if self.__selected:
            self.__button_font_color = config.COLOR_BLACK
            self.color = config.COLOR_LIGHT_GRAY
        else:
            self.__button_font_color = config.COLOR_LIGHT_GRAY
            self.color = config.COLOR_BLACK
        pygame.draw.rect(surface, self.color, self.__rect)
        if self.content[:2] == './':
            config.display_img(surface, self.content, (self.pos[0] + 10, self.pos[1] + 10))
        else:
            config.display_msg(surface, self.__button_font, self.content, self.__button_font_color,
                               (self.pos[0] + (self.__dimension[0] - self.__button_font.size(self.content)[0])//2,
                                self.pos[1] + (self.__dimension[1] - self.__button_font.size(self.content)[1])//2))

    def get_selected(self):
        return self.__selected

    def set_selected(self, is_selected):
        self.__selected = is_selected


buttons_index = 0

def move_selected_button(direction, buttons_lst):
    global buttons_index
    buttons_lst[buttons_index].set_selected(False)
    if direction == "up":
        buttons_index -= 1
    elif direction == "down":
        buttons_index += 1
    if buttons_index > len(buttons_lst) - 1:
        buttons_index = 0
    elif buttons_index < 0:
        buttons_index = len(buttons_lst) - 1
    buttons_lst[buttons_index].set_selected(True)


def check_key(buttons_lst):
    global buttons_index
    for event in pygame.event.get():
        config.check_quit_event(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                move_selected_button("up", buttons_lst)
            elif event.key == pygame.K_s:
                move_selected_button("down", buttons_lst)
            if event.key == pygame.K_RETURN:
                buttons_lst[buttons_index].set_selected(False)
                buttons_lst[buttons_index].execute_action()
                buttons_index = 0
                buttons_lst[buttons_index].set_selected(True)
