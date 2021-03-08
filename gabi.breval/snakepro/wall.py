import pygame
from config import *

# Metal Bar -------------------------------------------------------------------------------------------------- #
metal = pygame.image.load(address('gabi.breval.metal_vazado.png', 'skin'))
metal = pygame.transform.scale(metal, [200, 550])
metal_copy = metal.copy()
metal_copy = pygame.transform.rotate(metal_copy, 180)
