from random import randint
import config
import fruit
import snake
import pygame
import wall

player_record = 0


# Main game loop
def game_loop():
    global player_record
    config.game_close, config.game_over = False, False
    config.pygame.mixer.music.play(-1)
    random_ind1 = randint(0, 3)
    random_ind2 = randint(0, 3)
    frame_aux = 0
    snake.reset_snake()
    fruit.random_fruit()
    blink_surface = next(config.blink_surfaces)
    wall.blocks.clear()
    wall.blocks.append(wall.stone_block_img.get_rect())
    wall.random_block(snake.snake_len - 1)

    # The game is not closed, so we either play again or leave the game
    while not config.game_close:
        # When the snake collides with herself or with the wall, the game is over
        while config.game_over:
            config.screen.fill(config.COLOR_BROWN)
            if snake.snake_len - 1 > player_record:
                player_record = snake.snake_len - 1
            config.msg(config.continue_msg, "Your record: {}".format(player_record),
                       (config.window[0] // 2 - config.continue_msg.size("Your record: *")[0] / 2, config.BLOCK_SIZE))
            config.msg(config.game_over_font, "Game Over",
                       (config.window[0] // 2 - config.game_over_font.size("Game Over")[0] / 2,
                        config.window[1] // 2 - config.window[1] // 4))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        quit()
                    if event.key == pygame.K_e:
                        game_loop()
                if event.type == config.BLINK_EVENT:
                    blink_surface = next(config.blink_surfaces)

            # Displays blink message on the screen
            config.screen.blit(blink_surface, config.blink_rect)
            pygame.display.flip()
            if blink_surface == config.on_text_surface:
                pygame.time.wait(300)
            config.game_clock.tick(60)
        config.game_clock.tick(10)
        pygame.time.delay(85)
        config.screen.fill(config.COLOR_BROWN)
        config.draw_sky()
        config.draw_dark_brown_square()
        config.draw_ground_block()
        wall.draw_wall()
        for block in wall.blocks:
            config.screen.blit(wall.stone_block_img, block)
        config.screen.blit(fruit.fruits_imgs[random_ind2][frame_aux], fruit.general_fruit)

        # Displays score on the game screen
        config.msg(config.continue_msg, "Score: {}".format(snake.snake_len - 1),
                   (config.window[0] // 2 - config.continue_msg.size("Score: *")[0] / 2, config.BLOCK_SIZE))

        # Auxiliary variables
        frame_aux += 1
        if frame_aux > 2:
            frame_aux = 0
        fruit_eaten = (snake.snake.x == fruit.general_fruit.x and snake.snake.y == fruit.general_fruit.y)

        # Listen to players key and rotate the snake image to the respective direction
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                config.game_close = True
            snake.check_snake_moves(event, random_ind1)

        # Fruit eaten
        if fruit_eaten:
            random_ind1 = random_ind2
            config.apple_sound.play()
            snake.snake_len += 1
            fruit.random_fruit()
            wall.random_block(snake.snake_len - 1)
            # Reset snake image
            for m in range(3):
                snake.snake_imgs[random_ind1][m] = config.img("snake_" + snake.snake_colors[random_ind1] + str(m + 1))
            random_ind2 = randint(0, 3)
            snake.snake_colors_reset(random_ind1)

        # Snake moves
        snake.snake_moves()
        snake.draw_snake(random_ind1)

        # The snake collides with the wall / obstacle
        snake.check_snake_collide_herself()
        snake.snake_wall_collide()
        wall.snake_obstacle_collide()

        pygame.display.flip()

    pygame.quit()
    quit()
