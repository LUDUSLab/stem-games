from config import screen, background
import pygame


class Renderer(object):

    @staticmethod
    def draw(image, position):
        screen.blit(image, position)

    @staticmethod
    def display(asteroids, bullets, smallAlien, bigAlien, player):
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

        pygame.display.update()
