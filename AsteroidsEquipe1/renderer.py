from config import screen, background, sw, sh
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

        Renderer.draw(Renderer.write(score, 80), (70, -20))

        for lives in position:
            Renderer.draw(player.img, lives)

        pygame.display.update()

    @staticmethod
    def start():
        Renderer.draw(background, (0, 0))

        Renderer.draw(Renderer.write("PRESS ENTER TO START", 55), (460, 200))
        Renderer.draw(Renderer.write("| COIN | PLAY", 55), (525, 550))
        Renderer.draw(Renderer.write("ASTEROIDSTEAM1 POWERED BY ©2021 STEM-GAMES", 40), (385, 640))

        pygame.display.update()

    @staticmethod
    def game_over():
        screen.fill((0, 0, 0))

        Renderer.draw(Renderer.write("TEM QUE ESCREVER A MENSAGEMM DE GAME OVER AQUI!!!!!!!!!!!!!!!", 55), (0, 0))

        pygame.display.update()
