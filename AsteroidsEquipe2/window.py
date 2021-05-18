import pygame

class Window:
    def __init__(self, size: tuple = (1280, 720), caption: str = "Asteroids"):
        self.size = size
        self.screen = pygame.Surface = pygame.display.set_mode(size)
        pygame.display.set_caption(caption)
