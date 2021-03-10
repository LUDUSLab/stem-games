import pygame
# create a game.py file and place the functions and variables related to the game as a whole
import config

pygame.init()

screen = pygame.display.set_mode((config.screen_length, config.screen_height))
pygame.display.set_caption('Snake')
score_font = config.font_(size=20)


def pencil(text, color):
    message = score_font.render('%s' % text, True, color)
    return message


def write(text, color, surface, x, y):
    pen = pencil(text, color)
    surface.blit(pen, (x, y))


def game_loop():
    while True:
        screen.fill(config.royalblue)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        screen.blit(config.background, (config.bg_x, config.bg_y))
        screen.blit(config.walls, (config.bg_x, config.bg_y))

        pygame.display.flip()
