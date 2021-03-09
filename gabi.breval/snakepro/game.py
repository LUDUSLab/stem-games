from random import randint
from config import *
import fruit
from snake import *
from wall import *
from obstacles import *

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

    if my_direction == UP:  # shakes the snake´s head
        snake[0] = (snake[0][0], snake[0][1] - 10)

    if my_direction == DOWN:  # shakes the snake´s head
        snake[0] = (snake[0][0], snake[0][1] + 10)

    if my_direction == RIGHT:  # shakes the snake´s head
        snake[0] = (snake[0][0] + 10, snake[0][1])

    if my_direction == LEFT:  # shakes the snake´s head
        snake[0] = (snake[0][0] - 10, snake[0][1])
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
        apple_food_pos = on_grid_random()  # when there´s a collision the apple changes its position
        munch_sound_effect.play()  # sound
        score += 1
        snake.append((0, 0))

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
                        snake.clear()  # cleaning the list
                        snake = [(200, 200), (220, 200), (240, 200)]  # drawing it again
                        my_direction = LEFT
                        snake_head_pos = (snake[0][0] - 20, snake[0][1])
                        apple_food_pos = on_grid_random()
                        obstacle_pos = (750, 300)
                        obstacle_pos2 = (750, 150)  # where does it start
                        obstacle_pos3 = (750, 200)  # where does it start
                        obstacle_pos4 = (750, 340)  # where does it start
                        obstacle_pos5 = (750, 100)  # where does it start
                        died = False
                if event_over.type == BLINK_EVENT:
                    blink_surface = next(blink_surfaces)

            if score > SCORE_MAX:
                SCORE_MAX = score
            highest_score = SCORE_MAX
            highest_score_txt = score_font.render('HIGHEST SCORE : ' + str(highest_score), True, COLOR_WHITE,
                                                  COLOR_BLACK)
            screen.blit(highest_score_txt, highest_score_txt_rect)
            screen.blit(blink_surface, blink_rect)
            screen.blit(score_text, (WIDTH / 2, 330))
            screen.blit(apple_1_score, ((WIDTH / 2) - 50, 330))
            clock.tick(50)
            pygame.display.update()

    # Checking if there was a collision with herself ---------------------------------------------------------------- #
    if snake.count(snake_head_pos) > 1:
        died = True
        while died:
            screen.fill((0, 0, 0))
            for event_over in pygame.event.get():  # identifies what was clicked
                if event_over.type == QUIT:
                    pygame.quit()
                if event_over.type == KEYDOWN:
                    if event_over.key == K_r:
                        score = 0
                        snake.clear()  # cleaning the list
                        snake = [(200, 200), (220, 200), (240, 200)]  # drawing it again
                        my_direction = LEFT
                        snake_head_pos = (snake[0][0] - 20, snake[0][1])
                        apple_food_pos = on_grid_random()
                        obstacle_pos = (750, 300)
                        obstacle_pos2 = (750, 150)  # where does it start
                        obstacle_pos3 = (750, 200)  # where does it start
                        obstacle_pos4 = (750, 340)  # where does it start
                        obstacle_pos5 = (750, 100)  # where does it start
                        died = False
                if event_over.type == BLINK_EVENT:
                    blink_surface = next(blink_surfaces)
            if score > SCORE_MAX:
                SCORE_MAX = score
            highest_score = SCORE_MAX
            highest_score_txt = score_font.render('HIGHEST SCORE : ' + str(highest_score), True, COLOR_WHITE,
                                                  COLOR_BLACK)
            screen.blit(highest_score_txt, highest_score_txt_rect)
            screen.blit(blink_surface, blink_rect)
            screen.blit(score_text, (WIDTH / 2, 330))
            screen.blit(apple_1_score, ((WIDTH / 2) - 50, 330))
            clock.tick(50)
            pygame.display.update()

    # Checking if the snake has reached the limits of the screen ---------------------------------------------------- #
    if snake[0][0] > 750:
        snake[0] = (50, snake[0][1])
    if snake[0][0] < 50:
        snake[0] = (750, snake[0][1])
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
            apple_food_pos = on_grid_random()  # when there´s a collision the apple changes its position
            munch_sound_effect.play()  # sound
            score += 1
            snake.append((0, 0))

    if my_direction == DOWN:
        snake_head_pos = (snake[0][0], snake[0][1] + 20)
        screen.blit(snake_head_down, snake_head_pos)
        if collision(snake_head_pos, apple_food_pos):  # two tuples (first matrices´s line and apple food tuple)
            apple_food_pos = on_grid_random()  # when there´s a collision the apple changes its position
            munch_sound_effect.play()  # sound
            score += 1
            snake.append((0, 0))

    if my_direction == LEFT:
        snake_head_pos = (snake[0][0] - 20, snake[0][1])
        screen.blit(snake_head_left, snake_head_pos)
        if collision(snake_head_pos, apple_food_pos):  # two tuples (first matrices´s line and apple food tuple)
            apple_food_pos = on_grid_random()  # when there´s a collision the apple changes its position
            munch_sound_effect.play()  # sound
            score += 1
            snake.append((0, 0))

    if my_direction == RIGHT:
        snake_head_pos = (snake[0][0] + 20, snake[0][1])
        screen.blit(snake_head_right, snake_head_pos)
        if collision(snake_head_pos, apple_food_pos):  # two tuples (first matrices´s line and apple food tuple)
            apple_food_pos = on_grid_random()  # when there´s a collision the apple changes its position
            munch_sound_effect.play()  # sound
            score += 1
            snake.append((0, 0))

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
