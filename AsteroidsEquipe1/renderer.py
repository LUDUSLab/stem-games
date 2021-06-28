import pygame


class Renderer(object):

    @staticmethod
    def draw(screen, image, position):
        screen.blit(image, position)

    @staticmethod
    def display(screen, asteroids):

        for asteroid in asteroids:
            asteroid.draw(screen, asteroid._image, (asteroid.x, asteroid.y))

        pygame.display.update()
