import pygame
from config import *
from asteroids import *
from player import *
from enemy import *
from renderer import *
from particles import *

pygame.init()

game_on = True
count = 0

while game_on:
    game_clock.tick(60)
    count += 1

    if count % 100 == 0:
        asteroids.append(BigAsteroids())

    for i in asteroids:
        i.move()

    for i in player_missile:
        i.move()

    if not game_over:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            playership.player_left()
        if keys[pygame.K_d]:
            playership.player_right()
        if keys[pygame.K_w]:
            playership.move_up()
            if not keys[pygame.K_w]:
                playership.x += 10
                playership.y += 10
        playership.player_outside_screen()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_on = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if not game_over:
                    player_missile.append(PlayerMissile())

    screen.fill(color_black)

    for i in player_missile:
        i.draw(screen)

    for i in asteroids:
        i.draw(screen)

    playership.draw(screen)
    enemyship.draw(screen)

    pygame.display.update()

pygame.quit()
