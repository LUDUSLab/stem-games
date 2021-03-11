from config import *


def snake_move(moves):

    if moves == LEFT:
        for c in range(len(snake_position) - 1, 0, -1):
            snake_position[c] = (snake_position[c - 1][0], snake_position[c - 1][1])

        snake_position[0] = (snake_position[0][0] - 32, snake_position[0][1])

    if moves == UP:
        for c in range(len(snake_position) - 1, 0, -1):
            snake_position[c] = (snake_position[c - 1][0], snake_position[c - 1][1])

        snake_position[0] = (snake_position[0][0], snake_position[0][1] - 32)

    if moves == RIGHT:
        for c in range(len(snake_position) - 1, 0, -1):
            snake_position[c] = (snake_position[c - 1][0], snake_position[c - 1][1])

        snake_position[0] = (snake_position[0][0] + 32, snake_position[0][1])

    if moves == DOWN:
        for c in range(len(snake_position) - 1, 0, -1):
            snake_position[c] = (snake_position[c - 1][0], snake_position[c - 1][1])

        snake_position[0] = (snake_position[0][0], snake_position[0][1] + 32)


def snake_draw():
    snake = pygame.Surface(square)
    snake.fill(color_0F6E9D)

    for c in range(1, len(snake_position)):
        screen.blit(snake_sprite, snake_position[0])
        screen.blit(snake, snake_position[c])


snake_position = [(160, 320), (128, 320), (96, 320)]

# keys
LEFT, UP, RIGHT, DOWN = 37, 38, 39, 40

snake_sprite = pygame.image.load('assets/snake_sprite.png')
