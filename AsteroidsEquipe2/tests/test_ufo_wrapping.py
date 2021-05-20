import ufo
import pygame

def test_ufo_wrapping():
    ufo_test = ufo.UFO(pygame.Vector2(0, 40), 2)
    assert isinstance(ufo_test, ufo.UFO)
