import pygame
import config
import arena
import hud


class Game(object):
    def __init__(self):
        self.surface = config.window.create_surface()
        self.arena = arena.arena_obj
        self.snake_player = self.arena.snake_player
        self.clock = pygame.time.Clock()
        self.hud = hud.hud_obj
        self.framerate = 10

    def display_surface(self):
        config.window.display_surface(self.surface)

    def display_all(self):
        self.clock.tick(self.framerate)
        self.hud.display_hud_cubes(self.surface)
        self.display_surface()
        self.hud.display_score()
        self.snake_player.move()
        self.snake_player.collision_with_herself()
        self.arena.collision_with_snake()
        self.arena.collision_fruit_snake()
        self.arena.redraw_window(self.surface)
        pygame.display.update()

game_obj = Game()