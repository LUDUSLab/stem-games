import pytest
from enemy import SmallEnemyShip
from enemy import BigEnemyShip


@pytest.fixture
def test_small_enemy_move():
    small_enemy = SmallEnemyShip()
    small_enemy.move()
    assert small_enemy.x != 0


def test_big_enemy_move():
    big_enemy = BigEnemyShip()
    big_enemy.move()
    assert big_enemy.x != 0
