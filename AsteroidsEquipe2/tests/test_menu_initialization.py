from os import path
import pytest
import menu

@pytest.fixture
def the_menu():
    return menu.Menu()

def test_ufo_image_path_finded(the_menu):
    assert path.exists(the_menu.ufo.sprite_path)


def test_asteroids_image_path_finded(the_menu):
    for asteroid in the_menu.asteroids:
        assert path.exists(asteroid.sprite_path)
