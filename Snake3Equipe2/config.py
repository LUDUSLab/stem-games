import pygame

pygame.init()

COLOR_BLACK = (0, 0, 0)
COLOR_LIGHT_GRAY = (200, 200, 200)
window_size = (1280, 720)
center = (window_size[0] // 2, window_size[1] // 2)
screen = pygame.display.set_mode(window_size)

pygame.display.set_caption("Snake 3: Mad Kobra")


def font(size: int):
    path = "./assets/PressStart2P.ttf"
    return pygame.font.Font(path, size)


def display_msg(surface, fnt, message: str, color: tuple, pos: tuple):
    text = fnt.render(message, True, color)
    surface.blit(text, pos)


def display_img(surface, path: str, pos: tuple):
    image = pygame.image.load(path)
    surface.blit(image, pos)


def check_quit_event(event):
    if event.type == pygame.QUIT:
        pygame.quit()
        quit()

def exit_game():
    pygame.quit()
    quit()

class Button:
    __selected = False
    __button_font = font(32)
    __button_font_color = COLOR_LIGHT_GRAY

    def __init__(self, dimension: tuple, pos: tuple, content, event, color=COLOR_BLACK):
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
            self.__button_font_color = COLOR_BLACK
            self.color = COLOR_LIGHT_GRAY
        else:
            self.__button_font_color = COLOR_LIGHT_GRAY
            self.color = COLOR_BLACK
        pygame.draw.rect(surface, self.color, self.__rect)
        if self.content[:2] == './':
            display_img(surface, self.content, (self.pos[0] + 10, self.pos[1] + 10))
        else:
            display_msg(surface, self.__button_font, self.content, self.__button_font_color,
                        (self.pos[0] + (self.__dimension[0] - self.__button_font.size(self.content)[0])//2,
                         self.pos[1] + (self.__dimension[1] - self.__button_font.size(self.content)[1])//2))

    def get_selected(self):
        return self.__selected

    def set_selected(self, is_selected):
        self.__selected = is_selected

    def get_color(self):
        return self.color

    def set_color(self, new_color):
        self.color = new_color

    def get_rect(self):
        return self.__rect

    def get_content(self):
        return self.content

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
        check_quit_event(event)
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
