from config import screen, background, sw, sh
from time import time
import pygame


class Renderer(object):

    @staticmethod
    def draw(image, position):
        screen.blit(image, position)

    @staticmethod
    def write(string, size):
        font = pygame.font.Font('../AsteroidsEquipe1/assets/ThinPixel7-1Yq0.ttf', size)
        return font.render(f"{string}", True, (255, 255, 255))

    @staticmethod
    def display(asteroids, bullets, smallAlien, bigAlien, player, score, highest_score,position):
        Renderer.draw(background, (0, 0))
        Renderer.draw(Renderer.write("©2021 STEM-GAMES", 40), (535, 640))

        for asteroid in asteroids:
            Renderer.draw(asteroid._image, (asteroid.x, asteroid.y))

        for bullet in bullets:
            Renderer.draw(bullet.rect, (bullet.x, bullet.y))

        for alien in smallAlien:
            Renderer.draw(alien.img, (alien.x, alien.y))

        for alien in bigAlien:
            Renderer.draw(alien.img, (alien.x, alien.y))

        Renderer.draw(player.rotate, player.rotateRect)

        Renderer.draw(Renderer.write(score, 80), (70, -20))

        Renderer.draw(Renderer.write(highest_score, 60), (sw / 2, -15))

        for lives in position:
            Renderer.draw(player.img, lives)

        pygame.display.update()

    @staticmethod
    def start():
        Renderer.draw(background, (0, 0))

        Renderer.draw(Renderer.write("A S T E R O I D S", 200), (130, 25))

        if time() % 1 > 0.5:
            Renderer.draw(Renderer.write("PRESS ENTER TO START", 55), (460, 350))

        Renderer.draw(Renderer.write("| COIN | PLAY", 55), (525, 550))
        Renderer.draw(Renderer.write("ASTEROIDSTEAM1 POWERED BY ©2021 STEM-GAMES", 40), (385, 640))

        pygame.display.update()

    @staticmethod
    def game_over(score, highest_score, txt):
        Renderer.draw(background, (0, 0))

        Renderer.draw(Renderer.write(score, 80), (70, -20))
        Renderer.draw(Renderer.write(highest_score, 60), (sw / 2, -15))

        Renderer.draw(Renderer.write(txt, 80), (10, 10))

        Renderer.draw(Renderer.write("YOUR SCORE IS ONE OF THE TEN BEST", 80), (75, 120))
        Renderer.draw(Renderer.write("PLEASE ENTER YOUR INITIALS", 80), (75, 170))
        Renderer.draw(Renderer.write("PUSH ROTATE TO SELECT LETTER", 80), (75, 220))
        Renderer.draw(Renderer.write("PUSH HYPERSPACE WHEN LETTER IS CORRECT", 80), (75, 270))

        Renderer.draw(Renderer.write("©2021 STEM-GAMES", 40), (535, 640))

        pygame.display.update()
