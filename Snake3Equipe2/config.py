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


def set_obj_coordinates(obj, x, y):
    obj.x = x
    obj.y = y


def check_quit_event(event):
    if event.type == pygame.QUIT:
        pygame.quit()
        quit()


in_menu = True
options_key = ["in_game", "in_credits", "exit"]
options = {k: False for k in options_key}


class Button:
    __selected = False
    __button_font = font(32)
    __button_font_color = COLOR_LIGHT_GRAY
    __button_rect = ()

    def __init__(self, dimension: tuple, pos: tuple, rect: tuple, content: str, color=COLOR_BLACK):
        self.dimension = dimension
        self.pos = pos
        self.color = color
        self.rect = rect
        self.content = content
        self.button_rect = pos + rect

    def draw(self, surface):
        if self.__selected:
            self.__button_font_color = COLOR_BLACK
            self.color = COLOR_LIGHT_GRAY
        else:
            self.__button_font_color = COLOR_LIGHT_GRAY
            self.color = COLOR_BLACK
        pygame.draw.rect(surface, self.color, self.pos + self.rect)
        if self.content[:2] == './':
            display_img(surface, self.content, (self.pos[0] + 10, self.pos[1] + 10))
        else:
            display_msg(surface, self.__button_font, self.content, self.__button_font_color,
                        (self.pos[0] + (self.dimension[0] - self.__button_font.size(self.content)[0])//2,
                         self.pos[1] + (self.dimension[1] - self.__button_font.size(self.content)[1])//2))

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