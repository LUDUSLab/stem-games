import pygame

pygame.init()

sw, sh = 1280, 720

screen = pygame.display.set_mode((sw, sh))
pygame.display.set_caption("Asteroids")

background = pygame.image.load("../AsteroidsEquipe1/assets/space1.png").convert_alpha()

shootSound = pygame.mixer.Sound('../AsteroidsEquipe1/assets/391660__jeckkech__projectile.wav')
backgroundSound = pygame.mixer.Sound('../AsteroidsEquipe1/assets/455016__gamer73__my-arcade.wav')
shipDestruction = pygame.mixer.Sound('../AsteroidsEquipe1/assets/387861__runningmind__explosion-player.wav')
asteroidsDestruction = pygame.mixer.Sound('../AsteroidsEquipe1/assets/387858__runningmind__explosion-asteroid.wav')
defeatSound = pygame.mixer.Sound('../AsteroidsEquipe1/assets/538151__fupicat__8bit-fall.wav')

pygame.mixer.music.set_volume(0.1)

color_black = (0, 0, 0)
color_white = (255, 255, 255)

game_clock = pygame.time.Clock()
