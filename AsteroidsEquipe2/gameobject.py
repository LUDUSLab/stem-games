import pygame
import config

class GameObject:
    def __init__(self, position, sprite, velocity):
        self.position = pygame.Vector2(position)
        self.sprite = sprite
        self.radius = sprite.get_width() / 2
        self.velocity = pygame.Vector2(velocity)

    @staticmethod
    def wrap_position(position):
        x, y = position
        w, h = config.window.size
        return pygame.Vector2(x % w, y % h)

    def move(self):
        self.position = self.wrap_position(self.position + self.velocity)

    def collides_with(self, other_obj):
        distance = self.position.distance_to(other_obj.position)
        return distance < self.radius + other_obj.radius

    def display(self):
        blit_position = self.position - pygame.Vector2(self.radius)
        config.window.screen.blit(self.sprite, blit_position)
