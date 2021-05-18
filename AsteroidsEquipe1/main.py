from config import *
from asteroids import *
from player import *
from enemy import *
from hud import *
# from renderer import *
from particles import *

pygame.init()

game_on = True
count = 0

while game_on:
    game_clock.tick(60)
    count += 1

    if count % 65 == 0:
        asteroids.append(BigAsteroids())
    if count % 700 == 0:
        small_enemy.append(SmallEnemyShip())
    if count % 1400 == 0:
        big_enemy.append(BigEnemyShip())

    for i in asteroids:
        i.move()
    for i in player_missile:
        i.move()
    for i in small_enemy:
        i.move()
    for i in big_enemy:
        i.move()

    if not game_over:
        hud.live += 3
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            playership.player_left()
        if keys[pygame.K_d]:
            playership.player_right()
        if keys[pygame.K_w]:
            playership.move_up()

        playership.player_outside_screen()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_on = False
            hud.live += 4
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if not game_over:
                    player_missile.append(PlayerMissile())
                    shoot_sound.play()
                    # enemy_missile.append(EnemyMissile())

    # screen.blit(hud.background, (0, 0))
    screen.fill(color_black)

    for i in player_missile:
        i.draw(screen)
    for i in asteroids:
        i.draw(screen)
    for i in small_enemy:
        i.draw(screen)
    for i in big_enemy:
        i.draw(screen)

    playership.draw(screen)
    hud.display_life(screen)
    hud.display_score(screen)
    pygame.display.update()

pygame.quit()
