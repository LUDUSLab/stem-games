import pygame

apple = pygame.image.load('../snakepro/assets/ronald.boadana_apple.png')
apple_pos = ((random.randint(60, 560) // 10 * 10), (random.randint(60, 560) // 10 * 10))


def apple_randomness_movement():
    apple_x = (random.randint(60, 560) // 10 * 10)
    apple_y = (random.randint(60, 560) // 10 * 10)
    return apple_x, apple_y


grape = pygame.image.load('../snakepro/assets/ronald.boadana_grape.png.')
grape_pos = ((random.randint(60, 560) // 10 * 10), (random.randint(60, 560) // 10 * 10))


def grape_randomness_movement():
    grape_x = (random.randint(60, 560) // 10 * 10)
    grape_y = (random.randint(60, 560) // 10 * 10)
    return grape_x, grape_y


strawberry = pygame.image.load('../snakepro/assets/ronald.boadana_strawberry.png.')
strawberry_pos = ((random.randint(60, 560) // 10 * 10), (random.randint(60, 560) // 10 * 10))


def strawberry_randomness_movement():
    strawberry_x = (random.randint(60, 560) // 10 * 10)
    strawberry_y = (random.randint(60, 560) // 10 * 10)
    return strawberry_x, strawberry_y
