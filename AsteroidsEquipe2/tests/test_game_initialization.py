import pygame
import pytest
import menu

@pytest.fixture
def the_menu():
    return menu.Menu()

def test_menu_game_transition(the_menu):
    the_menu.check_game_enter(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_RETURN))
    assert the_menu.start_game
