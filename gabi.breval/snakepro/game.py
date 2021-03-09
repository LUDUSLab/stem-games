from random import randint
import config
import fruit
import pygame
import snake
from pygame.locals import *
import wall
import obstacles

while True:

    config.screen

    snake.snake_head_pos = (snake.snake[0])

    for event in pygame.event.get():  # identifies what was clicked
        if event.type == QUIT:
            pygame.quit()
        if event.type == KEYDOWN:

            if event.key == K_UP:
                if config.my_direction == config.DOWN:
                    pass
                else:
                    config.my_direction = config.UP

            if event.key == K_DOWN:
                if config.my_direction == config.UP:
                    pass
                else:
                    config.my_direction = config.DOWN

            if event.key == K_LEFT:
                if config.my_direction == config.RIGHT:
                    pass
                else:
                    config.my_direction = config.LEFT

            if event.key == K_RIGHT:
                if config.my_direction == config.LEFT:
                    pass
                else:
                    config.my_direction = config.RIGHT

    if config.my_direction == config.UP:  # shakes the snake´s head
        snake.snake[0] = (snake.snake[0][0], snake.snake[0][1] - 10)

    if config.my_direction == config.DOWN:  # shakes the snake´s head
        snake.snake[0] = (snake.snake[0][0], snake.snake[0][1] + 10)

    if config.my_direction == config.RIGHT:  # shakes the snake´s head
        snake.snake[0] = (snake.snake[0][0] + 10, snake.snake[0][1])

    if config.my_direction == config.LEFT:  # shakes the snake´s head
        snake.snake[0] = (snake.snake[0][0] - 10, snake.snake[0][1])
    obstacles.obstacle_pos = config.missiles_pos(obstacles.obstacle_pos)

    # Checking collision -------------------------------------------------------------------------------------------- #
    cobra = pygame.draw.rect(config.screen, (0, 255, 0), (snake.snake[0][0], snake.snake[0][1], 32, 32))
    fruit = pygame.draw.rect(config.screen, (255, 0, 0), (fruit.apple_food_pos[0], fruit.apple_food_pos[1], 32, 32))
    bomb1 = pygame.draw.rect(config.screen, (255, 0, 0), (obstacles.obstacle_pos[0], obstacles.obstacle_pos[1], 40, 40))
    bomb2 = pygame.draw.rect(config.screen, (255, 0, 0), (obstacles.obstacle_pos2[0], obstacles.obstacle_pos2[1], 40, 40))
    bomb3 = pygame.draw.rect(config.screen, (255, 0, 0), (obstacles.obstacle_pos3[0], obstacles.obstacle_pos3[1], 40, 40))
    bomb4 = pygame.draw.rect(config.screen, (255, 0, 0), (obstacles.obstacle_pos4[0], obstacles.obstacle_pos4[1], 40, 40))
    bomb5 = pygame.draw.rect(config.screen, (255, 0, 0), (obstacles.obstacle_pos5[0], obstacles.obstacle_pos5[1], 40, 40))

    if cobra.colliderect(fruit):
        apple_food_pos = on_grid_random()  # when there´s a collision the apple changes its position
        munch_sound_effect.play()  # sound
        config.score += 1
        snake.snake.append((0, 0))

    if cobra.colliderect(bomb1) or cobra.colliderect(bomb2) or cobra.colliderect(bomb3) or \
            cobra.colliderect(bomb4) or cobra.colliderect(bomb5):
        died = True
        while died:
            screen.fill((0, 0, 0))
            for event_over in pygame.event.get():  # identifies what was clicked
                if event_over.type == QUIT:
                    pygame.quit()
                if event_over.type == KEYDOWN:
                    if event_over.key == K_r:
                        score = 0
                        snake.snake.clear()  # cleaning the list
                        snake.snake = [(200, 200), (220, 200), (240, 200)]  # drawing it again
                        my_direction = LEFT
                        snake.snake_head_pos = (snake.snake[0][0] - 20, snake.snake[0][1])
                        apple_food_pos = on_grid_random()
                        obstacle_pos = (750, 300)
                        obstacle_pos2 = (750, 150)  # where does it start
                        obstacle_pos3 = (750, 200)  # where does it start
                        obstacle_pos4 = (750, 340)  # where does it start
                        obstacle_pos5 = (750, 100)  # where does it start
                        died = False
                if event_over.type == BLINK_EVENT:
                    blink_surface = next(blink_surfaces)

            if config.score > config.SCORE_MAX:
                config.SCORE_MAX = config.score
            config.highest_score = config.SCORE_MAX
            config.highest_score_txt = config.score_font.render('HIGHEST SCORE : ' + str(config.highest_score), True,
                                                                COLOR_WHITE,
                                                                COLOR_BLACK)
            config.screen.blit(config.highest_score_txt, config.highest_score_txt_rect)
            config.screen.blit(config.blink_surface, config.blink_rect)
            config.screen.blit(config.score_text, (config.WIDTH / 2, 330))
            config.screen.blit(apple_1_score, ((config.WIDTH / 2) - 50, 330))
            clock.tick(50)
            pygame.display.update()

    # Checking if there was a collision with herself ---------------------------------------------------------------- #
    if snake.snake.count(snake.snake_head_pos) > 1:
        died = True
        while died:
            config.screen.fill((0, 0, 0))
            for event_over in pygame.event.get():  # identifies what was clicked
                if event_over.type == QUIT:
                    pygame.quit()
                if event_over.type == KEYDOWN:
                    if event_over.key == K_r:
                        config.score = 0
                        snake.snake.clear()  # cleaning the list
                        snake = [(200, 200), (220, 200), (240, 200)]  # drawing it again
                        config.my_direction = LEFT
                        snake.snake_head_pos = (snake[0][0] - 20, snake[0][1])
                        apple_food_pos = on_grid_random()
                        obstacle_pos = (750, 300)
                        obstacle_pos2 = (750, 150)  # where does it start
                        obstacle_pos3 = (750, 200)  # where does it start
                        obstacle_pos4 = (750, 340)  # where does it start
                        obstacle_pos5 = (750, 100)  # where does it start
                        died = False
                if event_over.type == BLINK_EVENT:
                    config.blink_surface = next(config.blink_surfaces)
            if config.score > config.SCORE_MAX:
                SCORE_MAX = config.score
            highest_score = config.SCORE_MAX
            highest_score_txt = score_font.render('HIGHEST SCORE : ' + str(highest_score), True, COLOR_WHITE,
                                                  COLOR_BLACK)
            config.screen.blit(config.highest_score_txt, config.highest_score_txt_rect)
            config.screen.blit(config.blink_surface, config.blink_rect)
            config.screen.blit(config.score_text, (config.WIDTH / 2, 330))
            config.screen.blit(apple_1_score, ((config.WIDTH / 2) - 50, 330))
            clock.tick(50)
            pygame.display.update()

    # Checking if the snake has reached the limits of the screen ---------------------------------------------------- #
    if snake.snake[0][0] > 750:
        snake.snake[0] = (50, snake.snake[0][1])
    if snake.snake[0][0] < 50:
        snake.snake[0] = (750, snake.snake[0][1])
    if snake.snake[0][1] > 600:
        snake.snake[0] = (snake.snake[0][0], 55)
    if snake.snake[0][1] < 55:
        snake.snake[0] = (snake.snake[0][0], 600)

    for i in range(len(snake.snake) - 1, 0, -1):  # shakes the rest of snakes´s body
        snake.snake[i] = (snake.snake[i - 1][0], snake.snake[i - 1][1])

    # Update score hud --------------------------------------------------------------------------------- #
    snake.snake_head_pos = (snake.snake[0][0] - 20, snake.snake[0][1])
    config.score_text = config.score_font.render(str(config.score), True, config.COLOR_WHITE, config.COLOR_BLACK)
    config.screen.fill((0, 0, 0))  # cleaning the screen

    # Sprites ------------------------------------------------------------------------------------------ #

    if config.my_direction == config.UP:
        snake.snake_head_pos = (snake.snake[0][0], snake.snake[0][1] - 20)
        screen.blit(snake.snake_head_up, snake.snake_head_pos)
        if collision(snake.snake_head_pos, fruit.apple_food_pos):  # two tuples (first matrices´s line and apple food tuple)
            fruit.apple_food_pos = on_grid_random()  # when there´s a collision the apple changes its position
            config.munch_sound_effect.play()  # sound
            config.score += 1
            snake.snake.append((0, 0))

    if config.my_direction == config.DOWN:
        snake.snake_head_pos = (snake.snake[0][0], snake.snake[0][1] + 20)
        screen.blit(snake.snake_head_down, snake.snake_head_pos)
        if collision(snake.snake_head_pos, fruit.apple_food_pos):  # two tuples (first matrices´s line and apple food tuple)
            fruit.apple_food_pos = on_grid_random()  # when there´s a collision the apple changes its position
            config.munch_sound_effect.play()  # sound
            config.score += 1
            snake.snake.append((0, 0))

    if config.my_direction == config.LEFT:
        snake.snake_head_pos = (snake.snake[0][0] - 20, snake.snake[0][1])
        config.screen.blit(snake.snake_head_left, snake.snake_head_pos)
        if config.collision(snake.snake_head_pos, fruit.apple_food_pos):  # two tuples (first matrices´s line and apple food tuple)
            fruit.apple_food_pos = on_grid_random()  # when there´s a collision the apple changes its position
            config.munch_sound_effect.play()  # sound
            config.score += 1
            snake.snake.append((0, 0))

    if config.my_direction == config.RIGHT:
        snake.snake_head_pos = (snake.snake[0][0] + 20, snake.snake[0][1])
        screen.blit(snake.snake_head_right, snake.snake_head_pos)
        if config.collision(snake.snake_head_pos, fruit.apple_food_pos):  # two tuples (first matrices´s line and apple food tuple)
            fruit.apple_food_pos = on_grid_random()  # when there´s a collision the apple changes its position
            config.munch_sound_effect.play()  # sound
            config.score += 1
            snake.snake.append((0, 0))

    config.screen.blit(grass, ((5, 0), (5, 550)))
    config.screen.blit(grass, ((5, 20), (5, 550)))
    config.screen.blit(grass, ((770, 20), (550, 50)))
    config.screen.blit(grass, ((770, 0), (550, 50)))

    pygame.draw.line(config.screen, config.COLOR_WHITE, [5, 50], [800, 50], 1)

    if config.score > 2:
        obstacles.obstacle_pos2 = missiles_pos(obstacles.obstacle_pos2)
        config.screen.blit(obstacle2, obstacle_pos2)

    if config.score > 6:
        obstacles.obstacle_pos3 = missiles_pos(obstacles.obstacle_pos3)
        config.screen.blit(obstacle3, obstacle_pos3)

    if config.score > 12:
        obstacles.obstacle_pos3 = missiles_pos(obstacles.obstacle_pos3)
        config.screen.blit(obstacle3, obstacle_pos3)

    if config.score > 18:
        obstacles.obstacle_pos3 = missiles_pos(obstacles.obstacle_pos3)
        config.screen.blit(obstacle3, obstacle_pos3)

    if config.score > 24:
        obstacles.obstacle_pos3 = missiles_pos(obstacles.obstacle_pos3)
        config.screen.blit(obstacle3, obstacle_pos3)

    config.screen.blit(wall.metal_copy, (600, 50))
    config.screen.blit(wall.metal, (0, 50))
    config.screen.blit(obstacle, obstacle_pos)
    config.screen.blit(apple_food, fruit.apple_food_pos)
    config.screen.blit(score_text, score_text_rect)
    config.screen.blit(apple_1_score, ((WIDTH / 2) - 50, apple_1_score_y))

    for pos in snake.snake:
        config.screen.blit(snake.snake_skin, pos)

    pygame.display.update()
