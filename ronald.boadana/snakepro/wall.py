from config import *


def wall_pos():
    wall = pygame.image.load('./assets/ronald.boadana_wall.png')
    for i in range(0, 800, 32):
        screen.blit(wall, (i, 0))
        screen.blit(wall, (i, 576))

    for i in range(32, 640, 32):
        screen.blit(wall, (0, i))
        screen.blit(wall, (768, i))
