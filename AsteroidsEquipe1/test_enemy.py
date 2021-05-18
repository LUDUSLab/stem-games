from enemy import SmallEnemyShip


def test_small_enemy_move():
    small_enemy = SmallEnemyShip()
    small_enemy.move()
    assert small_enemy.x != 0
