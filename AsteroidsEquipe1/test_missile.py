from particles import PlayerMissile


def test_player_missile():
    player_missile = PlayerMissile()
    player_missile.move()
    assert player_missile.x != player_missile.xv
    assert player_missile.y != player_missile.yv
