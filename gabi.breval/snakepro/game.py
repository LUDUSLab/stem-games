from obstacles import *
from snake import *
from fruit import *
from wall import *
from config import *

while True:

    clock.tick(20)

    snake_head_pos = (snake[0])

    for event in pygame.event.get():  # identifies what was clicked
        if event.type == QUIT:
            pygame.quit()
        if event.type == KEYDOWN:

            if event.key == K_UP:
                if my_direction == DOWN:
                    pass
                else:
                    my_direction = UP

            if event.key == K_DOWN:
                if my_direction == UP:
                    pass
                else:
                    my_direction = DOWN

            if event.key == K_LEFT:
                if my_direction == RIGHT:
                    pass
                else:
                    my_direction = LEFT

            if event.key == K_RIGHT:
                if my_direction == LEFT:
                    pass
                else:
                    my_direction = RIGHT

    snake_moviment()
    obstacle_pos = missiles_pos(obstacle_pos)

    # Checking collision -------------------------------------------------------------------------------------------- #
    cobra = pygame.draw.rect(screen, (0, 255, 0), (snake[0][0], snake[0][1], 32, 32))
    fruit = pygame.draw.rect(screen, (255, 0, 0), (apple_food_pos[0], apple_food_pos[1], 32, 32))
    bomb1 = pygame.draw.rect(screen, (255, 0, 0), (obstacle_pos[0], obstacle_pos[1], 40, 40))
    bomb2 = pygame.draw.rect(screen, (255, 0, 0), (obstacle_pos2[0], obstacle_pos2[1], 40, 40))
    bomb3 = pygame.draw.rect(screen, (255, 0, 0), (obstacle_pos3[0], obstacle_pos3[1], 40, 40))
    bomb4 = pygame.draw.rect(screen, (255, 0, 0), (obstacle_pos4[0], obstacle_pos4[1], 40, 40))
    bomb5 = pygame.draw.rect(screen, (255, 0, 0), (obstacle_pos5[0], obstacle_pos5[1], 40, 40))

    if cobra.colliderect(fruit):
        after_collision()

    if cobra.colliderect(bomb1) or cobra.colliderect(bomb2) or cobra.colliderect(bomb3) or \
            cobra.colliderect(bomb4) or cobra.colliderect(bomb5):
        died = True
        while died:
            game_over_screen()

    # Checking if there was a collision with herself ---------------------------------------------------------------- #
    if snake.count(snake_head_pos) > 1:
        died = True
        while died:
            game_over_screen()

    # Checking if the snake has reached the limits of the screen ---------------------------------------------------- #
    if snake[0][0] > 800:
        snake[0] = (0, snake[0][1])
    if snake[0][0] < 0:
        snake[0] = (800, snake[0][1])
    if snake[0][1] > 600:
        snake[0] = (snake[0][0], 55)
    if snake[0][1] < 55:
        snake[0] = (snake[0][0], 600)

    for i in range(len(snake) - 1, 0, -1):  # shakes the rest of snakes´s body
        snake[i] = (snake[i - 1][0], snake[i - 1][1])

    # Update score hud --------------------------------------------------------------------------------- #
    snake_head_pos = (snake[0][0] - 20, snake[0][1])
    score_text = score_font.render(str(score), True, COLOR_WHITE, COLOR_BLACK)
    screen.fill((0, 0, 0))  # cleaning the screen

    # Sprites ------------------------------------------------------------------------------------------ #

    if my_direction == UP:
        snake_head_pos = (snake[0][0], snake[0][1] - 20)
        screen.blit(snake_head_up, snake_head_pos)
        if collision(snake_head_pos, apple_food_pos):  # two tuples (first matrices´s line and apple food tuple)
            after_collision()

    if my_direction == DOWN:
        snake_head_pos = (snake[0][0], snake[0][1] + 20)
        screen.blit(snake_head_down, snake_head_pos)
        if collision(snake_head_pos, apple_food_pos):  # two tuples (first matrices´s line and apple food tuple)
            after_collision()  # the snake grows, that´s why we add another tuple on it

    if my_direction == LEFT:
        snake_head_pos = (snake[0][0] - 20, snake[0][1])
        screen.blit(snake_head_left, snake_head_pos)
        if collision(snake_head_pos, apple_food_pos):  # two tuples (first matrices´s line and apple food tuple)
            after_collision()

    if my_direction == RIGHT:
        snake_head_pos = (snake[0][0] + 20, snake[0][1])
        screen.blit(snake_head_right, snake_head_pos)
        if collision(snake_head_pos, apple_food_pos):  # two tuples (first matrices´s line and apple food tuple)
            after_collision()

    screen.blit(grass, ((5, 0), (5, 550)))
    screen.blit(grass, ((5, 20), (5, 550)))
    screen.blit(grass, ((770, 20), (550, 50)))
    screen.blit(grass, ((770, 0), (550, 50)))

    pygame.draw.line(screen, COLOR_WHITE, [5, 50], [800, 50], 1)

    if score > 2:
        obstacle_pos2 = missiles_pos(obstacle_pos2)
        screen.blit(obstacle2, obstacle_pos2)

    if score > 6:
        obstacle_pos3 = missiles_pos(obstacle_pos3)
        screen.blit(obstacle3, obstacle_pos3)

    if score > 12:
        obstacle_pos3 = missiles_pos(obstacle_pos3)
        screen.blit(obstacle3, obstacle_pos3)

    if score > 18:
        obstacle_pos3 = missiles_pos(obstacle_pos3)
        screen.blit(obstacle3, obstacle_pos3)

    if score > 24:
        obstacle_pos3 = missiles_pos(obstacle_pos3)
        screen.blit(obstacle3, obstacle_pos3)

    screen.blit(metal_copy, (600, 50))
    screen.blit(metal, (0, 50))
    screen.blit(obstacle, obstacle_pos)
    screen.blit(apple_food, apple_food_pos)
    screen.blit(score_text, score_text_rect)
    screen.blit(apple_1_score, ((WIDTH / 2) - 50, apple_1_score_y))

    for pos in snake:
        screen.blit(snake_skin, pos)

    pygame.display.update()
