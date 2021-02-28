import pygame
from random import randint


def body_snake_move():
    global score, apple_position, score_text

    if UP:
        snake_position[0] = (snake_position[0][0], snake_position[0][1] - 10)

        for c in range(len(snake_position) - 1, 0, -1):
            snake_position[c] = (snake_position[c - 1][0], snake_position[c - 1][1])

    elif DOWN:
        snake_position[0] = (snake_position[0][0], snake_position[0][1] + 10)

        for c in range(len(snake_position) - 1, 0, -1):
            snake_position[c] = (snake_position[c - 1][0], snake_position[c - 1][1])

    elif LEFT:
        snake_position[0] = (snake_position[0][0] - 10, snake_position[0][1])

        for c in range(len(snake_position) - 1, 0, -1):
            snake_position[c] = (snake_position[c - 1][0], snake_position[c - 1][1])

    elif RIGHT:
        snake_position[0] = (snake_position[0][0] + 10, snake_position[0][1])

        for c in range(len(snake_position) - 1, 0, -1):
            snake_position[c] = (snake_position[c - 1][0], snake_position[c - 1][1])

    # coordinate's apple
    if snake_position[0] == apple_position:
        eating_sound.play()
        apple_position = (randint(0, 490) // 10 * 10, randint(0, 490) // 10 * 10)
        snake_position.append((500, 500))
        score += 1
        score_text = score_font.render(f'Score: {score}', True, (255, 255, 255), (0, 0, 0))


pygame.init()

# Screen configuration
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Snake')

# setting snake
snake = pygame.Surface((10, 10))
snake.fill((0, 255, 0))
snake_position = [(100, 250), (90, 250), (80, 250)]
UP = DOWN = LEFT = RIGHT = False

# setting apple
apple = pygame.Surface((10, 10))
apple.fill((255, 0, 0))
apple_position = (400, 250)

# score
score_font = pygame.font.Font('assets/PressStart2P.ttf', 20)
score_text = score_font.render('Score: 0', True, (255, 255, 255), (0, 0, 0))
score = 0

# game over text
game_ove_font = pygame.font.Font('assets/PressStart2P.ttf', 40)
game_ove_text = game_ove_font.render('Game Over', True, (255, 255, 255), (0, 0, 0))

# Sounds
eating_sound = pygame.mixer.Sound('assets/412068__inspectorj__chewing-carrot-a.wav')
game_ove_sound = pygame.mixer.Sound('assets/533034__evretro__8-bit-game-over-sound-tune.wav')
play_sound = 0

game_loop = True
game_clock = pygame.time.Clock()

while game_loop:
    game_clock.tick(20)

    # map events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        # map keys
        elif event.type == pygame.KEYDOWN:
            if not DOWN:
                if event.key == pygame.K_UP:
                    UP = True
                    DOWN = LEFT = RIGHT = False

            if not UP:
                if event.key == pygame.K_DOWN:
                    DOWN = True
                    UP = LEFT = RIGHT = False

            if not RIGHT:
                if event.key == pygame.K_LEFT:
                    LEFT = True
                    UP = DOWN = RIGHT = False

            if not LEFT:
                if event.key == pygame.K_RIGHT:
                    RIGHT = True
                    UP = DOWN = LEFT = False

    if (snake_position[0][0] < 0) or (snake_position[0][1] < 0) or (snake_position[0][0] > 490) or \
            (snake_position[0][1] > 490):
        if play_sound == 0:
            game_ove_sound.play()
            play_sound += 1

        screen.fill((0, 0, 0))

        screen.blit(game_ove_text, (80, 150))
        screen.blit(score_text, (150, 250))

        pygame.display.update()

    else:
        # Snake moves
        body_snake_move()

        # clear e draw
        screen.fill((0, 0, 0))

        screen.blit(score_text, (150, 0))
        screen.blit(apple, apple_position)

        for position in snake_position:
            screen.blit(snake, position)

        pygame.display.update()
