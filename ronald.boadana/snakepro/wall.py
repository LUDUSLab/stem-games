from config import *

wall = pygame.image.load('../snakepro/assets/ronald.boadana_wall.png')


def draw_borders():
    pygame.draw.line(screen, color_white, [10, 50], [590, 50], 3)
    pygame.draw.line(screen, color_white, [10, 590], [590, 590], 3)
    pygame.draw.line(screen, color_white, [10, 50], [10, 590], 3)
    pygame.draw.line(screen, color_white, [590, 50], [590, 590], 3)
