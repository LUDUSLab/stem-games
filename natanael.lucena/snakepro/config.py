import pygame

pygame.init()

# Colors
COLOR_LIGHT_GREY = (230, 230, 230)
COLOR_LIGHT_BLUE = (51, 153, 255)

# Window
window = (736, 480)
screen = pygame.display.set_mode(window)
pygame.display.set_caption("PySnake")

player_record = 0  # Player score record

BLINK_EVENT = pygame.USEREVENT + 0  # Event constant
