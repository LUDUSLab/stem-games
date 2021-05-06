import pygame
import config


class Header:
    def __init__(self, surface: pygame.Surface, text: str, size:int, ypos=580):
        self.surface = surface
        self.font_size = size
        self.font = config.font(self.font_size)
        self.color = config.COLOR_LIGHT_GRAY
        self.text = text
        self.pos = (config.window.size[0]/2 - self.font.size(text)[0]/2, ypos)

    def display(self):
        config.display_msg(self.surface, self.font, self.text, self.color, self.pos)

class Menu:
    surface = config.window.create_surface()
    start_game = False
    header = Header(surface, "1 COIN 1 PLAY", 36)
    footer = Header(surface, "STEM GAMES", 28, 660)
    header.display()
    footer.display()

    def __init__(self, bg_color: tuple = config.COLOR_BLACK):
        self.bg_color = bg_color

    def get_surface(self):
        return self.surface

    # def check_game_enter(self):
        # if key_pressed:
        #   self.start_game = True

menu_obj = Menu()
