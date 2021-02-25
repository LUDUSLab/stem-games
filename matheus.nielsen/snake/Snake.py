# Snake with Pygame by Matheus Nielsen 2021
# Pygame website https://www.pygame.org/news
# Version 0.0 "No code yet"
# Bite sfx by Koops available at https://freesound.org/people/Koops/sounds/20269/

import pygame

pygame.init()

# Screen render
screen_size = (640, 640)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Snake with Pygame - Version 0.0")

# Apple render
apple = pygame.image.load("Apple.png")

# Snake render
snake_head = pygame.image.load("Snake Head Protorype.png")
snake_body = pygame.image.load("Snake Body Prototype.png")
snake_tail = pygame.image.load("Snake Tail.png")
snake_head_y = 320
snake_head_x = 320



# game loop
game_loop = True
game_clock = pygame.time.Clock()

while game_loop is True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop = False

        #  keystroke events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                print('a')
            if event.key == pygame.K_LEFT:
                print('b')
    snake_head_x += 32
    screen.fill((0, 0, 0))
    screen.blit(apple, (0, 0))
    screen.blit(snake_head, (snake_head_x, snake_head_y))
    screen.blit(snake_body, (32, 32))

    # update screen
    pygame.display.flip()
    game_clock.tick(4)

pygame.quit()