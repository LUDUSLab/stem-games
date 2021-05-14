import pygame
from config import *
from asteroids import *
from player import *

pygame.init()

game_on = True

while game_on:
    game_clock.tick(60)

    for i in player_missile:
        i.missile_move()

    if not game_over:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            playership.player_left()

        if keys[pygame.K_d]:
            playership.player_right()

        if keys[pygame.K_w]:
            playership.move_up()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            game_on = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                if not game_over:
                    player_missile.append(Missile())

    screen.fill(color_black)
    playership.draw_playership(screen)
    for i in player_missile:
        i.draw_missile(screen)
    pygame.display.update()

pygame.quit()
