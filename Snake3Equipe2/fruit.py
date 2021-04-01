import cube
import pygame

# Sprite Loader
strawberry = pygame.image.load('assets/Strawberry.png')
banana = pygame.image.load('assets/Banana.png')
apple = pygame.image.load('assets/Apple.png')
watermelon = pygame.image.load('assets/Watermelon.png')


class Fruit(object):
    def __init__(self, fruit_type: int, pos: tuple):

        # List with sprite, value and probability of a fruit type
        fruits = (strawberry, 1), (banana, 2), (apple, 5), (watermelon, 10)

        self.type = fruit_type
        self.pos = pos
        self.sprite = fruits[fruit_type - 1][0]
        self.value = fruits[fruit_type - 1][1]
        self.fruit = cube.Renderer(self.pos, self.sprite)
