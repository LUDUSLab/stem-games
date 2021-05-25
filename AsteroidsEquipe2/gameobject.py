import pygame
import config
import ufo

class GameObject:
    def __init__(self, position, sprite, velocity):
        self.position = pygame.Vector2(position)
        self.sprite = sprite
        self.radius = sprite.get_width() / 2
        self.velocity = pygame.Vector2(velocity)
        self.explosion_animation_time = 5
        self.running_death_animation = False
        self.animation_aux = 1

    def wrap_position(self, position):
        x, y = position
        w, h = config.window.size
        if isinstance(self, ufo.UFO):
            return pygame.Vector2(x, y % h)
        else:
            return pygame.Vector2(x % w, y % h)

    def move(self):
        self.position = self.wrap_position(self.position + self.velocity)

    def collides_with(self, other_obj):
        distance = self.position.distance_to(other_obj.position)
        return distance < self.radius + other_obj.radius

    def explosion_animation(self):
        if self.explosion_animation_time <= 0:
            self.sprite = pygame.image.load(f'./assets/obstacle_explosion_{self.animation_aux}.png').convert_alpha()
            self.explosion_animation_time = 5
            self.animation_aux += 1
        self.explosion_animation_time -= 1

    def display(self):
        blit_position = self.position - pygame.Vector2(self.radius)
        config.window.screen.blit(self.sprite, blit_position)
