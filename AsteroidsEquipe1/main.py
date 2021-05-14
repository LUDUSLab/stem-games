import pygame
from config import *
from asteroids import *
from player import *
from enemy import *
from renderer import *

pygame.init()

game_on = True

while game_on:
    game_clock.tick(60)
    for i in player_missile:
        i.player_missile.move()
    if not game_over:
        if count % 750 == 0:
            enemy.append(EnemyShip())
        for i, a in enumerate(enemy):
            a.x += a.xv
            a.y += a.yv
            if a.x > sw + 150 or a.x + a.w < -100 or a.y > sh + 150 or a.y + a.h < -100:
                enemy.pop(i)
            if count % 60 == 0:
                enemy_missile.append(EnemyMissile(a.x + a.w // 2, a.y + a.h // 2))

        for i, b in enumerate(EnemyMissile):
            b.x += b.xv
            b.y += b.yv
            if (player.x - player.w // 2 <= b.x <= player.x + player.w // 2) or \
                    (player.x - player.w // 2 <= b.x + b.w <= player.x + player.w // 2):
                if (player.y - player.h // 2 <= b.y <= player.y + player.h // 2) or \
                        (player.y - player.h // 2 <= b.y + b.h <= player.y + player.h // 2):
                    enemy_missile.pop(i)
                    break

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
                    player_missile.append(PlayerMissile())

    screen.fill(color_black)
    renderer.display(screen)
    for i in player_missile:
        i.player_missile.draw(screen)
    pygame.display.update()

pygame.quit()
