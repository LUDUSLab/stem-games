import pygame

pygame.init()

# Size of objects
size_screen = (800, 640)
square = (32, 32)

# colours
color_black = (0, 0, 0)
color_white = (255, 255, 255)
color_green = (0, 255, 0)
color_red = (255, 0, 0)
color_73ED73 = (115, 237, 115)
color_0F6E9D = (15, 110, 157)

# Screen Setting
screen = pygame.display.set_mode(size_screen)
pygame.display.set_caption('Snake')

# sounds
eating_sound = pygame.mixer.Sound('assets/412068__inspectorj__chewing-carrot-a.wav')
game_over_sound = pygame.mixer.Sound('assets/533034__evretro__8-bit-game-over-sound-tune.wav')

# Loop and Clock
game_loop = True
game_clock = pygame.time.Clock()
