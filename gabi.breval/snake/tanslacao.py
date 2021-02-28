import pygame, sys

# Setup pygame/window ---------------------------------------- #
mainClock = pygame.time.Clock()
from pygame.locals import *

pygame.init()
pygame.display.set_caption('game base')
screen = pygame.display.set_mode((500, 500), 0, 32)

arrow_img = pygame.image.load('C:/Users/55929/Documents/STEM/stem-games/gabi.breval/snake/assets/arrow.png')

arrow_spin = 0

# Loop ------------------------------------------------------- #
while True:

    # Background --------------------------------------------- #
    screen.fill((0, 20, 0))

    arrow_spin += 1

    for i in range(4):

        arrow_copy = arrow_img.copy()
        if i == 0:
            arrow_copy = pygame.transform.flip(arrow_copy, True, False)
        if i == 1:
            arrow_copy = pygame.transform.scale(arrow_copy, (80, 10))
        if i == 2:
            arrow_copy = pygame.transform.rotate(arrow_copy, arrow_spin)
        screen.blit(arrow_copy, (50 + i * 120, 200))
    # Buttons ------------------------------------------------ #
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

    # Update ------------------------------------------------- #
    pygame.display.update()
    mainClock.tick(60)