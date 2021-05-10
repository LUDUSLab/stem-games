import pytest
from player import PlayerShip


def test_player_turn_left():
    player = PlayerShip()
    player.player_left()
    assert player.head != 4
