from config import *


def wall_draw():
    screen.blit(wall_sprite_corner1, (0, 32))
    screen.blit(wall_sprite_corner2, (768, 32))
    screen.blit(wall_sprite_corner3, (0, 608))
    screen.blit(wall_sprite_corner4, (768, 608))
    screen.blit(obstacle, (128, 160))
    screen.blit(obstacle, (384, 384))
    screen.blit(obstacle, (640, 160))
    screen.blit(obstacle, (128, 512))
    screen.blit(obstacle, (640, 512))
    screen.blit(obstacle, (384, 256))

    for c in range(32, 768, 32):
        screen.blit(wall_sprite1, (c, 32))
        screen.blit(wall_sprite1, (c, 608))

    for c in range(64, 608, 32):
        screen.blit(wall_sprite2, (0, c))
        screen.blit(wall_sprite2, (768, c))


wall_sprite1 = pygame.image.load('assets/wall_sprite1.png')
wall_sprite2 = pygame.image.load('assets/wall_sprite2.png')
wall_sprite_corner1 = pygame.image.load('assets/wall_sprite_corner1.png')
wall_sprite_corner2 = pygame.image.load('assets/wall_sprite_corner2.png')
wall_sprite_corner3 = pygame.image.load('assets/wall_sprite_corner3.png')
wall_sprite_corner4 = pygame.image.load('assets/wall_sprite_corner4.png')
obstacle = pygame.image.load('assets/obstacle.png')
