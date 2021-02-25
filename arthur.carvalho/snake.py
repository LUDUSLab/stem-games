import pygame
from random import randint


def body_snake():
    screen.blit(snake, snake_position)


pygame.init()

# Screen configuration
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Snake')

# snake set
snake = pygame.Surface((10, 10))
snake.fill((0, 255, 0))
snake_position = [250, 250]
UP = DOWN = LEFT = RIGHT = False

# Apple set
apple = pygame.Surface((10, 10))
apple.fill((255, 0, 0))
apple_position = [randint(0, 490) // 10 * 10, randint(0, 490) // 10 * 10]

game_loop = True

while game_loop:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        # map keys
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                UP = True
                DOWN = LEFT = RIGHT = False

            elif event.key == pygame.K_DOWN:
                DOWN = True
                UP = LEFT = RIGHT = False

            elif event.key == pygame.K_LEFT:
                LEFT = True
                UP = DOWN = RIGHT = False

            elif event.key == pygame.K_RIGHT:
                RIGHT = True
                UP = DOWN = LEFT = False

    if UP:
        snake_position[1] -= 0.1

    elif DOWN:
        snake_position[1] += 0.1

    elif LEFT:
        snake_position[0] -= 0.1

    elif RIGHT:
        snake_position[0] += 0.1

    if snake_position[0] == apple_position:
        apple_position = [randint(0, 490) // 10 * 10, randint(0, 490) // 10 * 10]

    screen.fill((0, 0, 0))

    screen.blit(apple, apple_position)
    body_snake()

    pygame.display.update()
