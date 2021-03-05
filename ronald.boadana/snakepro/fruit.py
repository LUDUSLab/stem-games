import pygame

apple = pygame.image.load('../snake/assets/ronald.boadana_apple.png')
apple = pygame.transform.scale(apple, [20, 20])
apple_pos = ((random.randint(60, 560) // 10 * 10), (random.randint(60, 560) // 10 * 10))


def apple_randomness_movement():
    apple_x = (random.randint(60, 560) // 10 * 10)
    apple_y = (random.randint(60, 560) // 10 * 10)
    return apple_x, apple_y
