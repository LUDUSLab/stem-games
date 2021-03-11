from config import *

wall = pygame.image.load('./assets/ronald.boadana_wall.png')


# drawing the borders
def wall_pos():
    for i in range(0, 800, 32):
        screen.blit(wall, (i, 0))
        screen.blit(wall, (i, 576))

    for i in range(32, 640, 32):
        screen.blit(wall, (0, i))
        screen.blit(wall, (768, i))


# drawing the obstacles on the map
def wall_obstacles():
    wall_1 = (192, 32)
    wall_2 = (192, 64)
    wall_3 = (608, 32)
    wall_4 = (608, 64)
    wall_5 = (32, 160)
    wall_6 = (64, 160)
    wall_7 = (416, 160)
    wall_8 = (416, 192)
    wall_9 = (416, 224)
    wall_10 = (480, 320)
    wall_11 = (480, 352)
    wall_12 = (480, 384)
    wall_13 = (736, 416)
    wall_14 = (704, 416)
    wall_15 = (672, 416)
    wall_16 = (32, 384)
    wall_17 = (64, 384)
    wall_18 = (224, 544)
    wall_19 = (224, 512)
    wall_20 = (224, 480)

    screen.blit(wall, wall_1)
    screen.blit(wall, wall_2)
    screen.blit(wall, wall_3)
    screen.blit(wall, wall_4)
    screen.blit(wall, wall_5)
    screen.blit(wall, wall_6)
    screen.blit(wall, wall_7)
    screen.blit(wall, wall_8)
    screen.blit(wall, wall_9)
    screen.blit(wall, wall_10)
    screen.blit(wall, wall_11)
    screen.blit(wall, wall_12)
    screen.blit(wall, wall_13)
    screen.blit(wall, wall_14)
    screen.blit(wall, wall_15)
    screen.blit(wall, wall_16)
    screen.blit(wall, wall_17)
    screen.blit(wall, wall_18)
    screen.blit(wall, wall_19)
    screen.blit(wall, wall_20)
