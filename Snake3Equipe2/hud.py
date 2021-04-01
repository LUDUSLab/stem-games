import config
import arena
import cube
import pygame

player_icon = pygame.image.load('assets/Player_head.png')
ai_icon = pygame.image.load('assets/Bot_head.png')


class Score(object):
    def __init__(self):
        self.font = config.font(25)
        self.text = self.font.render("Player " + str(arena.arena_obj.snake_player.score) + "X" +
                                     str(arena.arena_obj.snake_bot.score) + " AI", True, config.COLOR_LIGHT_GRAY)
        self.text_rect = self.text.get_rect()


class Hud(object):
    # __cube1 = cube.Cube((5, 1), (255, 0, 0))
    p1 = cube.Renderer((10, 1), player_icon)
    ia = cube.Renderer((21, 1), ai_icon)

    def __init__(self):
        self.score = Score()

    def display_score(self, surface):
        self.score = Score()
        self.score.text_rect.center = (640, 60)
        surface.blit(self.score.text, self.score.text_rect)

    def display_hud_cubes(self):
        self.p1.blit()
        self.ia.blit()


hud_obj = Hud()
