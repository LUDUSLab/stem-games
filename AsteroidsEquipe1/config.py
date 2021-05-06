import pygame
import player

pygame.init()

screen_size = (1000, 1000)
color_black = (0, 0, 0)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Asteroids")

game_on = True
game_clock = pygame.time.Clock()
while game_on:
    game_clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_on = False

    pygame.display.update()
    screen.fill(color_black)

pygame.quit()


