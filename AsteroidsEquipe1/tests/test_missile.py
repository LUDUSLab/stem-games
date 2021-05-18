from AsteroidsEquipe1 import particles


def test_missile():
    missile = Missile()
    missile.missile_move()
    assert missile.x != missile.xv
    assert missile.y != missile.yv
