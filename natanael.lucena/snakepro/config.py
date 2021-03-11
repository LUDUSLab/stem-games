import pygame
from itertools import cycle

pygame.init()

# Colors
COLOR_LIGHT_GREY = (230, 230, 230)
COLOR_BROWN = (119, 84, 64)
COLOR_DARK_BROWN = (106, 74, 54)
COLOR_LIGHT_BLUE = (95, 156, 238)
# Window
window = (800, 600)
screen = pygame.display.set_mode(window)
pygame.display.set_caption("PySnake")
game_clock = pygame.time.Clock()  # Clock object

# Block size constant
BLOCK_SIZE = 32

# Game loop variables
game_close, game_over = False, False


# Fonts
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


# Display message on screen
def msg(fnt, message, pos):
    txt = fnt.render(message, True, COLOR_LIGHT_GREY)
    screen.blit(txt, pos)


# Does what needs to be done when game is over
def game_over_treatment():
    global game_over
    wall_hit.play()
    game_over_sound.play()
    pygame.mixer.music.stop()
    game_over = True


# Draw a blue rect above the ground
def draw_sky():
    pygame.draw.rect(screen, COLOR_LIGHT_BLUE, (0, 0, window[0], 12))


# Draw many 32x32 dark brown squares for the snake's arena background
def draw_dark_brown_square():
    for i in range(BLOCK_SIZE, window[1] - BLOCK_SIZE * 3 + 24, BLOCK_SIZE):
        if (i // BLOCK_SIZE) % 2:
            aux = BLOCK_SIZE
        else:
            aux = 0
        for j in range(aux + BLOCK_SIZE * 3, window[0] - BLOCK_SIZE * 3, 2*BLOCK_SIZE):
            pygame.draw.rect(screen, COLOR_DARK_BROWN, (j, 3*BLOCK_SIZE + i, BLOCK_SIZE, BLOCK_SIZE))


# Ground sprite
general_ground_block = img("ground1").get_rect()
ground_block_imgs = [img("ground" + str(x+1)) for x in range(3)]


# Draw the ground background
def draw_ground_block():
    general_ground_block.y = BLOCK_SIZE * 2 + 24
    while general_ground_block.y <= window[1]:
        for i in range(0, BLOCK_SIZE * 2 + 1, BLOCK_SIZE):
            general_ground_block.x = i
            screen.blit(ground_block_imgs[(general_ground_block.y//BLOCK_SIZE) % 2], general_ground_block)
        for i in range(window[0] - 3 * BLOCK_SIZE, window[0] - BLOCK_SIZE + 1, BLOCK_SIZE):
            general_ground_block.x = i
            screen.blit(ground_block_imgs[(general_ground_block.y//BLOCK_SIZE) % 2], general_ground_block)
        general_ground_block.y += BLOCK_SIZE
    general_ground_block.x = 0
    while general_ground_block.x <= window[0] - BLOCK_SIZE:
        aux = 2
        for i in range(3):
            general_ground_block.y = 8 + i*BLOCK_SIZE
            screen.blit(ground_block_imgs[aux], general_ground_block)
            if i == 0:
                aux = (general_ground_block.y//BLOCK_SIZE) % 2
        general_ground_block.x += BLOCK_SIZE


# Sounds
apple_sound = pygame.mixer.Sound('./assets/natanael.lucena.apple_crunch.wav')
wall_hit = pygame.mixer.Sound('./assets/natanael.lucena.wall_hit.wav')
game_over_sound = pygame.mixer.Sound('./assets/natanael.lucena.game_over.wav')
pygame.mixer.music.load('./assets/natanael.lucena.background_music.wav')

# Fonts
game_over_font = font(64)
continue_msg = font(25)

# Blink text effect variables
BLINK_EVENT = pygame.USEREVENT + 0
on_text_surface = continue_msg.render("Q-Quit/E-Play again", True, COLOR_LIGHT_GREY)
blink_rect = on_text_surface.get_rect()
blink_rect.center = screen.get_rect().center
off_text_surface = pygame.Surface(blink_rect.size)
off_text_surface.fill(COLOR_BROWN)
blink_surfaces = cycle([on_text_surface, off_text_surface])
pygame.time.set_timer(BLINK_EVENT, 580)
