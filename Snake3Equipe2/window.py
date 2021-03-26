import pygame

class Window(object):
    def __init__(self, size: tuple = (1280, 720), caption: str = "Snake 3: Mad Kobra"):
        self.size = size
        self.center = (size[0] // 2, size[1] // 2)
        self.screen = pygame.display.set_mode(size)
        self.caption = caption

    def create_surface(self):
        return pygame.Surface(self.size)

    def display_surface(self, surface, pos=(0, 0)):
        self.screen.blit(surface, pos)
