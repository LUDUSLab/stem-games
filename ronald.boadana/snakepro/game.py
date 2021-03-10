from snake import *
from fruit import *
from config import *

playing_sound = 0
player_score = 10

# sounds
game_over_sound = pygame.mixer.Sound('../snake/assets/game-over-sound.wav')
victory_sound = pygame.mixer.Sound('../snake/assets/victory-sound.wav')
eating_fruit_sound = pygame.mixer.Sound('../snake/assets/eating-apple-sound.wav')


def game_over():
    global playing_sound
    screen.fill(color_black)
    screen.blit(defeat_text, defeat_text_rect)
    if playing_sound == 0:
        game_over_sound.play()
        playing_sound += 1


def victory():
    global player_score, playing_sound
    screen.fill(color_black)
    screen.blit(victory_text, victory_text_rect)
    if playing_sound == 0:
        victory_sound.play()
        playing_sound += 1


# looping to make the key pressed move the snake
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3
direction = LEFT


def game_loop():
    global direction, playing_sound, player_score, apple_pos, grape_pos, strawberry_pos, eating_fruit_sound
    game_on = True
    game_clock = pygame.time.Clock()
    while game_on:
        game_clock.tick(8)
        snake_head_pos = (snake[0][0] + 20, snake[0][1])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_on = False
            # mapping keys
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    direction = UP
                if event.key == pygame.K_s:
                    direction = DOWN
                if event.key == pygame.K_a:
                    direction = LEFT
                if event.key == pygame.K_d:
                    direction = RIGHT
        if direction == UP:
            snake[0] = (snake[0][0], snake[0][1] - 32)
        if direction == DOWN:
            snake[0] = (snake[0][0], snake[0][1] + 32)
        if direction == RIGHT:
            snake[0] = (snake[0][0] + 32, snake[0][1])
        if direction == LEFT:
            snake[0] = (snake[0][0] - 32, snake[0][1])

        # checking the score
        if snake_head_pos == apple_pos:
            apple_pos = apple_randomness_movement()
            eating_fruit_sound.play()
            snake.append((800, 600))
            player_score += 1

        if random.randrange(500) == 1:
            grape_pos = ((random.randint(60, 560) // 10 * 10), (random.randint(60, 560) // 10 * 10))
            if snake_head_pos == grape_pos:
                grape_pos = grape_randomness_movement()
                eating_fruit_sound.play()
                snake.append((800, 600))
                player_score += 3

        if random.randrange(100) == 1:
            strawberry_pos = ((random.randint(60, 560) // 10 * 10), (random.randint(60, 560) // 10 * 10))
            if snake_head_pos == strawberry_pos:
                strawberry_pos = strawberry_randomness_movement()
                eating_fruit_sound.play()
                snake.append((800, 600))
                player_score += 2
        print(snake_head_pos)

        # updating score
        score_text = score_font.render('SCORE:' + str(player_score), True, color_white, color_black)
        snake_head_pos = (snake[0][1] - 20, snake[0][1])

        for i in range(len(snake) - 1, 0, -1):
            snake[i] = (snake[i - 1][0], snake[i - 1][1])
        # defeat condition
        if (snake[0][0] < 0) or (snake[0][1] < 40) or (snake[0][0] > 770) or (snake[0][1] > 770):
            game_over()
        # victory condition
        elif player_score == 10:
            victory()

        else:
            body_snake_move()

            # updating screen
            screen.blit(score_text, score_text_rect)
            screen.blit(apple, apple_pos)
            screen.blit(grape, grape_pos)
            screen.blit(strawberry, strawberry_pos)

            for pos in snake:
                screen.blit(snake_body, pos)
            screen.blit(snake_head, snake_head_pos)

            # drawing the wall

        pygame.display.update()
        screen.fill(color_black)
    pygame.quit()
