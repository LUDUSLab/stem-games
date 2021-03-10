import random
from config import *

apple = pygame.image.load('../snakepro/assets/ronald.boadana_apple.png')
apple_pos = ((random.randint(60, 560) // 32 * 32), (random.randint(60, 560) // 32 * 32))


def apple_randomness_movement():
    apple_x = (random.randint(60, 560) // 32 * 32)
    apple_y = (random.randint(60, 560) // 32 * 32)
    return apple_x, apple_y


grape = pygame.image.load('../snakepro/assets/ronald.boadana_grape.png')
grape_pos = (1000, 1000)


def grape_randomness_movement():
    grape_x = (random.randint(60, 560) // 10 * 10)
    grape_y = (random.randint(60, 560) // 10 * 10)
    return grape_x, grape_y


strawberry = pygame.image.load('../snakepro/assets/ronald.boadana_strawberry.png')
strawberry_pos = (1000, 1000)


def strawberry_randomness_movement():
    strawberry_x = (random.randint(60, 560) // 10 * 10)
    strawberry_y = (random.randint(60, 560) // 10 * 10)
    return strawberry_x, strawberry_y
