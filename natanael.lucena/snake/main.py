import pygame

pygame.init()

# Window
window = (1280, 720)
center = (window[0]//2, window[1]//2)
screen = pygame.display.set_mode(window)
pygame.display.set_caption("Snake")

# Colors
COLOR_LIGHT_GREY = (200, 200, 200)
COLOR_DARK_GREY = pygame.Color('gray12')

# Game loop
game_loop = True
game_clock = pygame.time.Clock()


# Create font
def font(fontsize):
    font_path = "./assets/PressStart2P.ttf"
    return pygame.font.Font(font_path, fontsize)


# Create image
def img(name):
    img_path = "./assets/natanael.lucena_" + name + ".png"
    return pygame.image.load(img_path).convert_alpha()


# Set object coordinates
def set_obj_coordinates(obj, x, y):
    obj.x = x
    obj.y = y


# Check player key press
def check_player_key(b):
    global snake_direction
    if event.key == pygame.K_w or event.key == pygame.K_s or event.key == pygame.K_a or event.key == pygame.K_d:
        snake_direction[event.key] = b


# Check key events in-game
def event_conditional():
    global game_loop
    if event.type == pygame.QUIT:
        game_loop = False
    elif event.type == pygame.KEYDOWN:
        check_player_key(True)
    elif event.type == pygame.KEYUP:
        check_player_key(False)


score_font = font(36)


# Render score text
# def text_render(a_score_text):
#    return score_font.render(f"{a_score_text}", True, COLOR_LIGHT_GREY)


# Check if the snake collided and the game is over
def game_over():
    if snake.y < 0 or snake.y > 720 or snake.x < 0 or snake. x > 1280:
        return True


# Snake
snake_img = img("snake")
snake = snake_img.get_rect()
move_keys = [pygame.K_w, pygame.K_d, pygame.K_s, pygame.K_a]
snake_direction = {k: False for k in move_keys}
snake_score = 0
snake_vel = 10
set_obj_coordinates(snake, center[0], center[1])


# Apple
apple_img = img("apple")
apple = apple_img.get_rect()
apple_eaten = False
set_obj_coordinates(apple, 40, 40)


# Main game loop
while game_loop:
    for event in pygame.event.get():
        event_conditional()
    # score_text = text_render(snake_score)
    if not game_over():
        for i in range(4):
            if snake_direction[move_keys[i]]:
                sign = 1 if i % 3 else -1
                if i % 2:
                    snake.x += sign * snake_vel
                else:
                    snake.y += sign * snake_vel
        # if snake_direction[move_keys[0]]:
        #    snake.y -= snake_vel
        # if snake_direction[move_keys[1]]:
        #    snake.x += snake_vel
        # if snake_direction[move_keys[2]]:
        #    snake.y += snake_vel
        # if snake_direction[move_keys[3]]:
        #    snake.x -= snake_vel
        screen.fill(COLOR_DARK_GREY)
        screen.blit(snake_img, snake)
        screen.blit(apple_img, apple)
    # game over code here

    # Update screen
    pygame.display.flip()
    game_clock.tick(60)

pygame.quit()
