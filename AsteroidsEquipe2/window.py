import pygame

class Window:
    def __init__(self, size: tuple = (1280, 720), caption: str = "Asteroids"):
        self.size = size
        self.screen = pygame.Surface = pygame.display.set_mode(size)
        pygame.display.set_caption(caption)

    def create_surface(self):
        return pygame.surface.Surface(self.size)

    def display_surface(self, surface: pygame.Surface):
        self.screen.blit(surface, (0, 0))
        pygame.display.flip()