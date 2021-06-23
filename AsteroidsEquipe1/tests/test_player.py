import pytest
from player import PlayerShip


@pytest.fixture
def test_player_turn_left():
    player = PlayerShip
    player.player_left()
    assert player.angle != 0


def test_player_turn_right():
    player = PlayerShip()
    player.player_right()
    assert player.angle != 0


def test_player_move_up():
    player = PlayerShip()
    player.move_up()
    assert player.x != 0
    assert player.y != 0


def test_player_outside_screen():
    player = PlayerShip()
    player.player_outside_screen()
    assert player.x >= 1280
    assert player.y >= 720
