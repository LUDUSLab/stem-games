from snake import *
from fruit import *
from config import *
from wall import *

playing_sound = 0
player_score = 0

# sounds
game_over_sound = pygame.mixer.Sound('../snake/assets/game-over-sound.wav')
victory_sound = pygame.mixer.Sound('../snake/assets/victory-sound.wav')
eating_fruit_sound = pygame.mixer.Sound('../snake/assets/eating-apple-sound.wav')


# when the player loss the game
def game_over():
    global playing_sound
    screen.fill(color_black)
    screen.blit(defeat_text, defeat_text_rect)
    if playing_sound == 0:
        game_over_sound.play()
        playing_sound += 1
    pygame.display.update()


# when the player wins the game
def victory():
    global player_score, playing_sound
    screen.fill(color_black)
    screen.blit(victory_text, victory_text_rect)
    if playing_sound == 0:
        victory_sound.play()
        playing_sound += 1


def game_loop():
    global direction, playing_sound, player_score, apple_pos, grape_pos, strawberry_pos, eating_fruit_sound, snake_head_pos
    game_on = True
    game_clock = pygame.time.Clock()
    while game_on:
        game_clock.tick(10)
        snake_head_pos = (snake[0][0] + 32, snake[0][1])
        snake_head_pos = snake[0]
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
            grape_pos = ((random.randint(32, 726) // 32 * 32), (random.randint(64, 576) // 32 * 32))
        if snake_head_pos == grape_pos:
            grape_pos = grape_randomness_movement()
            eating_fruit_sound.play()
            snake.append((800, 600))
            player_score += 3

        if random.randrange(250) == 1:
            strawberry_pos = ((random.randint(32, 726) // 32 * 32), (random.randint(64, 576) // 32 * 32))
        if snake_head_pos == strawberry_pos:
            strawberry_pos = strawberry_randomness_movement()
            eating_fruit_sound.play()
            snake.append((800, 600))
            player_score += 2

        # updating score
        score_text = score_font.render('SCORE:' + str(player_score), True, color_white, color_black)
        snake_head_pos = (snake[0][1] - 32, snake[0][1])

        for i in range(len(snake) - 1, 0, -1):
            snake[i] = (snake[i - 1][0], snake[i - 1][1])
        # defeat condition
        if (snake[0][0] <= 0) or (snake[0][1] <= 32) or (snake[0][0] >= 768) or (snake[0][1] >= 576) \
                or snake[0] in [(192, 32), (192, 64), (608, 32), (608, 64), (32, 160), (64, 160), (416, 160),
                                (416, 192), (416, 224), (480, 320), (480, 352), (480, 384), (736, 416), (704, 416),
                                (672, 416), (32, 384), (64, 384), (224, 544), (224, 512), (224, 480)]:
            game_over()
        # victory condition
        elif player_score == 20:
            victory()

        else:
            body_snake_move()

            # drawing wall and obstacles
            wall_pos()
            wall_obstacles()

            # updating screen
            screen.blit(score_text, score_text_rect)
            screen.blit(apple, apple_pos)
            screen.blit(grape, grape_pos)
            screen.blit(strawberry, strawberry_pos)

            for pos in snake:
                screen.blit(snake_body, pos)

        pygame.display.update()
        screen.fill(color_black)
    pygame.quit()
