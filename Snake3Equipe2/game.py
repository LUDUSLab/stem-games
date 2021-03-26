import pygame
import config
import arena

class Game(object):
    def __init__(self):
        self.surface = config.window.create_surface()
        self.arena = arena.Arena(config.window.size)
        self.snake = self.arena.snake
        self.clock = pygame.time.Clock()
        self.framerate = 10

    def display_surface(self):
        config.window.display_surface(self.surface)

    def display_all(self):
        self.clock.tick(self.framerate)
        self.display_surface()
        self.snake.move()
        self.snake.collision_with_herself()
        self.arena.collision_with_snake()
        self.arena.redraw_window(self.surface)
        pygame.display.update()