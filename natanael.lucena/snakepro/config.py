import pygame
from itertools import cycle

pygame.init()

# Colors
COLOR_LIGHT_GREY = (230, 230, 230)
COLOR_LIGHT_BLUE = (51, 153, 255)
COLOR_DARK_BLUE = (44, 137, 230)

# Window
window = (800, 600)
screen = pygame.display.set_mode(window)
pygame.display.set_caption("PySnake")

game_clock = pygame.time.Clock()  # Clock object


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
    game_over_sound.play()
    pygame.mixer.music.stop()
    return True


def draw_blue_square():
    for i in range(0, window[1] - 120, 32):
        if (i // 32) % 2:
            aux = 32
        else:
            aux = 0
        for j in range(aux, window[0], 64):
            pygame.draw.rect(screen, COLOR_DARK_BLUE, (j, 96 + i, 32, 32))


# Sounds
apple_sound = pygame.mixer.Sound('./assets/natanael.lucena.apple_crunch.wav')
game_over_sound = pygame.mixer.Sound('./assets/natanael.lucena.game_over.wav')
pygame.mixer.music.load('./assets/natanael.lucena.background_music.wav')

game_over_font = font(64)
continue_msg = font(25)

# Blink text effect variables
BLINK_EVENT = pygame.USEREVENT + 0
on_text_surface = continue_msg.render("Q-Quit/E-Play again", True, COLOR_LIGHT_GREY)
blink_rect = on_text_surface.get_rect()
blink_rect.center = screen.get_rect().center
off_text_surface = pygame.Surface(blink_rect.size)
off_text_surface.fill(COLOR_LIGHT_BLUE)
blink_surfaces = cycle([on_text_surface, off_text_surface])
pygame.time.set_timer(BLINK_EVENT, 580)
