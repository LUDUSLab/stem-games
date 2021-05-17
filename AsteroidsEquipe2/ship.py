import pygame
import config
import gameobject

class Ship(gameobject.GameObject):
    UP = pygame.Vector2(0, -1)
    MANEUVERABILITY = 3
    ACCELERATION = 0.10

    def __init__(self):
        self.sprite_path = "./assets/ship.png"
        self.sprite = pygame.image.load(self.sprite_path).convert_alpha()
        self.direction = pygame.Vector2(self.UP)
        super().__init__((config.window.size[0]/2, config.window.size[1]/2), self.sprite, pygame.Vector2(0))
        self.rotated_sprite = pygame.image.load(self.sprite_path).convert_alpha()
        self.radius = self.sprite.get_height()/2
        self.img_rect = self.sprite.get_rect(center=(config.window.size[0]/2, config.window.size[1]/2))
        self.accelerating = False

    def rotate(self, clockwise=True):
        sign = 1 if clockwise else -1
        angle = self.MANEUVERABILITY * sign
        self.direction.rotate_ip(angle)
        self.rotated_sprite = pygame.transform.rotozoom(self.sprite, angle, 1.0)

    def accelerate(self):

        self.velocity += self.direction * self.ACCELERATION

    def check_ship_keys(self, key_pressed):
        if key_pressed[pygame.K_RIGHT] or key_pressed[pygame.K_d]:
            self.rotate(clockwise=True)
        elif key_pressed[pygame.K_LEFT] or key_pressed[pygame.K_a]:
            self.rotate(clockwise=False)
        if key_pressed[pygame.K_SPACE] or key_pressed[pygame.K_x] or key_pressed[pygame.K_UP] or \
                key_pressed[pygame.K_w]:
            self.accelerating = True
            self.accelerate()
        else:
            self.accelerating = False

    def display(self):
        self.move()
        if not self.accelerating:
            if self.velocity[1] < 0:
                self.velocity += pygame.Vector2(0, 0.008)
            elif self.velocity[1] > 0:
                self.velocity -= pygame.Vector2(0, 0.008)
            if self.velocity[0] < 0:
                self.velocity += pygame.Vector2(0.01, 0.008)
            elif self.velocity[0] > 0:
                self.velocity -= pygame.Vector2(0.01, 0.008)

        angle = self.direction.angle_to(self.UP)
        rotated_surface = pygame.transform.rotozoom(self.sprite, angle, 1.0)
        rotated_surface_size = pygame.Vector2(rotated_surface.get_size())
        blit_position = self.position - rotated_surface_size * 0.5
        config.window.screen.blit(rotated_surface, blit_position)
