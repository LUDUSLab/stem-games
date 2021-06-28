from config import screen, background, font, sw, sh
import pygame


class Renderer(object):

    @staticmethod
    def draw(image, position):
        screen.blit(image, position)

    @staticmethod
    def write(string):
        return font.render(f"{string}", True,  (255, 255, 255))

    @staticmethod
    def display(asteroids, bullets, smallAlien, bigAlien, player, score, position):
        Renderer.draw(background, (0, 0))

        for asteroid in asteroids:
            Renderer.draw(asteroid._image, (asteroid.x, asteroid.y))

        for bullet in bullets:
            Renderer.draw(bullet.rect, (bullet.x, bullet.y))

        for alien in smallAlien:
            Renderer.draw(alien.img, (alien.x, alien.y))

        for alien in bigAlien:
            Renderer.draw(alien.img, (alien.x, alien.y))

        Renderer.draw(player.rotate, player.rotateRect)

        Renderer.draw(Renderer.write(score), (0, 0))

        for lives in position:
            Renderer.draw(player.img, lives)

        Renderer.draw(Renderer.write("ASTEROIDSTEAM1 POWERED BY ©2021 STEM-GAMES"), (0, sh - 80))

        pygame.display.update()
