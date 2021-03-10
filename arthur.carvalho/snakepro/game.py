from config import *
from fruit import *
from snakebody import *
from wall import *


def scoring():
    global score

    score_text = score_font.render(f'Score: {score}', True, color_white, color_black)
    screen.blit(score_text, (0, 0))


def game_over():
    global play_sound
    score_text = score_font.render(f'Score: {score}', True, color_white, color_black)

    screen.fill(color_73ED73)

    screen.blit(game_over_text, (130, 200))
    screen.blit(score_text, (300, 300))

    if play_sound == 0:
        game_over_sound.play()

        play_sound += 1

    pygame.display.update()


def main_loop():
    global snake_direction

    while game_loop:
        game_clock.tick(15)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:

                if snake_direction != RIGHT:
                    if event.key == pygame.K_LEFT:
                        snake_direction = LEFT

                if snake_direction != DOWN:
                    if event.key == pygame.K_UP:
                        snake_direction = UP

                if snake_direction != LEFT:
                    if event.key == pygame.K_RIGHT:
                        snake_direction = RIGHT

                if snake_direction != UP:
                    if event.key == pygame.K_DOWN:
                        snake_direction = DOWN

        if snake_position[0][0] < 32 or snake_position[0][1] < 64 or snake_position[0][0] > 768 or \
                snake_position[0][1] > 608:
            game_over()

        else:
            snake_move(snake_direction)

            screen.fill(color_73ED73)

            wall_draw()
            snake_draw()
            fruit_draw()

            scoring()

            pygame.display.update()


# score
score_font = pygame.font.Font('assets/PressStart2P.ttf', 20)
score = 0

# game over
game_ove_font = pygame.font.Font('assets/PressStart2P.ttf', 60)
game_over_text = game_ove_font.render('Game Over', True, color_white, color_black)
play_sound = 0

snake_direction = 0
