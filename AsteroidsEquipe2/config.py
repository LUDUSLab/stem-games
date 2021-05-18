import window
import pygame

from itertools import cycle

pygame.init()

COLOR_BLACK = (0, 0, 0)
COLOR_LIGHT_GRAY = (154, 154, 154)

BLINK_EVENT = pygame.USEREVENT + 0

framerate = 60
clock = pygame.time.Clock()

window = window.Window()
middle = (window.size[0]/2, window.size[1]/2)

class Blinker:
    def __init__(self, text, font, message):
        self.on_text_surface = text
        self.blink_rect = self.on_text_surface.get_rect()
        self.blink_rect.center = ((window.size[0] - font.size(message)[0])/2 + 125, 120)
        self.off_text_surface = pygame.surface.Surface(self.blink_rect.size)
        self.blink_surfaces = cycle([self.on_text_surface, self.off_text_surface])
        self.blink_surface = next(self.blink_surfaces)
        pygame.time.set_timer(BLINK_EVENT, 540)

    def check_blink_event(self, event):
        if event.type == BLINK_EVENT:
            self.blink_surface = next(self.blink_surfaces)


class Text:
    def __init__(self, message: str, size: int, pos=(0, 0), path="./assets/VectorBattle-e9XO.ttf",
                 color=COLOR_LIGHT_GRAY, blink=False):
        self.message = message
        self.size = size
        self.pos = pos
        self.path = path
        self.color = color
        self.blink = blink
        self.font = pygame.font.Font(self.path, self.size)
        self.text = self.font.render(self.message, True, self.color)
        if self.blink:
            self.blinker = Blinker(self.text, self.font, self.message)

    def display(self):
        if self.blink:
            window.screen.blit(self.blinker.blink_surface, self.blinker.blink_rect)
        else:
            window.screen.blit(self.text, self.pos)


def check_quit_event(event):
    if event.type == pygame.QUIT:
        pygame.quit()
        quit()
