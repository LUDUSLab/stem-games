from config import *


def snake_move(moves):

    if moves == LEFT:
        snake_position[0] = (snake_position[0][0] - 32, snake_position[0][1])

        for c in range(len(snake_position) - 1, 0, -1):
            snake_position[c] = (snake_position[c - 1][0], snake_position[c - 1][1])

    if moves == UP:
        snake_position[0] = (snake_position[0][0], snake_position[0][1] - 32)

        for c in range(len(snake_position) - 1, 0, -1):
            snake_position[c] = (snake_position[c - 1][0], snake_position[c - 1][1])

    if moves == RIGHT:
        snake_position[0] = (snake_position[0][0] + 32, snake_position[0][1])

        for c in range(len(snake_position) - 1, 0, -1):
            snake_position[c] = (snake_position[c - 1][0], snake_position[c - 1][1])

    if moves == DOWN:
        snake_position[0] = (snake_position[0][0], snake_position[0][1] + 32)

        for c in range(len(snake_position) - 1, 0, -1):
            snake_position[c] = (snake_position[c - 1][0], snake_position[c - 1][1])


def snake_draw():
    snake = pygame.Surface(square)
    snake.fill(color_green)

    for c in range(0, len(snake_position)):
        if c == 0:
            screen.blit(snake_sprite, snake_position[c])
        else:
            screen.blit(snake, snake_position[c])


snake_position = [(64, 0), (32, 0), (0, 0)]

# keys
LEFT, UP, RIGHT, DOWN = 37, 38, 39, 40

snake_sprite = pygame.image.load('assets/snake_sprite.png')
