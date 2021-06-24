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
    #background_sound.play()
    count += 1

    if count % 65 == 0:
        asteroids.append(BigAsteroids())
    if count % 100 == 0:
        small_enemy.append(SmallEnemyShip())
    if count % 200 == 0:
        big_enemy.append(BigEnemyShip())

    for i, a in enumerate(small_enemy):
        for b in player_missile:
            if (b.x >= a.x and b.x <= a.x + a.w) or b.x + b.w >= a.x and b.x + b.w <= a.x + a.w:
                if (b.y >= a.y and b.y <= a.y + a.h) or b.y + b.h >= a.y and b.y + b.h <= a.y + a.h:
                    small_enemy.pop(i)
                    player_ship_explosion_sound.play()
                    hud.point += 1000
                    break

    for i, a in enumerate(big_enemy):
        for b in player_missile:
            if (b.x >= a.x and b.x <= a.x + a.w) or b.x + b.w >= a.x and b.x + b.w <= a.x + a.w:
                if (b.y >= a.y and b.y <= a.y + a.h) or b.y + b.h >= a.y and b.y + b.h <= a.y + a.h:
                    big_enemy.pop(i)
                    player_ship_explosion_sound.play()
                    hud.point += 200
                    break

    for a in asteroids:
        if (a.x >= player.x - player.w // 2 and a.x <= player.x + player.w // 2) or (
                a.x + a.w <= player.x + player.w // 2 and a.x + a.w >= player.x - player.w // 2):
            if (a.y >= player.y - player.h // 2 and a.y <= player.y + player.h // 2) or (
                    a.y + a.h >= player.y - player.h // 2 and a.y + a.h <= player.y + player.h // 2):
                asteroids.pop(asteroids.index(a))
                player.destroy()
                if a.w == 64:
                    na1 = MediumAsteroids()
                    na2 = MediumAsteroids()
                    na1.x = a.x
                    na2.x = a.x
                    na1.y = a.y
                    na2.y = a.y
                    asteroids.append(na1)
                    asteroids.append(na2)
                elif a.w == 32:
                    na1 = SmallAsteroids()
                    na2 = SmallAsteroids()
                    na1.x = a.x
                    na2.x = a.x
                    na1.y = a.y
                    na2.y = a.y
                    asteroids.append(na1)
                    asteroids.append(na2)
                break

        # bullet collision
        for b in player_missile:
            if (b.x >= a.x and b.x <= a.x + a.w) or b.x + b.w >= a.x and b.x + b.w <= a.x + a.w:
                if (b.y >= a.y and b.y <= a.y + a.h) or b.y + b.h >= a.y and b.y + b.h <= a.y + a.h:
                    if a.w == 64:
                        na1 = MediumAsteroids()
                        na2 = MediumAsteroids()
                        na1.x = a.x
                        na2.x = a.x
                        na1.y = a.y
                        na2.y = a.y
                        asteroids.append(na1)
                        asteroids.append(na2)
                        asteroids_explosion_sound.play()
                        hud.point += 50
                    elif a.w == 32:
                        na1 = SmallAsteroids()
                        na2 = SmallAsteroids()
                        na1.x = a.x
                        na2.x = a.x
                        na1.y = a.y
                        na2.y = a.y
                        asteroids.append(na1)
                        asteroids.append(na2)
                        asteroids_explosion_sound.play()
                        hud.point += 100
                    asteroids.pop(asteroids.index(a))
                    player_missile.pop(player_missile.index(b))
                    break

    for i in asteroids:
        i.move()
    for i in player_missile:
        i.move()
    for i in small_enemy:
        i.move()
    for i in big_enemy:
        i.move()

    hud.score_text = score_font.render(str(hud.point), True, color_white)

    if not game_over:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            player.player_left()
        if keys[pygame.K_d]:
            player.player_right()
        if keys[pygame.K_w]:
            player.acceleration()
            player.move_up()

        player.player_outside_screen()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_on = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if not game_over:
                    player_missile.append(PlayerMissile())
                    shoot_sound.play()
                    # enemy_missile.append(EnemyMissile())

    screen.blit(hud.background, (0, 0))

    for i in player_missile:
        i.draw(screen)
    for i in asteroids:
        i.draw(screen)
    for i in small_enemy:
        i.draw(screen)
    for i in big_enemy:
        i.draw(screen)

    player.draw(screen)
    hud.display_life(screen)
    hud.display_score(screen)
    pygame.display.update()

pygame.quit()
