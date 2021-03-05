import pygame

snake = [(200, 200), (220, 200), (240, 200)]
snake_head = pygame.image.load('../snake/assets/ronald.boadana_snakehead.png')
snake_head = pygame.transform.scale(snake_head, [20, 20])
snake_head_pos = (snake[0][0] + 20, snake[0][1])
snake_body = pygame.image.load('../snake/assets/ronald.boadana_snake_body_up_down.png')
snake_body = pygame.transform.scale(snake_body, [20, 20])