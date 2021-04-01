import pygame
import config
import arena
import hud


class Game(object):
    def __init__(self):
        self.surface = config.window.create_surface()
        self.arena = arena.arena_obj
        self.snake_player = self.arena.snake_player
        self.snake_bot = self.arena.snake_bot
        self.clock = pygame.time.Clock()
        self.hud = hud.hud_obj
        self.framerate = 10
        self.delay = 80

    def display_surface(self):
        config.window.display_surface(self.surface)

    def display_all(self):
        self.clock.tick(self.framerate)
        pygame.time.delay(self.delay)
        self.hud.display_hud_cubes(self.surface)
        self.hud.display_score(self.surface)
        self.display_surface()
        self.arena.collision_with_snake()
        self.arena.collision_fruit_snake()
        self.arena.collision_obstacles()
        self.snake_bot.collision_with_herself()
        self.snake_player.collision_with_herself()
        self.arena.collision_between_snakes()
        self.snake_bot.move(self.arena.fruit.pos, self.arena.obstacle_matrix)
        self.snake_player.move()
        self.arena.redraw_window(self.surface)
        pygame.display.update()

game_obj = Game()