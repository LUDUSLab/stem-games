import pygame
import random
import sys
#import time

pygame.init()

#colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 128, 0)
grey = (192, 192, 192)

#display
n_lines = 20
size = 500
cube_size = size // n_lines
size = 500
screen = pygame.display.set_mode((size, size))
pygame.display.set_caption('Snake')

#snake
pos_x = 5 * cube_size
pos_y = 10 * cube_size
snake = [(pos_x, pos_y), (pos_x, pos_y)]
snake_body = pygame.Surface((cube_size-1, cube_size-1))
snake_body.fill(green)

#snake eyes
eye_1 = pygame.Surface((5, 10))
eye_2 = pygame.Surface((5, 10))
eye_1.fill(black)
eye_2.fill(black)
#apple
#apple = pygame.Surface((cube_size-2, cube_size-2))
#apple.fill(red)
apple = pygame.image.load('assets/allef.ramos_apple.png')

game_loop = True
game_over_msg = False
game_clock = pygame.time.Clock()

#initial movement
direction_x = 0
direction_y = 1

score = 0
high_score = 0

score_font = pygame.font.Font('assets/PressStart2P.ttf', 17)
score_text = score_font.render('Score: %d' % score, True, white, black)
font = pygame.font.Font('assets/PressStart2P.ttf', 44)
msg = font.render('GAME OVER', True, white)
r_1 = score_font.render('Press "ENTER"', True, white)
r_2 = score_font.render('to Restart', True, white)
high = score_font.render('High Score: %d' % high_score, True, white)


def random_pos():
    aux = True
    x = 0
    y = 0
    while aux:
        x, y = random.randrange(0, 500, cube_size), random.randrange(0, 500, cube_size)
        if (x, y) not in snake:
            break
    return x // cube_size * cube_size, y // cube_size * cube_size


apple_cord = random_pos()


def draw_lines():
    screen.fill(black)
    l_x = 0
    l_y = 0
    #draw edge
    pygame.draw.line(screen, white, (0, size-1), (size-1, size-1))
    pygame.draw.line(screen, white, (0, 0), (0, size-1))
    pygame.draw.line(screen, white, (size-1, 0), (size-1, size-1))

    for i in range(0, n_lines):
        l_x += cube_size
        l_y += cube_size
        pygame.draw.line(screen, grey, (l_x, 0), (l_x, size))
        pygame.draw.line(screen, grey, (0, l_y), (size, l_y))


def draw_snake():

    for pos in snake:
        screen.blit(snake_body, pos)
    screen.blit(eye_1, (pos_x+5, pos_y+7))
    screen.blit(eye_2, (pos_x+15, pos_y+7))
    for j in range(len(snake) - 1, 0, -1):
        snake[j] = (snake[j][0], snake[j][1])


def move():
    global pos_x, pos_y

    if pos_x >= 498:
        pos_x = -cube_size
    elif pos_x < 0:
        pos_x = 475+cube_size

    if pos_y >= 498:
        pos_y = -cube_size
    elif pos_y < 0:
        pos_y = 475+cube_size

    pos_x += direction_x * cube_size
    pos_y += direction_y * cube_size
    snake[0] = (pos_x, pos_y)
    if direction_x != 0 or direction_y != 0:
        for i in range(len(snake) - 1, 0, -1):
            snake[i] = (snake[i - 1][0], snake[i - 1][1])


def add():
    dx, dy = direction_x, direction_y
    tail = snake[-1]

    if dx == 1 and dy == 0:
        snake.append((tail[0] - 1, tail[1]))
    elif dx == -1 and dy == 0:
        snake.append((tail[0] + 1, tail[1]))
    elif dx == 0 and dy == 1:
        snake.append((tail[0], tail[1] - 1))
    elif dx == 0 and dy == -1:
        snake.append((tail[0], tail[1] + 1))


def restart():
    global snake, score, direction_y, direction_x, pos_y, pos_x, game_loop, apple_cord, game_over_msg, high
    game_loop = True
    game_over_msg = False
    pos_x = 5 * cube_size
    pos_y = 10 * cube_size
    snake = [(pos_x, pos_y), (pos_x, pos_y)]
    high = score_font.render('High Score: %d' % high_score, True, white)
    direction_x = 0
    direction_y = 1
    apple_cord = random_pos()


def game_over():
    global direction_x, direction_y, game_loop, game_over_msg, event, score, high_score, high
    for i in range(2, len(snake)):
        if snake[0] == snake[i]:
            direction_x, direction_y = 0, 0
            pygame.mixer.Sound('assets/allef.ramos_game.over.wav').play()
            game_loop = False
            game_over_msg = True

    while game_over_msg:
        pygame.display.flip()
        if high_score <= score:
            high_score = score
            score = 0

        #High Score
        screen.blit(high, (225, 5))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_loop = False
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    restart()

        screen.blit(msg, (2.5 * cube_size, size / 2 - 100))
        screen.blit(r_1, (125, size / 2 - 40))
        screen.blit(r_2, (150, size / 2 - 10))


while game_loop:
    screen.fill(black)
    draw_lines()
    screen.blit(apple, (apple_cord[0]+1, apple_cord[1]+1))

    #read keyboard
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop = False
            pygame.quit()
            #definality close every code running
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction_y != 1 and pos_y < 500 and pos_x < 500 and pos_y >= 0 and pos_x >= 0:
                direction_x = 0
                direction_y = -1
            elif event.key == pygame.K_DOWN and direction_y != -1 and pos_y < 500 and pos_x < 500 and pos_y >= 0 and pos_x >= 0:
                direction_x = 0
                direction_y = 1
            elif event.key == pygame.K_LEFT and direction_x != 1 and pos_y < 500 and pos_x < 500 and pos_y >= 0 and pos_x >= 0:
                direction_x = -1
                direction_y = 0
            elif event.key == pygame.K_RIGHT and direction_x != -1 and pos_y < 500 and pos_x < 500 and pos_y >= 0 and pos_x >= 0:
                direction_x = 1
                direction_y = 0

    draw_snake()

    move()
    #check game over condition
    screen.blit(score_text, (5, 5))
    score_text = score_font.render('Score: %d' % score, True, white)

    if pos_x == apple_cord[0] and pos_y == apple_cord[1]:
        apple_cord = random_pos()
        add()
        score += 1
        pygame.mixer.Sound('assets/allef.ramos.apple-crunch.wav').play()

    #High Score

    if high_score > 0:
        high = score_font.render('High Score: %d' % high_score, True, white)
        screen.blit(high, (225, 5))

    game_over()

    pygame.display.flip()
    pygame.time.delay(100)
    game_clock.tick(10)
