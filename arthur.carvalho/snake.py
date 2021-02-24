import pygame
from random import randint

pygame.init()

# Screen configuration
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Snake')

# snake set
snake = pygame.Surface((10, 10))
snake.fill((0, 255, 0))
snake_position = [250, 250]

# Apple set
apple = pygame.Surface((10, 10))
apple.fill((255, 0, 0))
apple_position = (randint(0, 490), randint(0, 490))

game_loop = True

while game_loop:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        # map keys
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake_position[1] -= 10
                print(snake_position)

            elif event.key == pygame.K_DOWN:
                snake_position[1] += 10
                print(snake_position)

            elif event.key == pygame.K_LEFT:
                snake_position[0] -= 10
                print(snake_position)

            elif event.key == pygame.K_RIGHT:
                snake_position[0] += 10
                print(snake_position)

    screen.fill((0, 0, 0))

    screen.blit(apple, apple_position)
    screen.blit(snake, snake_position)

    pygame.display.update()
