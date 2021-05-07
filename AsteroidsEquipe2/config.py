import window
import pygame

pygame.font.init()

COLOR_BLACK = (0, 0, 0)
COLOR_LIGHT_GRAY = (154, 154, 154)

framerate = 60
clock = pygame.time.Clock()

window = window.Window()
class Text:
    def __init__(self, message: str, size: int, pos=(0, 0), path="./assets/VectorBattle-e9XO.ttf",
                 color=COLOR_LIGHT_GRAY):
        self.message = message
        self.size = size
        self.pos = pos
        self.path = path
        self.color = color
        self.font = pygame.font.Font(self.path, self.size)
        self.text = self.font.render(self.message, True, self.color)

    def display(self):
        window.screen.blit(self.text, self.pos)

def check_quit_event():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
