from player import PlayerShip
from player import Missile


def test_player_turn_left():
    player = PlayerShip()
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


def test_missile():
    missile = Missile()
    missile.missile_move()
    assert missile.x != missile.xv
    assert missile.y != missile.yv
