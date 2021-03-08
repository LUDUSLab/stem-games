from random import randint
from config import *
import fruit
import snake
from wall import *

player_record = 0

create_wall_img()


# Main game loop
def game_loop():
    global player_record
    set_obj_coordinates(snake.snake, (window[0] - snake.snake.w) // 2, (window[1] - snake.snake.h) // 2 - 28)
    game_close, game_over = False, False
    pygame.mixer.music.play(-1)
    snake_pos = [(window[0] // 2, window[1] // 2)]
    snake_len = 1
    snake.x_move = 0
    snake.y_move = 0
    random_ind1 = randint(0, 3)
    random_ind2 = randint(0, 3)
    frame_aux = 0
    for n in range(4):
        aux1 = []
        for m in range(3):
            aux1.append(img("snake_" + snake.snake_colors[n] + str(m + 1)))
        snake.snake_imgs[n] = aux1
    fruit.random_fruit(snake_pos)
    blink_surface = next(blink_surfaces)
    random_block(snake_pos)
    # The game is not closed, so we either play again or leave the game
    while not game_close:
        while game_over:  # When the snake collides with herself or with the wall, the game is over
            screen.fill(COLOR_LIGHT_BLUE)
            if snake_len - 1 > player_record:
                player_record = snake_len - 1
            msg(continue_msg, "Your record: {}".format(player_record),
                (window[0] // 2 - continue_msg.size("Your record: *")[0] / 2, snake.snake.w))
            msg(game_over_font, "Game Over",
                (window[0] // 2 - game_over_font.size("Game Over")[0] / 2, window[1] // 2 - window[1] // 4))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        quit()
                    if event.key == pygame.K_e:
                        game_loop()
                if event.type == BLINK_EVENT:
                    blink_surface = next(blink_surfaces)

            # Displays blink message on the screen
            screen.blit(blink_surface, blink_rect)
            pygame.display.flip()
            if blink_surface == on_text_surface:
                pygame.time.wait(300)
            game_clock.tick(60)
        game_clock.tick(10)
        screen.fill(COLOR_LIGHT_BLUE)
        draw_blue_square()
        draw_wall()
        screen.blit(stone_block_img, general_block)
        screen.blit(fruit.fruits_imgs[random_ind2][frame_aux], fruit.general_fruit)
        # Displays score on the game screen
        msg(continue_msg, "Score: {}".format(snake_len - 1),
            (window[0] // 2 - continue_msg.size("Score: *")[0] / 2, snake.snake.w))
        # Auxiliary variables
        frame_aux += 1
        if frame_aux > 2:
            frame_aux = 0
        fruit_eaten = (snake.snake.x == fruit.general_fruit.x and snake.snake.y == fruit.general_fruit.y)
        # Listen to players key and rotate the snake image to the respective direction
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_close = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a and snake.x_move <= 0:
                    if snake.y_move <= 0 and snake.x_move == 0:
                        snake.rotate_imgs(90, random_ind1)
                    elif snake.y_move > 0:
                        snake.rotate_imgs(-90, random_ind1)
                    snake.x_move = -snake.snake.w
                    snake.y_move = 0
                elif event.key == pygame.K_d and snake.x_move >= 0:
                    if snake.y_move <= 0 and snake.x_move == 0:
                        snake.rotate_imgs(-90, random_ind1)
                    elif snake.y_move > 0:
                        snake.rotate_imgs(90, random_ind1)
                    snake.x_move = snake.snake.w
                    snake.y_move = 0
                elif event.key == pygame.K_w and snake.y_move <= 0:
                    if snake.x_move > 0 and snake.y_move == 0:
                        snake.rotate_imgs(90, random_ind1)
                    elif snake.x_move < 0:
                        snake.rotate_imgs(-90, random_ind1)
                    snake.y_move = -snake.snake.h
                    snake.x_move = 0
                elif event.key == pygame.K_s and snake.y_move >= 0:
                    if snake.x_move > 0 and snake.y_move == 0:
                        snake.rotate_imgs(-90, random_ind1)
                    elif snake.x_move < 0:
                        snake.rotate_imgs(90, random_ind1)
                    elif snake.x_move == 0 and snake.y_move == 0:
                        snake.rotate_imgs(180, random_ind1)
                    snake.y_move = snake.snake.h
                    snake.x_move = 0
        # Snake moves
        snake.snake.x += snake.x_move
        snake.snake.y += snake.y_move
        snake_head = (snake.snake.x, snake.snake.y)
        snake_pos.insert(0, snake_head)
        # Snake body "moves"
        if len(snake_pos) > snake_len:
            del snake_pos[len(snake_pos) - 1]

        # The snake collides with the wall
        if snake.snake.y < 84 or snake.snake.y > window[1] - 25 or snake.snake.x < snake.snake.w or \
                snake.snake.x > window[0] - 2*snake.snake.w:
            game_over = game_over_treatment()
        # The snake collides with herself
        for x in snake_pos[1:]:
            if x == snake_head:
                game_over = game_over_treatment()

        # Draw snake
        for pos in snake_pos:
            if pos == snake_pos[0]:
                screen.blit(snake.snake_imgs[random_ind1][0], (pos[0], pos[1]))
            elif pos == snake_pos[len(snake_pos) - 1]:
                screen.blit(snake.snake_imgs[random_ind1][2], (pos[0], pos[1]))
            else:
                screen.blit(snake.snake_imgs[random_ind1][1], (pos[0], pos[1]))

        # Fruit eaten
        if fruit_eaten:
            random_ind1 = random_ind2
            apple_sound.play()
            snake_len += 1
            fruit.random_fruit(snake_pos)
            random_block(snake_pos)
            # Reset snake image
            for m in range(3):
                snake.snake_imgs[random_ind1][m] = img("snake_" + snake.snake_colors[random_ind1] + str(m + 1))
            random_ind2 = randint(0, 3)
            if snake.x_move < 0:
                snake.rotate_imgs(90, random_ind1)
            if snake.x_move > 0:
                snake.rotate_imgs(-90, random_ind1)
            if snake.y_move > 0:
                snake.rotate_imgs(180, random_ind1)
            if snake.y_move < 0:
                pass
        pygame.display.flip()
    pygame.quit()
    quit()
