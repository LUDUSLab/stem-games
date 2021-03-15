from screen import *
import pygame
from apple import get_points

wall = pygame.image.load('assets/matheus.nielsen_wall.png')
corner = pygame.image.load('assets/matheus.nielsen_wall_corner.png')

# score text render
score_font = pygame.font.Font('assets/PressStart2P.ttf', 32)
score_text = score_font.render('Score: 0', False, color_white)
score_rect = score_text.get_rect()
score_rect.center = (screen_size[0] / 2, hud_y / 2)


def blit():

    # wall tile render
    for square in range(0, screen_size[1], grid_square):
        screen.blit(pygame.transform.rotate(wall, 90), (square, hud_y))

    for square in range(0, screen_size[1], grid_square):
        screen.blit(pygame.transform.rotate(wall, -90), (square, screen_size[1] - grid_square))

    for square in range(hud_y + grid_square, screen_size[0] + 2 * grid_square, grid_square):
        screen.blit(pygame.transform.rotate(wall, -180), (0, square))

    for square in range(hud_y + grid_square, screen_size[0] + 2 * grid_square, grid_square):
        screen.blit(wall, (screen_size[0] - grid_square, square))

    # wall corner render
    screen.blit(pygame.transform.rotate(corner, -90), (0, hud_y))
    screen.blit(pygame.transform.rotate(corner, 180), (screen_size[0] - grid_square, hud_y))
    screen.blit(pygame.transform.rotate(corner, 0), (0, screen_size[1] - grid_square))
    screen.blit(pygame.transform.rotate(corner, 90), (screen_size[0] - grid_square, screen_size[1] - grid_square))

    # score rectangle render
    pygame.draw.rect(screen, color_gray, (0, 0, screen_size[0], hud_y))

# prints score on hud
def score_blit():
    points = get_points()
    score_text = score_font.render('Score: ' + str(points), False, color_white)
    screen.blit(score_text, score_rect)
